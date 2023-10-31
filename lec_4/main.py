def is_even(number:int):
    if number % 2 == 0:
        return True
    else:
        return False

li = input("Input your numbers ")
li = li.split()

even_numbers = list()
odd_numbers = list()

for i in li:
    if is_even(int(i)):
        even_numbers.append(int(i))
    else:
        odd_numbers.append(int(i))

print('Even numbers: ', even_numbers) 
print('Odd numbers: ', odd_numbers) 
