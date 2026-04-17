#set
my_set={0 ,1 ,2 ,3 ,3 ,4 ,5 ,6 ,1 ,3 ,4 ,2 }     # not allowed duplicate
print(my_set)

#set method 
my_set.add(10)     #add item
my_set.remove(6)   #remove item
print(my_set) 


#set operations 
A={1,2,3,4}
B={4,5,6,7}

print(A.union(B))                        # combined both set but skip duplicate numbers
print(A.intersection(B))                 # only dupliacate can be show
print(A.difference(B))                   # set A can be check first than give the output



