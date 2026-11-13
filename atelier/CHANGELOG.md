# Changelog

## 1.4.1 (2026-11-12)

- Layout fixes for multi-item orders: each item now shows on its own line in the Orders table (long combined names were pushing the edit/delete buttons off-screen), and in the order dialog the product dropdown gets a full-width line so long product names are readable.

## 1.4.0 (2026-11-09)

- Orders can now contain multiple items: one order holds several products, each with its own quantity and sell price (per-item suggested prices, inventory still decrements per item, dashboard revenue split per product). Also fixed same-day ordering in the Orders list - orders now remember when they were created, so the newest-added appears first within the same date.

## 1.3.0 (2026-08-17)

- Trendyol shipping now follows the Under-Threshold Support Model: a reduced price-band fee (3/4/5/8) applies automatically when the Trendyol selling price is under the threshold (125 RON) and the parcel is under the max weight (10 kg); otherwise the standard weight-based FAN rate applies. Threshold, max weight, and both fee tables are editable in Settings.

## 1.2.0 (2026-08-17)

- Trendyol shipping is now weight-based (FAN Courier, Romania) using each parcel weight, replacing the old sale-price bands. Parcels under 1 kg = 10.55 RON; the Settings shipping-bands editor is now in kg.

## 1.1.1 (2026-06-02)

- Product/pack code is now editable when editing. Renaming a code checks for collisions and automatically remaps any pack components that referenced the old code.

## 1.1.0 (2026-06-02)

- Adopted semantic versioning: features bump the minor version, fixes bump the patch. This 1.1.0 rolls up the recent feature work (pack builder, inventory materials with automatic stock decrement, Trendyol shipping bands) and the product-breakdown cleanup. The 1.0.x history below is kept as-is.

## 1.0.14 (2026-06-02)

- Product expanded breakdown now shows the product-level price (costs + desired profit + PFA tax) without the channel-specific platform cut and Genius/shipping — those appear per channel in the Price-by-channel table below.

## 1.0.13 (2026-06-02)

- Fixed the Save settings button spacing in Settings (it was cramped against the status checkboxes).

## 1.0.12 (2026-06-02)

- Trendyol prices now include the platform shipping fee (Taxă de expediere) by sale-price band, mirroring how Emag Genius works. Genius still applies only to Emag. Added a Trendyol shipping bands editor in Settings; the Price-by-channel column shows Genius for Emag and shipping for Trendyol.

## 1.0.11 (2026-06-02)

- The app file no longer embeds any data — all products, platforms, inventory, orders and expenses live only in atelier-data.json. A fresh app starts empty; Reset now clears everything.

## 1.0.10 (2026-06-02)

- New expense no longer defaults its category to Materials — pick from the dropdown.

## 1.0.9 (2026-06-02)

- Desired profit and Genius tax labels are single-line so their inputs align with Packaging cost / their row.

## 1.0.8 (2026-06-02)

- Product editor layout: Additional cost aligns with Material cost, the inventory-materials list sits under them, and the Emag & Trendyol tiers share a row.

## 1.0.7 (2026-06-02)

- Inventory items now have a unit price. Products can list inventory materials used (with quantities) whose cost is added to the price alongside the manual Additional cost. Placing a new order automatically decreases the stock of those inventory items. Packs inherit their components materials.

## 1.0.6 (2026-06-02)

- Fixed modal layout overflow — long product names (e.g. packs) no longer push the right-hand fields outside the dialog.

## 1.0.5 (2026-06-02)

- Pack builder: packaging cost is now editable (auto-fills to the largest component box, override it for a bigger box).

## 1.0.4 (2026-06-02)

- Pack builder now has an editable Additional materials field (e.g. "3x tea light").

## 1.0.3 (2026-06-02)

- New pack builder — create a product from existing products + quantities. It sums material weight, build time and additional cost; keeps the highest material rate, packaging (one box) and Emag/Trendyol tiers; and prices it automatically. Packs cannot be used as components of another pack.

## 1.0.2 (2026-06-02)

- Expense category dropdown now lists the categories already used in your expenses (plus common defaults), instead of a fixed set.

## 1.0.1 (2026-06-02)

- Lighter build — sample orders/expenses are no longer bundled inside the app file (your data loads from atelier-data.json), dropping the file from ~160 KB to ~60 KB. “Reset to seeded data” now clears to an empty ledger.

## 1.0.0 (2026-06-02)

- First versioned release — dashboard with yearly archives, orders (inline status, product-scoped channels), per-product pricing (RON/kg material, PFA & Emag Genius, price-by-channel), inventory, expenses, platforms with PFA flag, daily auto-backups (rolling 7), file auto-save with one-click reconnect, and a collapsible, alphabetical product list.
