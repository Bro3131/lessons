list1 = list(input())
def create_dict(lst):
    lenght = len(lst)
    list2 = list(range(lenght))
    dictionary = dict(zip(list2, lst))
    return dictionary
print(create_dict(list1))

