# def min_max_sum(list1):
#     min1=min(list1)
#     max1=max(list1)
#     sum=min1+max1
#     return sum
# print(min_max_sum([1,3,2,-1,4]))

# def find(list1):
#     num=int(input())
#     for i in list1:
#         if i==num:
#             return True
#     return False
# print(find([1,2,3,4]))


# def find(list1):
#     num=int(input())
#     for i in list1:
#         if i==num:
#             return list1[i-2]
#     return False
# print(find([1,2,3,4,7,9,8]))

# def find_k(list1,num):
#     for i in range(len(list1)):
#         if num in list1:
#             return True
#     return False
# print(find_k([1,2,3,4,5],6))

# def dup(list1,num):
#     list2=[]
#     list3=[]
#     for i in range(len(list1)):
#         if num in list1:
#             list2+=num
#         else:
#             list3+=num
# print(dup([1,2,3,4,5],5))


# def missing(list):
#     n=[]
#     for i in range(len(list)):
#         if list[i+1]-list[i]==1:
#             i+=1
#         else:
#             n.append(i+1)
#             break
# print(n)

# def reverse_num(list1):
#     low=0
#     high=len(list1)-1
#     while low<high:
#         list1[low],list1[high]=list1[high],list1[low]
#         low+=1
#         high-=1
#     return list1
# print(reverse_num([1,2,3,4,5]))

num=[1,2,3,3,3,3,4,4,5,6,7,5,6,7]
dup=[]
unique=[]
num.sort()
for i in range(len(num)-1):
    if num[i]==num[i+1]:
        dup.append(num[i])
for i in num:
    if i not in dup :
        unique.append(i)
print(dup)
print(unique)


