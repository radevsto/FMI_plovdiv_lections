#even numbers from 0 to 100
numberList = []

for number in range(101):
    if number%2 == 0:
        numberList.append(number)

print(numberList)
