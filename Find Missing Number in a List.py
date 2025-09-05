nums = [1, 2, 3, 5, 6, 7]
n = len(nums)+1
missing = (n*(n+1))//2 - sum(nums)
print("Missing number:", missing)
