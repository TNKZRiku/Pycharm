#sort

list = [['a',10],['b',55],['c',33]]

# def list_sort(elements):
#     return elements[1]

# list.sort(key = list_sort,reverse = True)
# print(list)

list.sort(key = lambda elements: elements[1],reverse = True)
print(list)

#sort中第一个key是排序依据 传入一个函数