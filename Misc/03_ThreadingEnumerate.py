races = ["aa", "bb", "cc"]

for i in races:
    print(i)
print("=" * 50)

for item in enumerate(races):
    print(item)
print("=" * 50)

for i, name in enumerate(races):
    print(i, name)
