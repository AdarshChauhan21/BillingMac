
#Automatic Billing and counter
import datetime
import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="1234",database="customer")
mycursor=con.cursor()
print("\nWelcome to Automatic and billing counter")
name=input("Enter Customer's name :\n(Press 0 to search in database):")
if name=="0":
    passwd=input("Enter the password :")
    if passwd=="1234":
        print("Authentication complete...")
        print("Select any operation\n1.Display all record\n2.Search for Customers\n3.Any other query\n4.Exit\n")
        choice=int(input("Choice :"))
        if choice==1:
            mycursor.execute("SELECT * FROM CUSTOMER")
            for x in mycursor:
                    print(x)
        elif choice==2:
            search=input("Enter name to be search :")
            query="SELECT * FROM CUSTOMER WHERE Customer_Name=%s"
            mycursor.execute(query,(search,))
            li=[]
            for x in mycursor:
                print(x)
                li.append(x)
            if li:
                print('')
            else:
                print("No user found of '",search,"' name")
        elif choice==3:
            print("Table name-Customer\nColumns-Customer_id,Customer_Name,Amount_paid")
            query=input("Enter a query for table customer: ")
            mycursor.execute(query)
            li=[]
            for x in mycursor:
                print(x)
                li.append(x)
            if li:
                print('')
            else:
                print("Invalid Query!!!")
        else:
            print("Exited!!")
            
        
        
    else:
        print("Authentication failed...")
else:
    amount=int(input("Enter the amount to be paid: "))
    cash=int(input("Enter the cash received by the customer: "))
    left=cash-amount
    print("Remaining amount paid to customer: ",left)
    mycursor.execute("INSERT INTO customer(Customer_Name, Amount_paid) VALUES(%s,%s)",(name,amount))
    con.commit()
    #for x in mycursor:
        #print(x)

    li=[]
    def func_notes(left):
        if left>=2000:
            li.append(2000)
            left=left-2000
            func_notes(left)
        elif left>=500:
            li.append(500)
            left=left-500
            func_notes(left)
        elif left>=200:
            li.append(200)
            left=left-200
            func_notes(left)
        elif left>=100:
            li.append(100)
            left=left-100
            func_notes(left)
        elif left>=50:
            li.append(50)
            left=left-50
            func_notes(left)
        elif left>=20:
            li.append(20)
            left=left-20
            func_notes(left)
        elif left>=10:
            li.append(10)
            left=left-10
            func_notes(left)
        elif left>=5:
            li.append(5)
            left=left-5
            func_notes(left)
        elif left>=2:
            li.append(2)
            left=left-2
            func_notes(left)
        elif left>=1:
            li.append(1)
            left=left-1
            func_notes(left)
              
    if cash<amount:
        print("You need to pay",left,"more")
    else:
        func_notes(left)
        #print("Notes to be given back to the customer : ",end="")
        #print(li)
        rec=input("Do you want to print the receipt(Y/N):")
        if rec=="y":
            myfile=open("Receipt.txt","w")
            time=datetime.datetime.now()
            myfile.write("Date and time :"+str(time))
            myfile.close()
            myfile=open("Receipt.txt","a")
            myfile.write("\nTotal amount to be paid :"+str(amount))
            myfile.write("\nCustomers Name :"+name)
            myfile.write("\nCash received by the customer: "+str(cash))
            myfile.write("\nRemaining amount paid to customer: "+str(left))
            myfile.write("\nNotes to be given back to the customer:")
            list2=[]
            for i in li:
                c=0
                for j in li:
                    if i==j:
                        c+=1
                if i not in list2:
                    myfile.write("\n"+str(i)+"="+str(c))
            
                list2.append(i)
            myfile.write("\nThank you for visiting us...\nVisit again")
            myfile.close()
            print("Generating Receipt...")
            myfile=open("Receipt.txt","r")       
            for i in myfile:
                print(i)
        else:
            print()
