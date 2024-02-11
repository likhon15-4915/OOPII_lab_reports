list=[]
list= [3,4,2,8,9,12,43]
print(list)

#swap the minimal and the maximal element

max= list.index(max(list))
min =list.index(min(list))
list[max], list[min] = list[min], list[max]

print(list)
