class A:
    def do_something(self):
        print("A's implementation")
        super().do_something() # This calls the next in the MRO, not necessarily the parent!

class B:
    def do_something(self):
        print("B's implementation")

class C(A, B):
    def do_something(self):
        print("C's implementation")
        super().do_something()

# Check the MRO
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

c = C()
c.do_something()
# Output:
# C's implementation
# A's implementation
# B's implementation (A's super() called B, its sibling in the MRO)
