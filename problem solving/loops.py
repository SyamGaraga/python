# for i in range(1,101):
#     print(i,end=' ')


# n=1
# while(n<=50):
#     if n%2==0:
#         print(n,end=' ')
#     n+=1
        
# n=int(input())
# for i in range(n):
#     a=(n*(n+1))/2
# print(int(a)) 




# n=int(input())
# while n>0:
#     n=int(int(input()))
#     if n<0:
#         break




# for i in range(1,21):
#     print(3,"x",i,"=",i*3)
# for i in range(0,101,3):
#     print(3,'x',int(i/3),'=',i)



# sum=0
# n=int(input("enter n value:"))
# for i in range(n+1):
#     sum+=i
# print(sum)



   

# n1=int(input())
# count=0
# for i in range(1,n1+1):
#     if n1%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")
    

# n1=int(input())
# n2=int(input())
# for i in range(n1,n2+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print("prime")
#     else:
#         print("not a prime")

# n=int(input())
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
#         n+=1
# if count==2:
#     print(n)        
    

# n1=int(input())
# while True:
#     n1+=1
#     count=0
#     for i in range(1,n1+1):
#         if n1%i==0:
#             count+=1
#     if count==2:
#         print(n1)
#         break
  

# n1=int(input())
# while True:
#     if n1 in [0,1,2]:
#         print("not exists")
#         break
#     n1-=1
#     count=0
#     for i in range(1,n1+1):
#         if n1%i==0:
#             count+=1
#     if count==2:
#         print(n1)
#         break 


# n1=int(input())
# while True:
#     n1+=1
#     count=0
#     for i in range(1,n1+1):
#         if n1%i==0:
#             count+=1
#     if count==2:
#         print(n1)
#         max_num=n1
#         break
# n1=int(input())
# while True:
#     if n1 in [0,1,2]:
#         print("not exists")
#         break
#     n1-=1
#     count=0
#     for i in range(1,n1+1):
#         if n1%i==0:
#             count+=1
#     if count==2:
#         print(n1)
#         min_num=n1
#         break 
# m1=max_num-n1
# m2=n1-min_num
# if m1>m2:
#     print(min_num,"is nearer prime number")    
# else:
#     print(max_num,"is nearer prime number")






# year=int(input())
# while True:
#     year+=1
#     if (year%4==0 and year%100!=0) or year%400==0:
#         print(year)
#         break;      


# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")


#factorial
# n=int(input())
# fact=1
# i=1
# while i<n:
#     fact=fact*i
#     i+=1
# print(fact)