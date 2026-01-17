
tax_rate = 0.20
price_input = input("Please enter the price: ")
price = float(price_input)
total_price = price + (price * tax_rate)
print("Total: ${:.2f}".format(total_price))
