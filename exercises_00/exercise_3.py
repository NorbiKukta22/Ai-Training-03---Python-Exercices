words = input("Please enter any number of words: ").strip().split()

middle = len(words) // 2

first_half = words [:middle]
second_half = words [middle:]

first_half.sort()
second_half = sorted(second_half, key = lambda x: ord(x[-1]))

print(first_half)
print(second_half)

zipped = zip(first_half, second_half)
print(list(zipped))
