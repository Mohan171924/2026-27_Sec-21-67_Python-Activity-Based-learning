marks = [
    [80, 75, 90],
    [60, 70, 65],
    [85, 95, 88]
]

for row in marks:
    total = sum(row)
    avg = total / len(row)
    print("Total:", total)
    print("Average:", avg)