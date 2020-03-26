import math


# 1 задание
def tripleDivideExpressionFirstTask(x):
    if (x != -7):
        result = 1 + (2 / (3 + (4 / (5 + (6 / (7 + x))))))
    else:
        return "This x provides division by thero!"

    return result


# 2 задание
def zetResultSecondTask():
    x = (2.468 / ((3.69 / math.sqrt(pow(10, 3))) ** (1. / 3))) ** (1. / 5)
    y = (25 / (125 / ((6.99 / (pow(300000, 2))) ** (1. / 9))))

    z = ((pow(x, 2) + pow(y, 2)) / (1 - ((pow(x, 2) - pow(y, 2)) / 2)))

    return z


# 3 задание
def aLotOfSqrtThirdTask(x):
    if (x == 5 or x == 0):
        return "With this x, expression have no solution"
    else:
        # Закоментированный пример ниже выводит "Math domain error", когда у нас корень выходит отрецательным.
        # По этому было решено оставить вариант с комплексными числами
        ## result = (math.sqrt((2 * x / (x - 5))) / (((math.sqrt(2 * x) - math.sqrt(x - 5)) / (math.sqrt(2 * x) + math.sqrt(x - 5))) - ((math.sqrt(2 * x) + math.sqrt(x - 5)) / (math.sqrt(2 * x) - math.sqrt(x - 5)))))
        result = ((2 * x / (x - 5)) ** (0.5)) / \
                 ((((2 * x) ** (0.5) - (x - 5) ** (0.5)) / ((2 * x) ** (0.5) + (x - 5) ** (0.5))) -
                  (((2 * x) ** (0.5) + (x - 5) ** (0.5)) / ((2 * x) ** (0.5) - (x - 5) ** (0.5))))

    return result


# 4 задание
def sinAndCosExpressionFourthTask():
    z = 1 / (math.sqrt(1 + (math.sin(1 / (math.sqrt(2 + math.cos(1 / (math.sqrt(3 + math.sin(1 / 4))))))))))
    return z


# 5 задание
def averageValueOfTwoNums(a, b):
    if (isinstance(a, int) and isinstance(b, int)):
        return (a + b) / 2
    else:
        return "Only integers are valid in this method"


# 6 задание
def sugarPriceAndAmount():
    print("How musch kg of sugar is in the shop yet? \n")

    amount = float(input())
    if (amount < 0):
        return "Invalid input"

    print("What is the price for 1 kg? \n")

    priceForKg = float(input())
    if (priceForKg < 0):
        return "Invalid input"

    print("%d kg sugar is in the shop, for the price %d for 1 kg " % (amount, priceForKg))

    print("Enter additional sugar: ")

    additionalAmount = float(input())
    if (additionalAmount < 0):
        return "Invalid input"

    print("Enter price for this batch: ")

    anotherPriceForKg = float(input())
    if (anotherPriceForKg < 0):
        return "Invalid input"

    return "Amount of sugar after new batch of sugar is %d, for the price %d for 1 kg" \
           % (amount + additionalAmount, (amount * priceForKg) + (additionalAmount * anotherPriceForKg))


# Задание 7
# В задании написано вернуть мин.число + его номер, поэтому возвращаю индекс + 1.
# Если имелось ввиду вернуть индекс, то исправлю
def getMinElementAndItsIndex(a, b, c, d, e):
    array = [a, b, c, d, e]

    return "Min element is %d. Its position is %d" % (min(array), array.index(min(array)) + 1)


# print(tripleDivideExpressionFirstTask(7))
#print(zetResultSecondTask())
# print(aLotOfSqrtThirdTask(6))
# print(sinAndCosExpressionFourthTask())
# print(averageValueOfTwoNums(2, 3))
# print(sugarPriceAndAmount())
# print(getMinElementAndItsIndex(4, -6, 2, 0, 1))


### ЧАСТЬ 2

# Задание 1

# Список из семи любых названий предметов в расписании.
subjects = ["ООП", "ЧМ", "БД", "ТКП", "АиП", "ТА", "ТеорВер"]

# Распечатайте первый, третий, четвертый, последний и предпоследний элементы списка.
print(subjects[0], subjects[2], subjects[3], subjects[-1], subjects[-2])

# Разбейте с помощью срезов список на три части - в первой части три элемента, во второй - один, в третьей - тоже три.
firstPart = subjects[0:3]
secondPart = subjects[3:4]
thirdPart = subjects[4:7]

print(firstPart, secondPart, thirdPart)

# Создайте новый список mnogospisok, в который бы в виде элементов входили три части из предыдущего задания
multiList = [firstPart, secondPart, thirdPart]
print(multiList)

# Поменяйте местами первый и последний элементы mnogo_spisok
multiList[0], multiList[-1] = multiList[-1], multiList[0]
print(multiList)

# Добавьте к mnogo_spisok еще один, любой элемент
multiList.append(["Вышмат", "Физика"])
print(multiList)

# Добавьте еще один, любой элемент к любому из подсписков mnogo_spisok
multiList[2].append(["Психология", "Философия"])
print(multiList)

# Удалите из списка mnogo_spisok все элементы кроме первого
del multiList[1:]
print(multiList)

# Задание 2
# ФИО: Ярчук Александр Александрович

fullName = input() + " " + input() + " " + input()
print(len(fullName))

surname = fullName[0:5]
name = fullName[6:15]
patronymic = fullName[16:len(fullName)]
print(surname, name, patronymic)

print(fullName.count("о"))
print(fullName.count("е"))

fullName_S = input() + "\n" + input() + "\t" + input()
print(len(fullName_S))
