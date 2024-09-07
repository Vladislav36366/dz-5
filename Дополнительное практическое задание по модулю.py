numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
entered_number = int(input('Введите число от 3 до 20'))
key_door = []
#if entered_number == 20:
    #entered_number = entered_number - 1
for i in range(entered_number ,numbers[entered_number]):
    for j in range(1, len(numbers)+1):
       for l in range(1,len(numbers)+1):
           sum_ = j + l
           if i % sum_ == 0:
               key_door.append(j)
               key_door.append(l)
    a = key_door[:len(key_door)//2]
    b = key_door[len(key_door)//2:]
    print(i , a)
    key_door = []












