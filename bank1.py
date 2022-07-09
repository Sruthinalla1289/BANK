class Account:
    def __init__(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        print(a)
        print(b)
        print(c)
        print(e)
    def display(self):
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
    def update(self,f,g,h,i):
        self.f=f
        self.g=g
        self.h=h
        self.i=i
    def __del__(self):
        print("deleted")
l=[]
a=["55,65,80,88,76"]
b=["sruthi,sravani,prathima,naveen,murthy"]
c=["saving,deposit,salary,deposit,saving"]
while(1):
    print("enter 1 to insert Bank details:")
    print("enter 2 to display Bank details:")
    print("enter 3 to update Bank details:")
    print("enter 4 to delete the Bank details:")
    print("enter 5 to exit")
    x=int(input())
    if x==1:
        a=int(input("enter Bank account number to be inserted:"))
        b=input("enter Account name:")
        c=input("enter Account type:")
        d=input("enter deposit amount:")
        e=input("enter withdraw amount:")
        acc=Account(a,b,c,d,e)
        l.append(acc)
        print(l)
    if x==2:
        print(a)
        print(b)
        print(c)
            
    if x==3:
        a=int(input("enter the account number to update the details:"))
        b=input("enter Account name:")
        c=input("enter Account type:")
        d=input("enter deposit amount to be update in balance:")
        e=input("enter balance amount")
        c1=1
        for obj in l:
            if c1!=a:
                c1=c1+1
            else:
                l.pop(a-1)
                del obj
        acc=Account(a,b,c,d,e)
        l.insert(a-1,acc)
    if x==4:
        c=1
        e=int(input("enter the withdraw amount:"))
        a=int(input("enter the account number to delete the details:"))
        for obj in l:
            if c!=a:
                c=c+1
            else:
                l.pop(a-1)
                del obj
                break
    if x==5:
        break
    print(l)