from functools import reduce

l = [["name", "dinner"], ["Abraham", "Avi"], ["Hello", "Tree", "Door"], ["Name", "Glass", "Two", "am"]]

# all steps
print(list(filter(lambda x: len(x) > 4, (set(reduce(lambda x,y:x+y,l))))))



# split to sub-steps:
#1 unify all sublists into one list
l1 = list(reduce(lambda x,y:x+y, l))

#2 remove duplicates from unified list
l2 = list(set(l1))

#3 print all strings that have more than 2 chars in the middle
print(list(filter(lambda x: len(x) > 4, l2)))

