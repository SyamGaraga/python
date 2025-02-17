# li=[1,2,3,4,5]
# max_num=li[0]
# min_num=li[0]
# sum=0
# for i in range(0,len(li)):
#     if li[i]>max_num:
#         max_num=li[i]
#     if li[i]<min_num:
#         min_num=li[i]
#     sum+=li[i]    
# print(max_num)
# print(min_num)
# print(sum)


# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)



# def fun(a, b):
#     return a + b,a*b,a-b,a/b,a//b,a**b
# result = fun(5, 2)
# print(result)



# ramesh=int(input())
# suresh=int(input())
# naresh=int(input())
# if (ramesh<suresh) and (ramesh<naresh):
#     print("ramesh is younger")
# elif (suresh<ramesh) and (suresh<naresh):
#     print("suresh if younger")
# elif (ramesh==suresh==naresh):
#     print("equal age")
# elif (ramesh==suresh) and naresh>ramesh and naresh>suresh:
#     print("ramesh,suresh are youngers")
# elif (ramesh==naresh) and suresh>ramesh and suresh>naresh:
#     print("ramesh,naresh are younger")   
# elif(suresh==naresh) and ramesh>suresh and ramesh>naresh:
#     print("suresh,naresh are youngers")
# else:
#     print("naresh is younger")



# a=int(input())
# b=int(input())
# c=int(input())
# str1='a is younger' if a<b and a<c else 'b is younger' if b<a and b<c else 'c is younger'
# print(str1)



# for i in range(1,101):
#     print(i,end='')

leap year
# n=int(input())
# str='Leap year' if (n%100!=0 and n%4==0) or n%400==0 else 'not a leap year'
# print(str)


forms a triangle or not
# a,b,c=map(int,input().split(','))
# # if a+b>c or a+c>b or b+c>a:
# #     print("Forms a triangle")
# # else:
# #     print("not a triangle")
# str='forms a triangle' if a+b>c or a+c>b or b+c>a else 'not a triangle1'
# print(str)

vowels or consonants
# str=(input("enter a character="))
# if str in ['a','e','i','o','u']:
#     print("vowels")
# elif str=int:
#     print("consonant")


# str=(input("enter a character="))
# if len(str)>1 or len(str)==0:
#     print("dont run the code")
# else:
#     if str in 'aeiou':
#         print("vowles")
#     elif str.isalpha():
#         print("consonant")
#     else:
#         print("neither")


# n=input("enter input:").lower()
# a=float(input())  
# b=float(input())
# if n=='add':
#     print(a+b)
# elif n=='sub':
#     print(a-b)
# elif n=='div':
#     str='ZeroDivisionError' if b==0 else a/b
#     print(str)
# elif n=='mul':
#     print(a*b)
# else:
#     print("error")    



