theo_marks = [ ]
n = int(input("Enter the theory exam marks : "))
for i in range(0,n):
    ele = int(input())
    theo_marks.append(ele)
'''int(a)=str(input("Enter the theory exam marks :")).split(",")
theo_marks.append(a)'''
int_marks = [ ]
n2 = int(input("Enter the internal exam marks : "))
for i in range(0,n2):
    ele1 = int(input())
    int_marks.append(ele1)
'''b=str(input("Enter a internal exam marks:")).split(",")
int_marks.append(int(b))'''
prac_marks = [ ]
n3 = int(input("Enter the practical exam marks  : "))
for i in range(0,n3):
    ele2 = int(input())
    prac_marks.append(ele2)
'''c=str(input("Enter the practical exam marks  :")).split(",")
prac_marks.append(int(c))'''
def combine_marks(tl,il):
    global comb_marks
    comb_marks=[]
    for i in range(len(tl)):
        j=tl[i]+il[i]
        comb_marks.append(j)
def grade_distubuter(l):
    global grade_l1
    grade_l1=[]
    for i in l:
        if i<40:
            print("you Fail Try again in next sem :)  ")
            break
        else:
            if 40<=i<=45:
                grade_l1.append("D")
            elif 45<=i<=50:
                grade_l1.append("C")
            elif 50<=i<=55:
                grade_l1.append("B")
            elif 55<=i<=60:
                grade_l1.append("B+")
            elif 60<=i<=70:
                grade_l1.append("A")
            elif 70<=i<=80:
                grade_l1.append("A+")
            elif 80<=i:
                grade_l1.append("O")
    
def prac_grade(l):
    global practical_grade
    practical_grade=[]
    for i in l:
        if i<5:
            print("bruh you failed in prcaticals shame!")
            break
        else:
            if 5<=i<=10:
                practical_grade.append("D")
            elif 10<=i<=20:
                practical_grade.append("C")
            elif 20<=i<=30:
                practical_grade.append("B")
            elif 30<=i<=40:
                practical_grade.append("A")
            elif 40<=i:
                practical_grade.append("O")
   
def final(thg):
    global thry_list
    thry_list=[]
    for i in thg:
        if i =='O':
           thry_list.append(10*2) 
        elif i=='A+':
            thry_list.append(9*2)
        elif i=='A':
            thry_list.append(8*2) 
        elif i=='B+':
            thry_list.append(7*2) 
        elif i=='B':
            thry_list.append(6*2) 
        elif i=='C':
            thry_list.append(5*2)
        elif i=='D':
            thry_list.append(4*2)  

def pgfinal(pg):
    global prc_list 
    prc_list=[]
    for i in pg:
        if i =='O':
            prc_list.append(10*2)
        elif i=='A':
            prc_list.append(9*2)
        elif i=='B':
            prc_list.append(8*2)
        elif i=='C':
            prc_list.append(7*2)
        elif i=='D':
            prc_list.append(6*2)


def addli(tll,pll):
    last_list=tll+pll
    sgpi=sum(last_list)/20
    print("you SGPI is ",float(sgpi),"theory grade of respective subjects: ",grade_l1,"Practical grade of respective subjects:",practical_grade)


combine_marks(theo_marks,int_marks)
grade_distubuter(comb_marks)
prac_grade(prac_marks)
final(grade_l1)
pgfinal(grade_l1)
print(addli(thry_list,prc_list))


