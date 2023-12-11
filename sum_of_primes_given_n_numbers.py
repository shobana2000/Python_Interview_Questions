#
# def is_prime(n):
#     if n<=1:
#         return False
#     if n<=3:
#         return True
#     if n%2==0 or n%3==0:
#         return False
#     i=5
#     while i*i<=n:
#         if n%i==0 or n%(i+1)==0:
#             return False
#     return True
#
# def primedigits(n):
#
#     prime=0
#
#     while n>0:
#         digits=n%10
#         if is_prime(digits):
#             prime+=digits
#         n//=10
#     return prime
# N = int(input("Enter a number: "))
#
# result = primedigits(30)
# print(result)

# input_str=(input("Enter A input string to get reversed: "))
# # result=''.join(reversed(input_str))
# result=input_str[::-1]
# print(result)

# input=input("Enter a palindfrome string: ")
# input=input.lower().replace(" ","")
# print(input==input[::-1])

# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n+1):
#         # print(i)
#         value=fib[i-1]+fib[i-2]
#         fib.append(value)
#         # fib.append(fib[i-1]+fib[i-2])
#     return fib
#
# input=10
# fibo=fibonacci(input)
# print(fibo)

# def is_prime(n):
#     if n<=1:
#         return False
#
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def find_primes(limit):
#     primes = []
#     for num in range(2, limit + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes
#
# # Test case
# print(find_primes(30))

# def two_sum(nums,target):
#     num_to_index={}
#     for i,num in enumerate(nums):
#         complement=target-num
#         if complement in num_to_index:
#             return [num_to_index[complement], i]
#         print(i,num)
#         num_to_index[num]=i
#     return None
# input_nums=[2,7,11,15]
# target=9
# print(two_sum(input_nums,target))

# def replace_with_greatest_on_right(arr):
#     n = len(arr)
#     max_right = arr[n - 1]
#     arr[n - 1] = -1  # The rightmost element will always be replaced with -1
#
#     for i in range(n - 2, -1, -1):
#         temp = arr[i]
#         arr[i] = max_right
#         max_right = max(max_right, temp)
#
#     return arr
#
# # Example usage
# input_array = [17, 18, 5, 4, 6, 1]
# result_array = replace_with_greatest_on_right(input_array)
# print(result_array)


# def alternateSort(arr, n):
#     arr.sort()
#     i=0
#     j=n-1
#     for i in range(n-2,-1,-1):
#         print(arr[j],end=" ")
#         j-=1
#         print(arr[i],end=" ")
#         i+=1
#     if (n%2!=0):
#         print(arr[i])
#
# arr = [1, 12, 4, 6, 7, 10]
# n=len(arr)
# alternateSort(arr, n)

# import re
# input_string = "(((abc)((de))"
# result=re.sub(r'[^()]*\((?:[^()]*\)|[^()]*)*|[^()]*\)(?:[^()]*\(|[^()]*)*',r'',input_string,0)
# print(result)  # Output: "((abc)(de))"

# array1 = [1, 2, 3, 6, 9]
# array2 = [2, 4, 5, 10]
# merged = sorted(set(array1 + array2))
# print(merged)

# from collections import Counter
# arr=[2,1,3,2,2,5,8,9,8]
# count=Counter(arr)
# print(count)
# for num, count in count.items():
#     print (f"{num}-{count}")

# import re
#
# text = "abcd"
# pattern = "a*cd"
#
# if re.search(pattern.replace('\\', r'\\').replace('*', r'.*'), text):
#     print("Pattern matches a substring in the first string.")
# else:
#     print("Pattern does not match any substring in the first string.")

# fib=10
# fib1=[0,1]
# for i in range(2,fib+1):
#     fib1.append(fib1[0-1]+fib1[i-2])
# print(fib1)

# pal="racecars"
# s=pal.lower()
# s=''.join(filter(str.isalnum,s))
# print(s==s[::-1])

# strs = ["svunfslower", "sunflour", "vunflight"]
# strs.sort()
# first_str = strs[0]
# last_str = strs[-1]
# common_prefix = []
# for i in range(len(first_str)):
#     if i<len(last_str) and first_str[i]==last_str[i]:
#         common_prefix.append(first_str[i])
#     else:
#         break
# print(''.join(common_prefix))

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result=[]
#
# while matrix:
#     result+=matrix.pop(0)
#
#     if matrix and matrix[0]:
#         for row in matrix:
#             result.append(row.pop())
#     if matrix:
#         result+=matrix.pop()[::-1]
#
#     if matrix and matrix[0]:
#         for row in matrix[::-1]:
#             result.append(row.pop(0))

# string="the sky is ths blue"
# str=string.split()
# reverse=list(reversed(str))
# rev=" ".join(str[::-1])
# rev=" ".join(reverse)
# print(rev)

# numbers=[0,1,2,8]
# n=len(numbers)
# # print(n*5//2)
# total=(n*(n+1))//2
# actual=sum(numbers)
# print(actual)
# tot=total-actual
# print(tot)

from collections import Counter
input_array = [2, 1, 3, 2, 2, 5, 8, 9, 8]
count=Counter(input_array)
for num,count in count.items():
    print(f"{num}-{count}")