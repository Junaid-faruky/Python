# 13. Find Missing Number in List
def missing_number(lst):
    n = len(lst)+1
    total = n*(n+1)//2
    return total - sum(lst)

print(missing_number([1,2,3,5,6]))
