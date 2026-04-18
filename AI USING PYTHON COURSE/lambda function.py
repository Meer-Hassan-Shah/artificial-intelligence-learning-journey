
#lambda function 1st example
add = lambda a,b : a+b
print(add(3,7))



#lambda function 2nd example 
double_it = lambda c : c * 2 
print(double_it(6))


#lambda function 3nd example 

number = [1,3,5,7,9,10]
sqaures = list(map(lambda y : y * y, number))

print(sqaures)


#lambda function 4nd example 

num = [1,2,3,4,5,6,4,8,4,3,3,2,1]
odd_number = list(filter(lambda z: z % 2 != 0,num))
print(odd_number)
