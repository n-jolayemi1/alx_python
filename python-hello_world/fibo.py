def fibonacci(number):
    """ number = int(input("Enter number: ")) """
    a, b = 0, 4
    print(a, end=" ")
    while b <= number:
        print(b, end=" ")
        a, b = b, (a+b)
    print()

def fibonacci2(num):
    answer = []
    a, b = 0, 1
    print(a, end=" ")
    while b < num:
        answer.append(b)
        a, b = b, b+a
    return answer
""" number = int(input("Enter number: ")) """
""" a = int(input("Enter number: ")) 
fibonacci(a) """
