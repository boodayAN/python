import random
botNumber = random.randint(1, 10)
playerNumber = int(input("ведите число"))
while playerNumber != botNumber:
    if playerNumber > botNumber:
        razn = playerNumber - botNumber
        znach = "меньше"
    else:
        razn = botNumber - playerNumber
        znach = "больше"
    if razn <= 2:
        temp = "Горячо"
    elif razn == 3 or razn == 4:
        temp = "Тепло"
    else:
        temp = "Холодно"
    print(f"{temp}, ты не угадал, моё число {znach}")
    playerNumber = int(input("ведите число"))
print(f"ты угадал, моё число: {botNumber}")