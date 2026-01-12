import copy

#general copy
a=[1,2,3,[5,6,7]]
# b=copy.copy(a)
# b.append(10)
# print(b)
# print(a)
# b[3][1]=9
# print(a)
# print("\n")
print("deep copy:")
print("\n")

b=copy.deepcopy(a)
b.append(10)
print(b)
print(a)
b[3][1]=9
print(a)