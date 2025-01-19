# Given an array of integers where every element appears even number of times except one element which appears odd number of times,
# write a program to find that odd occurring element in O(log n) time. The equal elements must appear in pairs in the array but there
# cannot be more than two consecutive occurrences of an element. 

# For example :

# 3 
# 2 3 2 
# It doesn't have equal elements appear in pairs 

# 7 
# 1 1 2 2 2 3 3 

# It contains three consecutive instances of an element. 

# 5 
# 2 2 3 1 1 

# It is valid and the odd occurring element present in it is 3. 
# Enter only valid inputs. 

# Sample Input : 

# 5 
# 2 2 3 1 1 

# Sample Output : 

# 3


# Code:

n = int(input())
data = input()
list1 = list(map(int, data.split()))

if list1[0] != list1[1]:
    print(list1[0])
elif list1[n-1] != list1[n-2]:
    print(list1[n])
else:
    left = 0
    right = n-1
    while left <= right:
        mid = ((right-left)//2)+left
        prev = mid-1
        nxt = mid+1
        if list1[prev]!=list1[mid] and list1[mid]!=list1[nxt]:
            print(list1[mid])
            break
        elif mid%2 == 0:
            if list1[prev] == list1[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if list1[prev] == list1[mid]:
                left = mid+1
            else:
                right = mid-1
                