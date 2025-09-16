
rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

table = []

for r in range(rows):
    print(f"\nRow {r + 1}")
    row = []
    for c in range(cols):
        num = float(input(f"Enter number for Column {c + 1}: "))
        row.append(num)
    table.append(row)


print("\nThe numbers are:")
for r in table:
    print(" ".join(str(x) for x in r))


target = float(input("\nSearch: "))


found = {}

for r in range(rows):
    for c in range(cols):
        if table[r][c] == target:
            found.setdefault(r, []).append(c)


if found:
    print(f"\nNumber {target} found at:")
    for r, cols_found in found.items():
        for c in cols_found:
            pos: tuple = (r + 1, c + 1)
            print(f"  Row {pos[0]}, Col {pos[1]}")
else:
    print("\nNumber not found.")
