class student:
    #student mod
    def __init__(self, firstName,lastName,userName,PW,id):
        self.firstName = firstName # first name
        self.lastName = lastName  # last name
        self.id = id # uniqe id number
        self.userName = userName #uniqe username
        self.PW = PW  # uniqe password

    #prints out calss
    def __str__(self):
        # Justin,Hall,Jch24,password!,1001,
        n = "," # this makes csv esayir
        return  self.firstName +n+ self.lastName +n+ (self.userName)+n+(self.PW)+n+ str(self.id)+n

    def getUserName(self):#returens user name
        return (self.userName)

    def getUserName(self): #retreuns ID
        return (self.id)


james = student("justin","Hall","jch24","password!","1101")

