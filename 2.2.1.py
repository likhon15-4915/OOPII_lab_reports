def unique_list(fst):
 new_fst = []
 for a in fst:
 if a not in new_fst:
 new_fst.append(a)
 return new_fst
print(unique_list([1, 2, 3, 3, 3,4, 4, 5,8,12]))
