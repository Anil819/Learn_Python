class Student:
    Sub1 = 1
    Sub2 = 2
    Sub3 = 3
    
    def __init__(self, name, Listofmarks):
        self.name = name
        self.Listofmarks = Listofmarks
        
    # @staticmethod  don not require self keyword
    
    def Avg(self):
        sum = 0
        for avg in self.Listofmarks:
            sum = sum + avg
        Average = sum / 3
        print("Average of Marks : ", Average)


std1 = Student("ANil", [12, 34, 56])
print(std1.name, std1.Listofmarks)
std1.Avg()

std2 = Student("Govind", [43, 57, 69])
print(std2.name, std2.Listofmarks)

std2.Avg()
