first_number = int(input())
operation = input("Введите операцию: ")
second_number = int(input())

def result(first_num, op, second_num):
    if op == "+":
        return first_num + second_num
    elif op == "-":
        return first_num - second_num
    elif op == "*":
        return first_num * second_num
    elif op == "/":
        if second_num != 0:
            return first_num/second_num
        else: 
            return "На ноль делить нельзя"
    else:
        return "Такой опреации не существует"

print(result(first_number, operation, second_number))