# Kiosk Manager

A command-line inventory and sales management tool built for a small Nairobi kiosk owner, as a capstone project covering Sessions 1–6: variables, conditionals, loops, functions, data structures (dict/list/tuple/set), and string/file handling. No classes, no `try/except`, no external modules beyond the standard library.

## What it does

On startup, the program asks for the kiosk's name and the owner's name, then presents a menu-driven system for managing stock, recording sales, and reviewing sales performance - all backed by a persistent file so nothing is lost between runs.

## Core Features

**1. Welcome & Setup**
Asks for the kiosk name and owner name, cleans both with `.strip().title()`, and prints a formatted welcome banner.

**2. Main Menu Loop**
A `while True` loop drives the whole program. Menu input is validated with `.isdigit()` before conversion, so typing letters or an out-of-range number never crashes the program - it just reprints a friendly message and shows the menu again.

**3. Inventory Management**
Stock is stored as a dictionary of `{product: {"price": ..., "quantity": ...}}`. Supports viewing the full inventory in aligned columns, and restocking - either adding to an existing product or creating a brand-new one on the fly.

**4. Selling a Product**
Checks there's enough stock before selling anything; if not, nothing changes and a clear message prints. On a successful sale, stock is reduced, the total is calculated, and the sale is recorded as a `(product, quantity, total)` tuple in a sales log list. A set tracks every unique product sold in the session.

**5. Sales Report**
Loops through the sales log to print every sale, accumulates total revenue, reports how many unique products were sold (from the set), and identifies the best-selling product by quantity.

**6. Search Products**
Case-insensitive, partial-match search using `.lower()` and the `in` operator - searching `"rea"` finds `"Bread"` regardless of how the user or the stored name is cased.

**7. Saving and Loading Data**
On startup, the program loads `inventory.txt` if it exists; otherwise it starts from a small default inventory. On exit, the current inventory is written back to `inventory.txt` (overwritten, since it should always reflect the latest true state), and this session's sales are appended to `sales_log.txt` (never overwritten, so history accumulates across sessions).

> **Note on save files:** `inventory.txt` and `sales_log.txt` are tied to the folder the script runs from, not to the kiosk name typed at startup. Running the program again in the same folder loads the same save files regardless of what name is entered - the kiosk name is currently just banner text, not a save-file key.

## Running it

```bash
python kiosk_manager.py
```

## Testing

`test_input.txt` contains a full scripted run covering every feature plus edge cases (insufficient stock, unknown product, non-numeric input, invalid/out-of-range menu choices). Run it non-interactively with:

```bash
python kiosk_manager.py < test_input.txt
```

Run it twice in a row to confirm inventory persists and the sales log accumulates across sessions rather than resetting.

## Status

Core (Features 1–7) complete and tested against the brief's self-check list.

## What's next

Optional "More Features" add-ons will be built one at a time, each on its own branch off `main`:

- Shopping basket checkout
- Change calculator
- Top-selling leaderboard
- Restock alert file
- Customer loyalty tracker
- Human-readable daily report
- Bulk restock mode
- Simple PIN check at startup