from lab_9_func import shift_left, shift_right

s1 = [-1,-2,3,4,5]
k = int(input("Введите k: "))

zero_plus = 0

for elem in s1:
    if elem >= 0:
        zero_plus += 1

if(zero_plus > k):
    shift_right(s1,k)
else:
    shift_left(s1,k)

print(s1)

    

