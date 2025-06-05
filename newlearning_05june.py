class narsingh:
  def __init__(self,a,b):
        self.a=a
        self.b=b
class hemant(narsingh):
  def __init__(self,a,b):
         super().__init__(a,b)
  def display(self):
    print(f"{self.a}this is the first value{self.b}")
a=hemant("ram","shyam")
##to access parent function 
a.pringt()
##to access method

a.display()
