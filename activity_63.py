prices = [100, 120, 110]

for i in range(1, len(prices)):
    change = prices[i] - prices[i - 1]
    print("Price change:", change)