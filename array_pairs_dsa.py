import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10])
multp=0
for i in range (len(array)):
    for j in range(i+1,len(array)):
       if array[i]*array[j] > multp:
           multp=array[i]*array[j]
           pairs=str(array[i])+",",str(array[j])
print(pairs)
print(multp)            
           
       