#RETAIL BILLING WITH MULTIPLE DISCOUNT RULES
tax_rates = {"grocery": 0.05, "clothing": 0.08,
             "electronics": 0.18, "other": 0.12}
items = []
n = int(input("Number of products: "))
for i in range(n):
    name = input("Product: ")
    category = input("Category: ").lower()
    qty = int(input("Quantity: "))
    price = float(input("Unit price: "))
    if category in tax_rates and qty > 0 and price >= 0:
        items.append((name, category, qty, price))
subtotal = sum(x[2]*x[3] for x in items)
rate = 0 if subtotal < 1000 else 0.05 if subtotal < 5000 else 0.10 if subtotal < 10000 else 0.15
discount = min(subtotal*rate, 2000)
total_tax = 0
for x in items:
    amount = x[2]*x[3] - discount*(x[2]*x[3]/subtotal)
    tax = amount*tax_rates[x[1]] if subtotal else 0
    total_tax += tax
    print(x[0], "Tax:", round(tax, 2))
print("Subtotal:", subtotal, "Discount:", discount)
print("Tax:", round(total_tax, 2))
print("Final bill:", round(subtotal-discount+total_tax, 2))
