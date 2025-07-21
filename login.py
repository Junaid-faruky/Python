    password=input()

alpha_count=0 
special_count=0
numeric_count=0

for each_char in password:
    if('A'<= each_char and each_char<='Z') or (each_char >='a' and each_char >='z'):
        alpha_count=alpha_count+1
    elif(each_char>='0' and each_char<='9'):
         numeric_count=numeric_count+1
    else:
        special_count=special_count+1
if(alpha_count==5 and numeric_count==3 and special_count==1):
    print("Valid password")
else:
    print("Invalid password")

condition = True

while(condition):
    full_name = input()

    for each_char in full_name:
        if(each_char ==' '):
            condition =False
            
last_index = full_name.index(' ')
            
#bitme123
condition = True
digit = False
upper_letter = False
while(condition):
    password = input()
    len_password = len(password)
    for each_char in password:
        if(each_char.isupper()):
            digit = True
            break
        
 for each_char in password:
        if (each_char.isupper()):
            upper_letter = True
        break
    
    if(len_password >=8 and digit and upper_letter):
        print("first name is:",first_name)
        condition = False
rev_list=[]

fir i in range(n):
    rev_list=rev_list+[list_1[n-1-i]]

print(rev_list)

print(list_1.reverse())
print(list_1)
print(list_1[::-1])
#to join the list 1 with list 2
str_1="BITM 123"
list_1=list(str_1)

list_2=["junaid","python"]
str_2=','.join(list_2)
print(str_2)
str_3="Ballari Institute of technology and management"
list_3=str_3.split(' ')
print(list_3)
