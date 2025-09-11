# 10. Find Duplicate Elements in List
def find_duplicates(lst):
    seen, dupes = set(), set()
    for x in lst:
        if x in seen:
            dupes.add(x)
        seen.add(x)
    return list(dupes)

print(find_duplicates([1,2,3,4,2,3,5,6,3]))
