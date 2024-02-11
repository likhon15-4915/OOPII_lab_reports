list=[]
list= [3,4,2,8,9,12,43]

print(list)
max= list.index(max(list))

#swap the minimal and the maximal element

min =list.index(min(list))
list[max], list[min] = list[min], list[max]

print(list)
