numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
entered_number = int(input('Введите число от 3 до 20: '))
key_door = []
for i in range(entered_number ,numbers[entered_number]):
    for j in range(1, len(numbers)):
       for l in range(j,len(numbers)):
           sum_ = j + l
           if  i % sum_ == 0:
               key_door.append([j,l])

    print(i , key_door)












