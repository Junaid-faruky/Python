login(name,password)
class loginandreg:
    def reg(self):
        username=input("Enter the employee ID:")
        password=input("Enter password:")
        phonenumber=input("Enter phone number:")
        email=input("enter Email ID:")
        print("Registration success")
        self.data.append(username)
        self.data.append(password)
    def login(self):
        l_username=input("Enter username")
        l_pwd=input("enter login password")
        if l_username in self.data and l_pwd in self.data:
            print("Login success")
        else:
            print("Invalid")
obj = loginandreg

while True:
    print("1.Register,2.login")
    choice=int(input("Enter your choice"))
    
    if choice==1:
        obj.Reg()
    elif choice==2:
        obj.login()

from abc import ABc,abstractmethod
class bank:
    @abstractmethod
    def desposit(self):
        pass
    @abstractmethod
    def withdrawl(self):
        pass
    @abstractmethod
    def checkbalance(self):
        pass
class SBI(bank):
    balance=0
    def _init_(self,amount):
        self.balance+=amount
    def deposit(self,amount)
        self.balance-=amount
    def checkBal(self):
        return self.balance
s=SBI(500)
s.deposit(500)
print(s.checkBal())
s.withdrawl(500)
print(s.checkBal())


