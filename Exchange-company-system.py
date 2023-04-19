total_deposit=total_withdrawal=total_exchange=0
x=[]
branches=int(input("enter the number of branchs:"))
for i in range(branches):
    deposit=withdrawal=exchange=0
    NumOperation=int(input(f"enter the number of operations in branch{i+1}:"))
    for j in range(NumOperation):
        operation=input("enter the kind of operation:")
        money=int(input("How mach you want to deposit or withdrawal or exchange?"))
        if operation=="deposit":
            deposit+= money
        elif operation=="withdrawal" :
            withdrawal+=money
        else:
            exchange+=money
    total_deposit+=deposit
    total_withdrawal+=withdrawal
    total_exchange+=exchange
    x.append(["deposit=",deposit,"  ,withdrawal=",withdrawal,"  ,exchange=",exchange])
for k in range(len(x)):
    print("")
    print(f"branch{k+1}:")
    for w in range(6):
        print(x[k][w],end="")
print(f"\nthe total of deposit operations for all branches={total_deposit}")
print(f"the total of withdrawa operations for all branches={total_withdrawal}")
print(f"the total of exchange operations for all branches={total_exchange}")
