def twoSum(numbers, target):
    arrLen = len(numbers);
    
    for i in range(0, arrLen):
        for j in range(i+1, arrLen):
            if(numbers[i] + numbers[j] == target):
                return [numbers[i], numbers[j]]
            
    return []
            

print(twoSum([2, 7, 11, 15],9))
print(twoSum([3,2,4],6))

