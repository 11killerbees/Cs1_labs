class course:
    #student mod
    def __init__(self,courseName,id):
        self.courseName = courseName # name of course
        self.id = id # uniqe id number

    #prints out calss
    def __str__(self):
        return  (self.courseName) + str(self.id)