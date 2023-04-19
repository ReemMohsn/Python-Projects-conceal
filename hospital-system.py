a=0
b=0
c=0
a1=0
b1=0
c1=0
nums_pat=int(input("enter the number of patient the came in the mont:"))
for patient in range(nums_pat):
    a=input("enter the name of patient:")
    x=input("enter the kind of room  a or b or c he stayed in it:")
    while x!="a" or x!="b" or x!="c":
        x = input(" try again,the kind of room  a or b or c he stayed in it:")
    w=int(input("How many days he stayed in room:"))
    if x=="a":
        if w>=5 and w<=10:
            a1+=(w*50)-((w*50)*(5/100))
        elif w>10:
            a1+=(w*50)-((w*50)*(15/100))
        a+=w
    elif x=="b":
        if w>=5 and w<=10:
            b1+=(w*30)-((w*30)*(5/100))
        elif w>10:
            b1+=(w*30)-((w*30)*(15/100))
        b+=w
    else:
        if w>=5 and w<=10:
            c1+=(w*10)-((w*10)*(5/100))
        elif w>10:
            c1+=(w*10)-((w*10)*(15/100))
        c+=w
print("the total befor antagonist {}".format(a*50+b*30+c*10) )
print("a={}".format(a*50))
print("b={}".format(b*30))
print("c={}".format(c*10))

if (a1+b1+c1)<(a*50+b*30+c*10):
    print("the total after antagonist {}".format(a1+b1+c1))
else:
    print("there is no antagonist then the total is {}".format(a*50+b*30+c*10))
print("the total of antagonist is {}".format((a*50+b*30+c*10)-(a1+b1+c1)))