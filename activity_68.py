before = [100, 150, 200]
after = [80, 120, 160]

for i in range(3):
    saved = before[i] - after[i]
    print("Appliance", i + 1)
    print("Units saved:", saved)