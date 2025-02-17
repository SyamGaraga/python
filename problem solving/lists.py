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


def find(list1):
    num=int(input())
    for i in list1:
        if i==num:
            return list1[i-2]
    return False
print(find([1,2,3,4,7,9,8]))