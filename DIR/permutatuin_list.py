def permutation(lis1,list2):
    if len(lis1)!=len(list2):
      return False
    lis1.sort()
    list2.sort() 
    if lis1==list2:
        return True
    else:
        return False
list1=['a','b','c']
list2=['c','b','a']
print(permutation(list1,list2))
        