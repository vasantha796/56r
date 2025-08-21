# def check_num_staus(num):
#     if num>0:
#         print("positive")
#     elif num==0:
#         print("zero")
#     else:
#         print("negative")
# num_input=input("enter a number")
# check_num_staus(input)                    



# terinary operator 4 lines of code is written in 1 line

# def even_or_odd(num1):
#     res="even" if num1%2==0 else "odd"
# #     print(res)

# even_or_odd=(num1=25)


# def eligible_to_vote_or_not(n):
#     res="eligible" if n>=18 else "not eligible"
#     print(res)

# eligible_to_vote_or_not=(19)    




# def print_greatest_of_2_numbers(a,b):
#     res="greatest" if a>b else "lowest"
#     print(res)

# print_greatest_of_2_numbers(2,6)    




# def print_greatest_of_2_numbers(a,b):
#     return a if a>b else b
# print(print_greatest_of_2_numbers(3,5))

# def print_greatest(a,b):
#     return a if a>b else "both are equal" if a==b else b
# print(print_greatest(3,3))


# def simple_cal(n1,n2,op):
#     if op== "+"or op=="ADD":
#         print(n1+n2)
#     elif op=="-" or op=="SUB":
#         print(n1-n2)
#     elif op== "*" or op=="MUL":
#         print(n1*n2)
#     elif op== "/" or op=="DIV":
#         print(n1/n2) if n2 !=0 else print("not possible")

# n1=input("enter your number")
# n2=input("enter your number")
# input_op=input("enter your o")


# simple_cal(n1,n2,"op")
# bitwise operators :

# age=19
# if age>18:
#     print("eligible to vote")
# else:
#     print("not eligible ")    

# age= int(input("enter your age"))
# if age>=18:
#     print("your an adult")
# else:
#     print("your a minor")                                                                                                                                                                                                                      


# num1=int(input("enter your number"))
# if num1==0:
#     print("zero")
# elif num1<=0:
#     print("negative") 
# else:
#     print("positive")       


# a=int(input("enter your number:"))
# b=int(input("enter your number:"))
# if a>b:
#     print(a)
# else:
#     print(b) 
# a=6
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# char1=(input("enter:")).lower()
# if char1 in "a,e,i,o,u":
#     print("vowel")
# else:
#     print("constant")    

# num1=25
# if num1%5==0:
#     print("divisible by 5")
# else:
#     print("nt divisible") 
# week1=input("enter the day").lower()
# if week1 == "saturday" or week1=="sunday":
#     print("its a weekend")
# else:
#     print("its a weekday")    

# pass1=input("enter your password:")
# if pass1==("python@123"):
#     print("login succesfull")
# else:
#     print("retry")    

# year1=2024
# if year1%4==0 and year1%100!=0:
#     print("its a leap year")
# else:
#     print("not a leap year")
# n1=int(input("enter your numb1:"))   
# n2=int(input("enter your numb2:"))  
# n3=int(input("enter your numb3:"))  
# if n1>=n2 and n1>=n3: 
#     print(n1)
# elif n2>=n1 and n2>=n3:
#     print(n2)
# else:
#     print(n3)  
# day1=input("enter your num").lower()
# if day1==1:
#     print("1.monday")
# elif day1==2:
#     print("2.tuesday")
# elif day1==3:
#     print("3.wednesday")    
# elif day1==4:
#     print("4.thursday") 
# elif day1==5:
#     print("5.friday")
# elif day1==6:
#     print("6.saturday")

# elif day1==7:
#     print("7.sunday")
    
#  else:
#     print("invalid number")    


# score=int(input("enter yr num:"))
# if score>=90:
#     print("GRADE A")
# elif score>89:
#     print("GRADE B")
# elif score>79:
#     print("GRADE C")
# else:
#     if score>69 or score<=40:
#         print("GRADE D")


# s1=int(input("enter s1"))
# s2=int(input("enter s2"))
# s3=int(input("enter s3"))
# if (s1+s2>s3)and(s1+s3>s2) and (s2+s3>s1):
#     print("a triangle can b formed")
# else:
#     print("a triangle is not formed")   

# def positive_or_negative(n):
#     if n>0:
#         print("positive")
#     elif n==0:
#         print("zero")
#     else:
#         if n<0:
#             print("negative")

# positive_or_negative(3)


# def even_or_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")  
# even_or_odd(6)
 
# def print_highest_of_3_numbers(n1,n2,n3):
#     if n1>=n2 and n1>=n3:
#         print(n1)
#     elif n2>=n1 and n2>=n3 :
#         print(n2)
#     else:
#         if n3>=n1 and n3>n2:
#             print(n3) 


# n1=input("enter your n1")
# n2=input("enter your n2")
# n3=input("enter your n3") 

# print_highest_of_3_numbers(n1,n2,n3)

# def print_leap_year(n):
#      if n%4==0 and n%100!=0:
#           print("its a leap yr")
#      else:
#           print("its nt a leap yr")

# print_leap_year(2024)          

# char1=input("enter:").lower()
# if char1 in "a,e,i,o,u":
#     print("vowel")
# else:
#     print("consonant")


# def class_grades(n):
#  if n>=90:
#     print("GRADE A")
#  elif n>=89:
#    print("GRADE B")
#  elif n>=79:
#    print("GRADE C")
#  elif n>=69 and n>=40:
#    print("GRADE D") 
# n=int(input("enter your marks"))
# class_grades(n) 
def sides_of_a_triangle(s1,s2,s3):
    if (s1>s2+s3) and (s1+s2>s3) and (s1+s3>s2):
        print("triangle is formed")
    else:
        print("triangle cant be formed")
s1=int(input("enter yr s1"))
s2=int(input("enter your s2"))
s3=int(input("enter your s3"))

sides_of_a_triangle(s1,s2,s3)










 









  