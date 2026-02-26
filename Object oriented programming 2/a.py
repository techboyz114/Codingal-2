class emp:
    def __init__(self):#constructor
        print('Employee object created')
    def __del__(self):#destructor
        print('Employee object is destroyed')
o1=emp()#object is created, call constructor automatically
del o1#object is destroyed, 




















#ACP
class expr:
    def __init__(self,ex):
        self.ex=ex
    def evaluate(self):
        print(eval(self.ex))
o1=expr('2 * 8')
o1.evaluate()