def Char(text):
    counts = {}
    for ch in text:
        if ch != " " and ch != ",":
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
    return counts


string = input("Enter string: ")

result = Char(string)

output = []
for k, v in result.items():
    output.append(f"{k}={v}")

print(", ".join(output))
