operation1=[]
date1=[]
money1=[]
account_number=int(input("enter the account_number:"))
account_holder=input("enter the account_holder:")
balance=0
operation=input("enter the type of  operation deposit or widthrawal:")

while operation!="finish":
    operation1.append(operation)
    date=input("enter the date:")
    money=int(input("how mach you want to deposit or widthrawal?"))
    date1.append(date)
    money1.append(money)
    if operation=="deposit":
        balance+=money
    else:
        balance-=money
    operation = input("enter the type of  operation deposit or widthrawal:")
print("account_number=",account_number)
print("account_Holder=",account_holder)
print("date         amount          operation")
if len(operation1)<5:
    for j in range(-1,-(len(operation1)+1),-1):
        print(date1[j],"      ",money1[j],"      ",operation1[j])
else:
    for k in range(-1,-6,-1):
        print(date1[k], "      ", money1[k], "      ", operation1[k])
print("_______________________________________________________________")
if balance<0:
    print(f"balance={balance} ,so you have دين")
else:
    print(f"balance={balance}")