import goofycoin as goof
import User_Management as um
#########################################################
# The consumed coins are valid:
# they were really created in previous transactions
# all the digital signature of previous owners are valid
#########################################################

user_dict={}
print "Hello! Welcome to Goofy Coin !"
pub,pri = um.adduser("##GOOFY##")
user_dict["##GOOFY##"]=[pub,pri]
start_amount = input("Enter the amount to start the chain : ")
sign = pri.sign(str(pub)+" "+str(pub)+" "+str(start_amount),'')
g=goof.goofy_coin(user_dict["##GOOFY##"][0],start_amount,sign)
print "##GOOFY## ADDED : Let's Start !"
print "Lets Add Users to the System !"
no_of_users = input("Please tell the No of Users : ")
for i in range(0,no_of_users):
    temp = raw_input("Enter the user name : ")
    pub,pri = um.adduser(temp)
    print "========================================"
    print "PUBLIC KEY : "+str(pub)
    print "PRIVATE KEY : "+str(pri)
    print "========================================"
    user_dict[temp]=[pub,pri]

while(True):
    try:
        print "-------MENU-------"
        print "1 : Make a new coin "
        print "2 : Do a transaction "
        print "3 : To see the entire chain "
        print "4 : To quit "
        print "5 : To verify "
        choice = input("Your Input : ")
        if(choice == 1):
            x=input("Enter Coin Value : ")
            sign = user_dict["##GOOFY##"][1].sign(str(user_dict["##GOOFY##"][0])+" "+str(user_dict["##GOOFY##"][0])+" "+str(x),'')
            g.makecoin(user_dict["##GOOFY##"][0],x,sign)
        elif(choice == 2):
            x=raw_input("Sender : ")
            y=raw_input("Receiver : ")
            z=input("Amount :")
            pub_sen = None
            pub_rec= None
            try:
                pub_sen = user_dict[x][0]
                pub_rec = user_dict[y][0]
                g.transaction(pub_sen,pub_rec,z,user_dict[x][1])
            except:
                print "Invalid users !! Try Again"

        elif(choice==3):
            g.print_goofy_list()
        elif(choice==4):
            break
        elif(choice==5):
            tid=raw_input("Transaction id : ")
            g.transaction_verify(tid)
        else:
            print "Enter Again ! "
    except:
        pass
