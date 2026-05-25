def isPrime(n):

    for i in range(1,n+1):

        if n%i == 0 and not (i == 1 or i == n):

            return False

    return True



# Get numbers
nums = input()
nums = nums.split()
nums = [int(n) for n in nums]

# Find first prime
i = 0
p1 = -1
while i < len(nums):

    if isPrime(nums[i]):
        p1 = nums[i]
        break

    else:
        i+=1

# Find 2nd prime
i+=1
p2 = -1
while i < len(nums):

    if isPrime(nums[i]):
        p2 = nums[i]
        break

    else:
        i+=1



# Solution
prod = p1*p2
print(prod)