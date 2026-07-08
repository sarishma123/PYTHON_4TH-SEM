# nums = [2, 4, 5, 3, 6]
# target = 9

# def twoSum(nums, target):
    
#     for i in range(len(nums)):
       
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# print(twoSum(nums, target))

num2=[2,4,5,3,2,40,95,85,4]
target=5
  
def twosum1(num2,target):
     for i in range(len(num2)):
         for j in range(len(num2)):
             if num2[i]+num2[j]==target:
                 return[i,j]
print(twosum1(num2,target))