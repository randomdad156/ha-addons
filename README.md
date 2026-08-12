# Atelier — Home Assistant add-on

Run the Atelier side-business tracker inside Home Assistant, with all data stored
on your Home Assistant machine (your HA Green). Every device that opens it — phone,
tablet, PC, local or via Nabu Casa remote — reads and writes the **same** data file,
behind Home Assistant's login.

> This is a **Home Assistant add-on**, not a HACS integration. Add-ons are installed
> from Home Assistant's built-in **Add-on Store**, not from HACS.

## One-time setup

1. Create a new **public** GitHub repository (e.g. `atelier-addon`) and push the
   contents of this folder to it (so the repo has `repository.yaml` at the root and an
   `atelier/` folder next to it).
2. In `repository.yaml` and `atelier/config.yaml`, replace `YOUR_GITHUB_USERNAME`
   with your GitHub username.

## Install on Home Assistant (HAOS on your Green)

1. Home Assistant → **Settings → Add-ons → Add-on Store**.
2. Top-right **⋮ menu → Repositories**.
3. Paste your repo URL: `https://github.com/YOUR_GITHUB_USERNAME/atelier-addon` → **Add**.
4. Close the dialog; the **Atelier** add-on now appears in the store. Open it → **Install**.
5. After it installs, turn on **Start on boot** and **Show in sidebar**, then **Start**.
6. Open **Atelier** from the HA sidebar. It runs through HA ingress, so it's already
   behind your HA login and works remotely via Nabu Casa — no port forwarding.

## Moving your existing data in

Your current data lives in `atelier-data.json` (in your Atelier folder). To load it here:
open the add-on → sidebar **Import backup** → pick that file. From then on it's stored on
Home Assistant and shared across all your devices.

## Where the data lives / backups

- Live data: `/data/atelier-data.json` inside the add-on (persisted by HA).
- Server-side rolling backups: `/data/backups/` (last 14 days).
- The app also keeps in-browser daily backups and has Export/Import, as before.

## Updating the app later

When I ship a new version, replace `atelier/www/index.html`, bump `version:` in
`atelier/config.yaml`, push to GitHub — Home Assistant will offer an **Update** on the
add-on page. Your data is untouched by updates.
