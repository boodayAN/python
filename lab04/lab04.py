summa = int(input("Введите сумму в рублях:"))
zapr = input("Введите валюту (доллар, юани, евро):")
if zapr == "доллар":
    val = 92
elif zapr == "юани": 
    val = 13
elif zapr == "евро": 
    val = 100
print(summa/val, zapr)