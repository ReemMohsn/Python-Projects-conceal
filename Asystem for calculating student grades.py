fail=0
pass1=0
good=0
verygood=0
excellent=0
num_student=int(input("enter the number of student:"))
type_sub=input("enter the type of subject (2Hours or 3Hours): ")
if type_sub=="2Hours":
    for i in range(num_student):
        name=input("enter the name of student:")
        mid_term=float(input("enter the mark of mid_term:"))
        final=float(input("enter the mark of final:"))
        while 100<mid_term+final:
            mid_term = float(input("try again,the mark of mid_term="))
            final = float(input("try again,the mark of final="))
        if (mid_term+final)<=39:
            fail+=1
        elif 40<=(mid_term+final)<=59:
            pass1+=1
        elif 60 <= (mid_term + final) <= 79:
            good+=1
        elif 80<=(mid_term+final)<=89:
            verygood+=1
        else:
            excellent+=1
else:
    for i in range(num_student):
        name=input("enter the name of student:")
        mid_term=float(input("enter the mark of mid_term:"))
        final=float(input("enter the mark of final:"))
        practical = float(input("enter the mark of practical:"))
        while 150<mid_term+final+practical:
            id_term = float(input("try again,the mark of mid_term="))
            final = float(input("try again,the mark of final="))
            practical = float(input("try again,the mark of practical:"))
        if (mid_term+final+practical)<75:
            fail+=1
        elif 75<=(mid_term+final+practical)<=96:
            pass1+=1
        elif 97 <= (mid_term + final+practical) <= 119:
            good+=1
        elif 120<=(mid_term+final+practical)<=134:
            verygood+=1
        else:
            excellent+=1
print(f"the number of student in fail grade is {fail}")
print(f"the number of student in pass1 grade is {pass1}")
print(f"the number of student in good grade is {good}")
print(f"the number of student in verygood grade is {verygood}")
print(f"the number of student in excellent grade is {excellent}")
print("the percentage of student in fail grade is {}%".format(fail/num_student*100))
print("the percentage of student in pass grade is {}%".format(pass1/num_student*100))
print("the percentage of student in good grade is {}%".format(good/num_student*100))
print("the percentage of student in very good grade is {}%".format(verygood/num_student*100))
print("the percentage of student in excellent grade is {}%".format(excellent/num_student*100))