import StudentMod
class admin:
    #student mod
    def __init__(self, firstName,lastName,userName,PW):
        self.firstName = firstName # first name
        self.lastName = lastName  # last name
        self.userName = userName #uniqe username
        self.PW = PW  # uniqe password

    #prints out calss
    def __str__(self):
        return  self.firstName + self.lastName + (self.userName) +(self.PW)
