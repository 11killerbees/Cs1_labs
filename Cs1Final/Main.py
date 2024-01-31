import MainMod

running = True
check = True
while running:
    while check:
        login= input("admin login [1] or student login [2]" ) # asks for login type
        if login != "1" and login != "2" :
            print("plase put 1 or 2 ")
        else:
            check = False


    if login == "1": # admin login
        check2 = True
        while check2:
            username=input("username")
            PW = input("password")
            if MainMod.adminLogin(username,PW):
                check2=False
            check4 = True
            while check4:
                print()
                print("what would you like to do")
                action = input("[1]add student,[2]add class,[3]add student to class,[4]look at list of students ")
                if action != "1" and action != "2" and action != "3" and action != "4":
                    print("put 1,2,3 or 4")

                elif action =="1":
                    MainMod.crateStudent()


                elif action =="2":
                    MainMod.crateClass()

                elif action =="3":
                    MainMod.addStudentToClass()

                elif action =="4":
                    MainMod.printStudentCSV()

    elif login == "2":
        check1 = True
        i = 0
        while i <=5 and check1:
            username = input("input username")
            PW = input("input password")
            if MainMod.studentLogin(username,PW):
                check1 = False

            else: running = False