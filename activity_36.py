s = input("Enter a sentence: ").lower()
words = s.split()

for word in words:
    if words.count(word) > 1:
        print(word)
        words = [w for w in words if w != word]