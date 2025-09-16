def convert_currency(dollars):
    """Return Peso and Yen given dollars."""
    peso = dollars * 57.17
    yen = dollars * 146.67
    return peso, yen

user_input = input("Enter currency in ($): ")

parts = user_input.split(",")
numbers = [int(p) for p in parts]

print("\nDollar($)\tPhil Peso(P)\tJpn Yen (Y)")

for d in numbers:
    peso, yen = convert_currency(d)
    print(f"{d:<10}\t{peso:,.2f}\t{yen:,.2f}")
