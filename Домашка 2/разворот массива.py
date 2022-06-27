numbers = [3,1,8,2,6,4]
index = 0
size = len (numbers)
cycles = 0
print("Прямой  массив    =", numbers)
while cycles < size-1 :
    while index < size -1 :
        buff = numbers[index]
        numbers[index] = numbers[index + 1]
        numbers[index + 1] = buff
        index ++ # проверка работы "++" вместо "+= 1" ?
    index = 0
    size -- # будет ли работать с "--" вместо "-= 1" ?
    
print("Зеркальный массив =", numbers)
