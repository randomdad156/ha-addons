#!/usr/bin/env python3
"""Tiny web server for the Atelier Home Assistant add-on.
Serves the single-page app and stores its data in /data/atelier-data.json
(persisted by Home Assistant across restarts/updates), with 14 daily backups.
Reached only through Home Assistant ingress (authenticated)."""
import json, os, time, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DATA_DIR = "/data"
DATA_FILE = os.path.join(DATA_DIR, "atelier-data.json")
BACKUP_DIR = os.path.join(DATA_DIR, "backups")
INDEX = "/app/www/index.html"
PORT = 8099
MAX_BACKUPS = 14
_lock = threading.Lock()


def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return f.read()
    return b"null"


def write_data(body):
    with _lock:
        os.makedirs(DATA_DIR, exist_ok=True)
        tmp = DATA_FILE + ".tmp"
        with open(tmp, "wb") as f:
            f.write(body)
        os.replace(tmp, DATA_FILE)
        try:
            os.makedirs(BACKUP_DIR, exist_ok=True)
            day = time.strftime("%Y-%m-%d")
            with open(os.path.join(BACKUP_DIR, "atelier-%s.json" % day), "wb") as f:
                f.write(body)
            files = sorted(x for x in os.listdir(BACKUP_DIR)
                           if x.startswith("atelier-") and x.endswith(".json"))
            while len(files) > MAX_BACKUPS:
                os.remove(os.path.join(BACKUP_DIR, files.pop(0)))
        except Exception:
            pass


class Handler(BaseHTTPRequestHandler):
    def _is_data(self):
        return self.path.split("?", 1)[0].rstrip("/").endswith("/data")

    def do_GET(self):
        if self._is_data():
            body = read_data()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        with open(INDEX, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self._is_data():
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length)
            try:
                json.loads(body)
            except Exception:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"invalid json")
                return
            write_data(body)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return
        self.send_response(404)
        self.end_headers()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Atelier add-on listening on :%d" % PORT, flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
