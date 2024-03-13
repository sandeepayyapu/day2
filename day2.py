a,b=c=7,8
print(a)
print(b)
print(c)

a=b, c=4,2
print(a,b)

temp=7
a=b #a=5
b=temp #b=7

# # a=5,b=7
#print(a,b)

#a=a=b #a=12
#b=a-b #b=a2-7=5
a=a-b #a=12-7
#print(a,b)

#a=a*b #a=35
#b=a/b #b=35/7=5.0
#a=a/b #a=35/5=7.0
print(int(a), int(b))

a=7
b=8
print(id(a))
print(id(b))

#....>keywords
#keywords are reservd=ed word which provides speical meaning to compiler or interpretor

import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
print(len(keyword.kwlist))

#....>To check if the string is keyword or not
print(keyword.iskeyword("break"))
print(keyword.iskeyword("fill"))

#if=8
#print(if) #error c0z if is a keyword

#!.....> literls
# Literl is the constant valu assigned to a variables
# A variable is consider to be constant when it is defines
# in caps

# a=58 #a is variable
# A=58 #A is constant

# hash()....> it creats as hash value for constant datatypes and
# provides error for non constant datatypes
n1=89+7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1))

#!.....operators
#? opertors are symbols which is used tpm perform various opertions
#? bewteen 2 or more operands

# ARITHMATIC
# Assignment
#logical
#Relational or comparison
#Bitwise
#Identity
#Membership
# todo......>Arithmatic...>+,-,*,%,//,**
# Eg;1
a=8
b=6
c=9
print(a+b+c)

#input()...>used to get the runtime input
#eval()...>used to get the runtime values all datatype

n1=int(input("Enter the value:"))
print(type(n1))

a=4
b=2
#print(a/b)# is used get the quotient valu
#print(a%d)# is used get the remainder valu

# !//..>fl devision
#a= 765433
#b=19
#print(a//b)#-> the outputwill be inn integer and the output will be
# based on floor valu

#! **-->used for power of number
print(2**4)#-->16


# ! Assignment-->+-=,-=,/=,//=,**=,&=,|=

a=10
a+=5
print(a)


a=30
a-=5
print(a) 

# ! compersion --> ==, >,< ,!=, <=,>=
a=8
b=7
print(a>b)

a=9
b=5
print(a==b)

# ! Bitwise operator--> &,|,^,~,<<,>>
a=7
b=4
print(a&b)


# Logical opertor
# and,or, not
a=6
print(a>3 and a<10)
print(a>8 and a<30)
print(not(a>8 and a<10))

#! Identity opertor
#? It is used to compare the memory location that the values
#? are stored


#is is not
a=10
a=20
print(a is b)
print(a==b)

#a =[1,2,3]
#b =[1,2,3]
#print(a is not b)

# ! Membership opertor
#in ,not in
# l1 =[7,8,9,,0,6,5]
# num = 55
# print(num in l1)
#print(num not in l1]

# num=678
# print(8 in numbe) # error

#! conditional statement

# eg:1
#a=6
# if a>3:
#   print(hello)

Eg; 3
# if 7>8

Eg:4
a=0
a=none
a=false
a=-""
# ifa:
print("yes")
#else:
print("No")

#a Number is even or odd
if n%2==0:
     print( "the number is even")  
else:
      print( "the number is odd")

     

    
 











































