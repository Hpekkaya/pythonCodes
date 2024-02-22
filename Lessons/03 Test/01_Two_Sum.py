# nums = [2,7,11,15] 
# target = 9

# nums = [3,2,4] 
# target = 6

nums = [3,3] 
target = 6


# each number should not be used twice
# generate for loop
# generate check sum of two num whether equals to target or not if yes break the loop
# display the output

indic1=0
indic2 =0

for i in range(len(nums)-1):
        if (nums[i]+nums[i+1]) == target  :
            indic1=i
            indic2=i+1
            break

output =[indic1,indic2]

print(output)
    



