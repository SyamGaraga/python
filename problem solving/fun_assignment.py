# #sum 
# def sum(a,b):
#     return a+b
# print(sum(2,3))

# #min to second
# def con(a):
#     return a*60
# print(con(2))


# def str(a,b):
#     if a+b==10 or (a==10 or b==10):
#         return True
#     else:
#         return False
# print(str(1,1))


# def fun(str,str1):
#     if len(str)==len(str1):
#         return True
#     else:
#         return False
# # str="syam"
# # str1="syam1"
# print(fun("syam","syam1"))



# def large(num):
#     return(max(num))
# print(large([1,2,3]))


# def voWels(str):
#     Vowels='aeiou'
#     count=0
#     for char in str:
#         if char in Vowels:
#             count+=1
#     return count
# print(voWels('SYAMGARAGA'.lower()))

def fun(n):
    for i in range(n):
        i=i*2
    return i
print(fun(5))
