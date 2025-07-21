def solveit2():
    print("this is line 123")
def solveit4():
    print("iam solveit 4")
    print("this is getting exected")
    solveit2()
def solveit():
    print("this is line 111")
    print("this is line 112")
    solveit4()
def sumoftwonumbers(num1,num2):
    solveit()
    result=num1+num2
    return result
num1=int(input())
num2=int(input())
result = sumoftwonumbers(num1,num2)
print(result)
