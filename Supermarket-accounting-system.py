#the first style
x,w,y=[],[],[]
num=int(input("enter the number of cashers:"))
for i in range(num):
    x.append(0)
    w.append(input(f"enter the name of casher{i+1}:"))
    y.append(input(f"enter the ID of cAasher{i+1}:"))
while True:
    castmer=input("enter the name of castemer:")
    enter=input("If you want a report enter(report) or choos one of cashers:")
    if enter=="report":
        break
    amount=int(input("how much you bouth:"))
    x[int(enter)-1]+=amount
for k in range(len(x)):
    print(f"the name of casher{k+1}:{w[k]}\nthe ID of casher{k+1}:{y[k]}\nthe total income={x[k]} ")
    print("___________________________________________________________")

#the secound style
x=[]
num_cashier=int(input("enter the number of cashiers:"))
products=int(input("enter the number of types of products that are in the supermarket :"))
for j in range(num_cashier):
    name=input(f"enter the name of cashier {j+1}:")
    id=input(f"enter the ID of cashier {j+1}:")
    total=0
    for i in range(products):
        name_products=input("enter the name of product:")
        unit_price=int(input("enter the unit price"))
        num=int(input("How many of them did you sell?"))
        total+=unit_price*num
    x.append(["the name of cashier:",name,"\nthe ID of cashier:",id,"\nthe total income=",total])
for k in range(len(x)):
    print("")
    for r in range(6):
        print(x[k][r],end="")
    print("\n________________________________________________________",end="")
