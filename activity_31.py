key = ["A", "B", "C", "D", "A"]
ans = []
score = 0

for i in range(5):
    a = input("Enter answer: ").upper()
    ans.append(a)

for i in range(5):
    if ans[i] == key[i]:
        score = score + 1

print("Total marks:", score)