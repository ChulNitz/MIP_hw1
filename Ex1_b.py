import random


def change_multiples_to_one(arr, num):
    for i in range(len(arr)):
        if arr[i] % num == 0:
            arr[i] = 1
    return arr


my_array = [random.randint(1, 50) for i in range(10)]
my_num = random.randint(1, 5)

print("random input array:", my_array)
print("random input number:", my_num)
print("Output array:", change_multiples_to_one(my_array, my_num))