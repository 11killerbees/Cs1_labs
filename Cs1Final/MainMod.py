
import StudentMod

def lookForBlock(block): # this turns a csv into a list
    semi = 0
    blockList=[]
    for i in range(len(block)):
        blockString = block[semi:i]
        char = block[i:i+1]
        if char == ",":
            blockList.append(blockString)
            semi = i+1
    return blockList

def crateStudent():
    makeing = True # this is for while your makeing a new stdent class
    check1 = True # this is a check that needs to be passed brfor a student class can be added
    check2 = True  # this is a check that needs to be passed brfor a student class can be added
    check3 = True  # this is a check that needs to be passed brfor a student class can be added

    while makeing:
        firstName = input("enter student first name ")
        lastName = input("enter student last name")
        while check1:
            userName = input("create student user name ")
            if compareStudentIndex(userName,2,False):
                check1 = False
        while check2:
            PW = input("create student password (must be a length of 6 or more )")
            if len(PW)>= 6:
                check2 = False


        while check3:
            id = input("id num(id num should start with grad year with 5 leading numnbers ex: 2712345) ")
            if compareStudentIndex(id,4,False) and len(id) == 7:
                check3 = False
        newStudent = StudentMod.student(firstName,lastName,userName,PW,id)
        print("new student made")
        students = open("Student.csv", "a")

        students.write("\n")
        students.write(str(newStudent))

        students.close()
        makeing = False


# this this compares a student class agenst the student csv at an collem
def compareStudentIndex(student,index,returnStudent): #student, row
    students = open("Student.csv", "a")
    students.close()
    students = open("Student.csv", "r")

    line = students.readlines()
    for i in range(1,len(line)):
        temp1 = (lookForBlock(line[i]))
        compare = temp1[index]
        if compare == student:
            if returnStudent:
                return temp1
            else:
                return False
    if returnStudent:
        return print("student not found")

    return True

    students.close()
#######################################################################
def compareAdminIndex(student,index,returnStudent): #student, row
    students = open("Admin.csv", "a")
    students.close()
    students = open("Admin.csv", "r")

    line = students.readlines()
    for i in range(1,len(line)):
        temp1 = (lookForBlock(line[i]))
        compare = temp1[index]
        if compare == student:
            if returnStudent:
                return temp1
            else:
                return False
    return True

    students.close()
###############################################
def compareCourseIndex(student,index,returnStudent): #student, row
    students = open("Course.csv", "a")
    students.close()
    students = open("Course.csv", "r")

    line = students.readlines()
    for i in range(1,len(line)):
        temp1 = (lookForBlock(line[i]))
        compare = temp1[index]
        if compare == student:
            if returnStudent:
                return temp1
            else:
                return False
    return True

    students.close()
####################################################

def crateClass():
    makeing = True # this is for while your makeing a new stdent class
    check1 = True # this is a check that needs to be passed brfor a student class can be added

    while makeing:
        Name = input("name the new class not uniqe and no ',' ")
        while check1:
            classID = input("enter class id , this should be 7 uniqe numbers")
            if compareCourseIndex(classID,1,False) and len(classID)==7:
                check1 = False

        print("new class made")
        students = open("Course.csv", "a")

        students.write("\n")
        students.write(Name+","+classID+",")
        students.close()
        temp2 = Name+'-'+classID+".csv"
        temp = open(temp2,"a")
        temp.close()

        makeing = False


####################################################

def studentLogin(userName,Pw):
    for i in range(5):
        if not compareStudentIndex(userName,2,False) and not compareStudentIndex(Pw, 3,False):
            print("your now loged in as", userName)
            return True
    return False

def adminLogin(userName,Pw):
    for i in range(5):
        if not compareAdminIndex(userName,2,False) and not compareAdminIndex(Pw, 3,False):
            print("your now loged in as", userName)
            return True
    return False

def getStudentFromCSV(id):
    n = ","
    temp = compareStudentIndex(id,4,True)
    temp2 = temp[0]+n+temp[1]+n+temp[4]+n
    return temp2

def getCourseFromCSV(id):
    n = ","
    temp = compareCourseIndex(id,1,True)
    temp2 = temp[0]+"-"+temp[1]+".csv"
    return temp2

def addStudentToClass(studentID,classID,grade):
    student = getStudentFromCSV(studentID)
    try:
        classCSV = getCourseFromCSV(classID)
        CSV= open(classCSV,"a")
        CSV.write("\n")
        CSV.write(student+grade+",")
        print("here")



    except:
        print("classID not found")


def addClass(name,id):
    Courses = open("Courses.csv", "a")
    Courses.close()

def printStudentCSV():
    CSV = open("Student.csv","a")
    CSV.close()
    CSV = open("Student.csv","r")

    line = CSV.readlines()
    for i in range(1, len(line)):
        print(line[i])

#studentLogin("mjf24","123456")

#print(getStudentFromCSV("1234567"))
#if adminLogin("jch24","password"):
   # print("here")
#crateClass()
