print("starting line")
a=[11,22,33,66,89,45]
print(a)
print(a[5])
try:
    a=10/0
except:
     print("some exception raised")
else:
    print("no exception raised,everything worked perfectly")
finally:
        print("this is final block")
print("output try block")
