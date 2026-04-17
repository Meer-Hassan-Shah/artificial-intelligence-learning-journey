#conditional statemnet

temp = int(input("Enter Temperature  : "))

if temp > 35 :
    print("it is hot weather .")

else:
    print("It is not hot weather .")




print("============          2nd Program start           =======================")




#conditional statement part II

marks = int(input("Enter Your Marks :   "))

if marks >= 90 :
    print("A+ GRADE")

elif marks >= 80 :
    print("A GRADE")

elif marks >= 70:
    print("B GRADE")


elif marks >= 60:
    print("C GRADE")

elif marks >= 50:
    print("D GRADE")


elif marks >=40 :
    print("passed but marks are not good")

else :
    print("YOU ARE FAIL")





print("============          3nd Program start           =======================")


age = int(input("What Is Your Age   :"))

if age>= 18:
    country =input("What Is Your Country    :").capitalize()      #capital or small latter problem solved
    if country == "Pakistan" :                  #Nested if
        print("You Can Vote in Pakistan")
    else:
        print("You Can Not Vote In Pakistan")

else:
    print("You Can Not Vote")
