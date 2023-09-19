from collections import Counter

s = "This is a sentence and i want to get is a dic or not is up in the down"

words = s.split()
c = Counter(words)

print(c.most_common()[:-4:-1])
