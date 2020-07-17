def login():
    global password
    global identification
    username = input("Please enter your username:   ")
    password = input("Please enter your password:   ")
    print ("\n")
    identification = False
    with open ("accountfile.txt","r") as file:
        for line in file:
            user, passe = line.split()
            if username == user:
                identification = password == passe
                #print("You have accessed the system ")
                break

    if username!= user:
        print("Sorry the username is not in our system please register \n")
        main_menu()



def hr_menu():
    def register():
        username = input("Enter desired username:  ")
        password = input("Enter desired password:    ")
        file = open("accountfile.txt", "a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write("\n")
        file.close()
        print("The account has been registered")
        hr1 = input("Enter 1 to return to Human Resources Menu")
        if hr1 == "1":
            hr_menu()

    def holidays():
        with open ("holidays.txt","r") as f: # f is just a variable
            f_contents = f.read() #read all lines
            print(f_contents)
        hr2 = input("Enter 1 to return to Human Resources Menu")
        if hr2 == "1":
            hr_menu()

    def Faq():
        with open ("FAQ.txt","r") as l:
            l_contents = l.read()
            print (l_contents)
        hr3 = input("Enter 1 to return to Human Resources Menu")
        if hr3 == "1":
            hr_menu()

    def early_leave():
        with open ("early leaves.txt","r") as q:
            q_content = q.read()
            print (q_content)
        hr4 = input("Enter 1 to return to Human Resources Menu")
        if hr4 == "1":
            hr_menu()

    def V(): # View lecturer profile
        with open ("status.txt","r") as a:
            a_content = a.read()
            print (a_content)
        hr5 = input("Enter 1 to return to Human Resources Menu")
        if hr5 == "1":
            hr_menu()
#def S():
    #searchfile = open("lecturer profile.txt","r")
    #for line in searchfile:
        #if

    def MVS():
        print ("1.  View")
        print ("2. Search")
        choose = input("Enter a number")
        if choose == ("1"):
            V()
        if choose == ("2"):
            print ("good")
        hr6 = input("Enter 1 to return to Human Resources Menu")
        if hr6 == "1":
            hr_menu()

    def hr_menu():
        print ("        *****   HR Menu Functions   *****        \n")
        print ("1.  Create New Lecturer / Academic Leader’s profile\n")
        print ("2.  Modify, View and Search Lecturer Profile\n")
        print ("3.  View the employee leave status\n")
        print ("4.  Upload the yearly leaves in system\n")
        print ("5.  Upload the Public and University Holidays\n")
        print ("6.  Update and Upload FAQs About University’s Leave Policies in System.\n") #Done just write FAQ and check for upload funciton

        choise = input("Enter your Choise:  ")
        if choise == "1":
            register()
        if choise == "2":
            MVS()
        if choise == "3":
            V() # call function
        if choise == "4":
            early_leave()
        if choise == "5":
            holidays()
        if choise == "6":
            Faq()
    login()
    hr_menu() #************************************

def ac_menu():
    def view_leave():
        with open ("leaves_form.txt","r") as f:
            f_contents = f.read()
            print(f_contents)

        ac1 = input("Enter 1 to return to Academic Leader Menu: ")
        if ac1 == "1":
            ac_menu()


    def approving():
        with open ("leave_form.txt","r") as f:
            f_contents = f.read()
            print(f_contents)
        print ("To Approve Press 1 to Reject press 2")
        approving_rejecting= input("Please Enter a Choice:      ")
        if approving_rejecting == "1":
            print("Approved")
            approved = open("approving_rejecting.txt","w")
            approved.write("Approved")
            approved.close()
        if approving_rejecting == "2":
            print ("Rejected")
            approved = open("approving_rejecting.txt", "w")
            approved.write("Rejected")
            approved.close()
        ac2 = input("Enter 1 to return to Academic Leader Menu: ")
        if ac2 == "1":
            ac_menu()




    def holidays():
        with open ("holidays.txt","r") as f:
            f_contents = f.read()
            print(f_contents)
        ac3 = input("Enter 1 to return to Academic Leader Menu: ")
        if ac3 == "1":
            ac_menu()

    def policies():
        with open ("policies.txt","r") as f:
            f_contents = f.read()
            print(f_contents)
        ac1 = input("Enter 1 to return to Academic Leader Menu: ")
        if ac1 == "1":
            ac_menu()



    def al_menu():
        print ("        *****   Welcome to Academic leader menu   *****     \n")
        print ("1.  View Lecturer's Leave Application","\n")
        print ("2.  Approve or Reject the Leave","\n")
        print ("3.  View Public and University Holidays","\n")
        print ("4.  University Leave Policies\n",)
        pick_number= input("Please Choose a Number for the list:        ")
        if pick_number == "1":
            view_leave()
        if pick_number == "2":
            approving()
        if pick_number == "3":
            holidays()
        if pick_number == "4":
            policies()

    login()
    al_menu()

def lecturer_menu():

    def leave_application():
        leave_form = open("leaves_form.txt", "w")
        leave_form.write(input("Enter username: "))
        leave_form.write("\n")
        leave_form.write(input("Contact Number: "))
        leave_form.write("\n")
        leave_form.write(input("Reason: "))
        leave_form.write("\n")
        leave_form.close()
        print("You leave application is sent, please check the statue after a while\n")
        le1 = input("Enter 1 to return to Lecturer Menu: ")
        if le1 == "1":
            lecturer_menu()


    def check_status():
        file1 = open('approving_rejecting.txt','r')
        if 'Approved' or 'approved' in open('approving_rejecting.txt').read():
            print("true")
        if 'Rejected ' or "rejected" in open ('approving_rejecting.txt').read():
            print("false")
        file1.close()
        le2 = input("Enter 1 to return to Lecturer Menu: ")
        if le2 == "1":
            lecturer_menu()


    def public():
        with open ("holidays.txt","r") as f:
            f_contents = f.read()
            print(f_contents)
        le3 = input("Enter 1 to return to Lecturer Menu: ")
        if le3 == "1":
            lecturer_menu()

    def policies():
        with open ("policies.txt","r") as f:
            f_contents = f.read()
            print(f_contents)
        le4 = input("Enter 1 to return to Lecturer Menu: ")
        if le4 == "1":
            lecturer_menu()

    def lecture_menu():
        print ("        *****   Welcome to lecturer Menu  *****        \n")
        print ("Choose a number from the following list ","\n")
        print ("1.  Apply for a leave ","\n")
        print ("2.  Check the status of the leave application","\n")
        print ("3.  View Public Holidays and University  Holidays","\n")
        print ("4.  University Polices ","\n")
        choose1 = input("Please Enter a number from the following list:  ")
        if choose1 == "1":
            leave_application()
        if choose1 == "2":
            check_status()
        if choose1 == "3":
            public()
        if choose1 == "4":
            policies()

    login()
    lecture_menu()

def main_menu():
    print ("*****   Welcome to EMPLOYEES LEAVE MANAGEMENT SYSTEM (ELMS)  *****\n")
    print ("Choose one of the following Employees  \n ")
    print ("1.  Human Resources ")
    print ("2.  Academic Leader ")
    print ("3.  Lecturer \n")
    employees = input("Enter a Choice:  ")
    if employees == "1":
        hr_menu()
    if employees == "2":
        ac_menu()
    if employees == "3":
        lecturer_menu()
main_menu()














