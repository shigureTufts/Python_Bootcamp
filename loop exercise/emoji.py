counter = 1
while counter <= 10:
    print("\U0001f600" * counter)
    counter += 1

print()
for integer in range(1, 11):
    print("\U0001f600" * integer)

print()
counter = 1
while counter <= 20:
    print("  " * int((20-counter)/2), "\U0001f600" * counter, " " * int((20-counter)/2))
    counter += 2