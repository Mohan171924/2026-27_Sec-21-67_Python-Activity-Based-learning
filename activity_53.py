prepared = [100, 120, 80]
served = [90, 100, 70]

for i in range(3):
    waste = prepared[i] - served[i]
    percent = waste / prepared[i] * 100

    print("Day", i + 1)
    print("Waste:", waste)
    print("Waste percentage:", percent)