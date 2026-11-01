items = ["pencil", "eraser", "notebook"]
in_stock = [item for item in items if item != "eraser"]
print(in_stock)

items = ["pencil", "eraser"]
stock_counts = [12, 0]
inventory = {item: count for item, count in zip(items, stock_counts)}
print(inventory)