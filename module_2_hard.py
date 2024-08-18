def code(numbers):
    otvet = []
    for i in range(1, numbers + 1):
        for j in range(i + 1, numbers + 1):
            sum_ = i + j
            if numbers % sum_ == 0:
                otvet.append(i)
                otvet.append(j)
    return otvet
numbers = int(input('Ввидите число от 3 до 20: '))
otvet = code(numbers)
print("Результат разложения чила: ", *otvet)