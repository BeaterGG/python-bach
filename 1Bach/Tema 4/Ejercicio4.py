palabra=input("Dime una palabra y te digo sus vocales:")

vocales = ("a","e","i","o","u")

for x in vocales:
    if x in palabra:
        print(x)
        