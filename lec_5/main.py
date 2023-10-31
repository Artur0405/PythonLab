def sum_of_elements(li: list, oper: bool = False):
    if oper:
        return sum(li)
    else:
        result = 0
        for i in li:
            if i > 0:
                result += i
        return result

def convert_list_to_int(li):
    new_list = [int(element) for element in li]
    return new_list

def yes_or_no(oper: str):
    if oper.lower() == 'yes':
        return True
    if oper.lower() == 'no':
        return False
    else:
        print('Your answer is not clear')
        
li = input("Input your numbers ")
oper = yes_or_no(input("exclude negative numbers: "))

li = convert_list_to_int(li.split())

print(sum_of_elements(li, oper))