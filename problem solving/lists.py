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

# num=[1,2,3,3,3,3,4,4,5,6,7,5,6,7]
# dup=[]
# unique=[]
# num.sort()
# for i in range(len(num)-1):
#     if num[i]==num[i+1]:
#         dup.append(num[i])
# for i in num:
#     if i not in dup :
#         unique.append(i)
# print(dup)
# print(unique)

# # sum of elements in a list
# def list_stats(list1):
#     total_sum=sum(list1)
#     return total_sum

# list1=[5,19,10,3,15]
# total_sum=list_stats(list1)

# print("sum of numbers:",total_sum)

# # search element in a list

# def search_element(list2,search_num):
#     for i in list2:
#         if i == search_num:
#             return True
#     return False

# list2=[11,22,33,44,55,66]
# search_num=int(input("enter a number"))

# if search_element(list2,search_num):
#     print("found")
# else:
#     print("not found")

# # 12 largest and smallest in a list
# def max_min(list3):
#     largest=max(list3)
#     smallest=min(list3)
#     return largest, smallest

# list3=[1,22,45,68,1001]
# # maximum=max_min(list3)
# largest, smallest =max_min(list3)

# print("Smallest number is:",smallest)
# print("Largest  numbers is :",largest)

# # unique and duplicate

# duplicates = set()
# unique = set()

# list4 = [1,1,1,1,2,2,2,2,3,3,3,3,4,5,6,7,8,9,9,9,9]
# for i in list4:
#     if i in unique:
#         duplicates.add(i)
#         unique.remove(i)
#     elif i not in duplicates:
#         unique.add(i)

# print(duplicates)
# print(unique)

# # 4
# def find_duplicates(number):
#     list4 = [int(digit) for digit in str(number)] 
#     duplicates = set()
#     unique = set()

#     for i in list4:
#         if i in unique:
#             duplicates.add(i)
#             unique.remove(i)  
#         elif i not in duplicates:
#             unique.add(i) 

   
#     if len(duplicates) == 1:
#         print(f"Duplicate is :",duplicates)
#     elif len(duplicates) > 1:
#         print("Duplicates are:",duplicates)
#     else:
#         print("No duplicates found")

#     print("Unique digits are:",unique)


# find_duplicates(1214)

# # 5
# str1=input("enter the string")

# res={}
# for k in str1:
#     if k in res:
#         res[k] +=1
#     else:
#         res[k] =1

# print(res)

# # 6
# def duplicate_digit_exists(num1):
#     curr_list  = []
#     while num1 > 0:
#         rem  = num1 % 10
        
#         if rem in curr_list:
#             return True
#         curr_list.append(rem)
#         num1  = num1 // 10
#     return False

# list2  = [202,89,112,99]
# res  = []
# for i in list2:
#     # res.append(duplicate_digit_exists(i))
#     temp  = duplicate_digit_exists(i)
#     res.append(temp)

# print(res)

# # 7

# def sum_of_digits(num1):
#     digits_sum = 0
#     while num1 > 0:
#         rem = num1 % 10
#         digits_sum += rem
#         num1 = num1 // 10
#     return digits_sum

# list5 = [202,89,112,88]
# res = []

# for i in list5:
#     temp = sum_of_digits(i)
#     res.append(temp)
# print(res)

# # # 8
# # def digits_in_increasing_order(num1):
# #     last_digit = -1
# #     while num1>0:
# #         rem = num1 % 10
# #         if rem <= last_digit:
# #             return False
# #         last_digit = rem
# #         num1 = num1 // 10
# #     return True

# # list6 = [568,89,112,88,571]
# # res = []

# # for i in list6:
# #     temp = digits_in_increasing_order(i)
# #     res.append(temp)

# # print(res)

# # 11 missing numbers
# def missing_number(num1):

#     remainder = []
#     str1 = ""
#     while num1 > 0:
#         rem = num1 % 10
#         remainder.append(rem)
#         num1 = num1 // 10

#     for i in range(1, max(remainder)):
#         if i not in remainder:
#             str1 += str(i)
#     return str1 + " missing "


# # Finding the frequency of elements in an array.
# #     arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2
# arr = [10, 30, 10, 20, 10, 20, 30, 10]
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# for key, value in freq.items():
#     print(f"{key} => {value}")


# # 19) check if array is subset of another array or not .if the arr2 contains elements which are there in arr1 then it is a subset of an array.
# def is_subset(arr1, arr2):
#     for element in arr2:
#         if element not in arr1:
#             return False
#     return True
# arr1 = [1, 3, 4, 5, 2]
# arr2 = [2, 4, 3, 1, 7, 5, 15]
# if is_subset(arr1, arr2):
#     print("arr2 is a subset of arr1")
# else:
#     print("arr2 is NOT a subset of arr1")


# # Wap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not
# #  Input: [568,89,112,88,571]     Output: [true,true ,false,false ,false]
# def is_increasing(num):
#     num_str = str(num)  
#     for i in range(len(num_str) - 1):
#         if num_str[i] > num_str[i + 1]:  
#             return False
#     return True
# def check_numbers(lst):
#     return [is_increasing(num) for num in lst]  
# numbers = [568, 89, 112, 88, 571]
# result = check_numbers(numbers)
# print(result)

# def large_short(list):
#     list.sort()
#     max=list[-1]
#     min=list[0]
#     return max,min
# print(large_short([2,1,6,3,7]))


# def large_short(list):
#     list.sort()
#     second_max=list[-2]
#     third_max=list[-3]
#     return second_max,third_max
# print(large_short([2,1,6,3,7]))


# def large_short(list):
#     list.sort()
#     second_min=list[1]
#     third_min=list[2]
#     return second_min,third_min
# print(large_short([2,1,6,3,7]))

# def sort(list):
#     list1=sorted(list)
#     return list,list1
# print(sort([20,15,26,2,98,6]))

# list=[20,15,26,2,98,6]
# list1=sorted(list)
# res=[]
# for i in list:
#     res.append(list1.index(i)+1)
# print(res)    


# def sort(list):
#     list1=sorted(list)
#     res=[]
#     for i in list:
#         res.append(list1.index(i)+1)
#     return res
# print(sort([20,15,26,2,98,6]))


# def sort(list):
#     list1=sorted(list)
#     res=[]
#     for i in list:
#         res.append(len(list)-list1.index(i))
#     return res
# print(sort([20,15,26,2,98,6]))


# def sort1(list1):
#     list1.sort()
#     low=int((len(list1)-1)/2)+1
#     high=len(list1)-1
#     while low<high:
#         list1[low],list1[high]=list1[high],list1[low]
#         low+=1
#         high-=1
#         return list1
# print(sort1([8,7,1,6,5,9,10])) #1,5,6,7,8,9,10


# list1=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in list1:
#     for j in  i:
#         sum+=j
# print(sum)


# list1=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in range(list1):
#     for j in range(len(list1)):
#         if i==0 or i==len(list1)-1:
#             sum+=list

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]        
sum1= m[0][0]+m[0][2]+m[1][1]+m[2][0]+m[2][2] 
print(sum1) 



