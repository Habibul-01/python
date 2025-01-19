class Cyber:
    def __init__(self,number):
        self.number=number
        pass
class BCA(Cyber):
    def student(self):
        return f"{self.number} student is present in BCA department"
ob=BCA(150)
print(ob.student())