x=[]
total=0
import datetime
date=datetime.date.today()
name=input("enter the name of costumer:")
discount=float(input("enter the discount value:"))
item=input("enter the item:")
while item!="finish":
    qty=int(input("enter the a qty"))
    unit_price=float(input("enter the price of  one item:"))
    amount=qty*unit_price
    x.append([item,"        ",qty,"        ",unit_price,"         ",amount])
    item = input("enter the item:")
    total+=amount

discount1=total-(total*discount)
print(f"date:{date}")
print(name)
print("item      qty      unit price       amount")
for j in range(len(x)):
    print("")
    for k in range(7):
         print(x[j][k],end="")
print("\n____________________________________________________________________________")
print(f"total={total}")
print(f"discount={discount}")
print(f"net total={discount1}")
