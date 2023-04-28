
print("Welcome In Bank")
# for show variables
def show_fun():
    print("1=credit")
    print("2=debit")
    print("3=show balance")
    print("4=Exit")
    
    

 
def sona_balc():
    f=open("sonabalance.txt","r")
    t=f.read()
    bal = int(t)
    print(bal)
    nw_bal=int(input("credit your balance"))
    new_bal=bal+nw_bal
    print(new_bal)
    new_bal_1=str(new_bal)
    f=open("sonabalance.txt","w")
    f.write(new_bal_1)
    f.close()

def kapil_balc():
     f = open("kpbalance.txt","r")
     t=f.read()
     print(t)
     bal=int(t)
     print(bal)
     nw_bal=int(input("credit your balance"))
     new_bal=nw_bal+bal
     print(new_bal)
     new_bal_1=str(new_bal)
     f=open("kpbalance.txt","w")
     f.write(new_bal_1)
     f.close()
    
def man_bal():
     f = open("manbal.txt","r")
     t = f.read()
     print(t)
     bal = int(t)
     print(type(bal))
     print(bal)
     nw_bal=int(input("credit your balance"))
     new_bal=nw_bal+bal
     print(new_bal)
     new_bal_1=str(new_bal)
     f=open("manbal.txt","w")
     f.write(new_bal_1)
     f.close()

    
     

def sona_bald():
    f=open("sonabalance.txt","r")
    t=f.read()
    print(t)
    bal=int(t)
    nw_bal=int(input("credit your balance"))
    new_bal=bal-nw_bal
    new_bal_1=str(new_bal)
    print(new_bal_1)
    f=open("sonabalance.txt","w")
    f.write(new_bal_1)
    f.close()

def kp_bald():
     f=open("kpbalance.txt","r")
     t=f.read()
     print(t)
     bal=int(t)
     new_bal=int(input("debit your balance"))
     new_bal=bal-new_bal
     new_bal_1=str(new_bal)
     print(new_bal_1)
     f=open("kpbalance.txt","w")
     f.write(new_bal_1)
     f.close()

def man_bald():
    f=open("manbal.txt","r")
    t=f.read()
    print(t)
    bal=int(t)
    nw_bal=int(input("credit your balance"))
    new_bal=bal-nw_bal
    new_bal_1=str(new_bal)
    print(new_bal_1)
    f=open("manbal.txt","w")
    f.write(new_bal_1)
    f.close()



     




     

     
def sonabal():
    f=open("sonabalance.txt","r")
    print(f.read())

def kpbal():
     f=open("kpbalance.txt","r")
     print(f.read())

def manbal():
     f=open("manbal.txt","r")
     print(f.read())

while True:
    pin = int(input("enter your pin"))
   


 

    if pin==1997:
        print("welcome sonali its your account")
        print("what do you do want")
        show_fun()
        choice=int(input("Enter your choice 1 2 3 4 "))
        

        if  choice==1:
            print("you want to be credit your balance")
            sona_balc()

        elif choice==2:
            print("you want to be debit your amount ")
            sona_bald()

        elif choice==3:
            print("your balnce")
            sonabal()
        elif choice==4:
            print("Exit")

        # kapi"s information//


    elif pin == 1996:
        print("welcome kapil its your account")
        print("what do you do want")
        show_fun()
        choice=int(input("Enter your choice 1 2 3 4 "))

        if  choice==1:
                print("you want to be credit your balance")
                kapil_balc()

        elif choice==2:
                print("ypu want to be debit your amount ")
                kp_bald()

        elif choice==3:
                print("your balnce")
                kpbal()

        elif choice==4:
                print("Exit") 


#  man"s information //


    elif pin == 2000:
        print("welcome Man its your account")
        print("what do you do want")
        show_fun()
        choice=int(input("Enter your choice 1 2 3 4 "))

        if choice == 1:
            print("credit your balance")
            man_bal()

        elif choice == 2:
            print("debit your balance")
            man_bald()

        elif choice == 3:
            print("its your balance")
            manbal()

        elif choice==4:
            print("thankyou")
        
    else :
        print("entered worng pin")