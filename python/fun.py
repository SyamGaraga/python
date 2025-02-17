# def is_prime(n):
#     for i in range(2,n):
#         if n<=1:
#             return False
#         if n%i==0:
#             return "not a prime"
#         else:
#             return "prime"
# print(is_prime(11))


# def is_prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return "prime"
#     else:
#         return "not a prime"
# print(is_prime(6))        


# def is_Armstrong(n):
#     temp=n
#     res=0
#     while temp>0:
#         rem=temp%10
#         res+=rem**len(str(n))
#         temp=temp//10
#     return res==n
# print(is_Armstrong(10))

# def is_armstrong(n1,n2):
#     for i in range(n1,n2+1):
#         temp=i
#         res=0
#         while temp >0:
#             rem=temp%10
#             res+=rem**len(str(i))
#             temp=temp//10
#         if res==i:
#             return i 
# print(is_armstrong(1,100))


# for i in range(0,3):
#     while(i*2)>=3:
#         print("Debba adhurs kadhu")

# for i in range(1,11):
#     for j in range(1,31):
#         if i==5 or j<15:
#             break
#         print(i,j)
        
# n=[1,2,3,4,5,7]
# for i in range(len(n)):
#     if n[i+1]-n[i]==1:
#         i+=1
#     else:
#         print(n[i]+1)
#         break