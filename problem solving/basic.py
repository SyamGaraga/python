# positive or not
n=int(input())
if n==0:
    print("Zero")
elif n>0:
    print("positive")
else:
    print("negative")

#odd or even
n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")

#Eligible to vote
n=int(input())
if n>=18:
    print("Eligible to vote")
else:
    print("not Eligible")

#greatest of two numbers
n,m=map(int,input().split(','))
if n>m:
    print("n is greater")
elif n==m:
    print("equal")
else:
    print("m is greater")   

#pass or fail
n=int(input())
if n>40:
    print("pass1")
else:
    print("Fail")     

#finding a day in a week
n=int(input())
if(n==1):
    print("monday")
elif n==2 :
    print("Tuesday")
elif n==3:
    print("wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("friday")
elif n==6:
    print("saturday")
else:
    print("sunday")   


 #finding a month in a year
n=int(input())
if(n==1):
    print("Jan")
elif n==2 :
    print("Feb")
elif n==3:
    print("Mar")
elif n==4:
    print("Apl")
elif n==5:
    print("May")
elif n==6:
    print("June")
elif n==7:
    print("July")
elif n==8:
    print("Aug")
elif n==9:
    print("Sept")
elif n==10:
    print("Oct")
elif n==11:
    print("Nov")
elif n==12:
    print("Dec")
else:
    print("wrong Number")

 #calculator
n=input().lower 
a=float(input())  
b=float(input())
if n=='add' :
    print(a+b)
elif n=='sub':
    print(a-b)
elif n=='div':
    str='ZeroDivisionError' if b==0 else a/b
    print(str)
elif n=='mul':
    print(a*b)
else:
    print("error")


#medium
#greatest of three
a,b,c=map(int,input().split())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


#grades of thge students
n=int(input())
if n>=90 and n<=100:
    print("A Grade")
elif n>=80 and n<=89:
    print("B Grade")
elif n>=70 and n<=79:
    print("C Grade")
else:
    print("Fail")

  