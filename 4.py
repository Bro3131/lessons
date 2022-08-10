problem = input()
def calc(exp):
    lst = exp.split(' ')
    dictionary = { '+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b: a*b, '/': lambda a,b: a/b}
    znak = dictionary[lst[1]]
    total = znak(int(lst[0]), int(lst[2]))
    return total
print(calc(problem))
