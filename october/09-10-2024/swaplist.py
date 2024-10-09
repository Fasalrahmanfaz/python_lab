lst=[1,2,3,4,5,6,7,8,9]
length = len(lst)
print("before swap",lst)

temp = lst[0]
lst[0] = lst[length-1]
lst[length-1] = temp
print("after swap",lst)
