numbers = [3,1,8,2,6,4]
index = 0
size = len (numbers)
max = numbers[index]
min = numbers[index]
sum = 0
while index < size :
    if numbers[index] > max :
        max = numbers[index]
        max_index = index
    elif numbers[index] < min :
        min = numbers[index]
        min_index = index
    sum = sum + numbers[index]    
    index += 1
print("Сумма всех элементов =", sum)
sum = sum - min - max
print("Сумма элементов между макс и мин =", sum)
print("Индекс максимального элемента =", max_index, "значение", max)
print("Индекс минимального элемента =", min_index, "значение", min)