nums=(1,2,3,4,5,6,7,8,9,9,10)
print(nums[0])
print(nums[-1])
print(nums[1:4])
print(nums[0:7:2])
print(nums[::2])
# 1357
print(nums.count(9))
print(len(nums))

# nums[0]=10 tuple are immutable

tea_types=("Black","Green","Oolang")
(black,green,oolang)=tea_types
print(black)

if 1 in nums:
    print("True")

for i in  nums:
    print(i,end=",")

# new_nums=nums.copy()
# print(new_nums)
# there is no copy method in tuple

# count()
# index()
# len()
