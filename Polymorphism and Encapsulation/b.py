class Laptop:
    def __init__(self):  # constructor
        self.__sprice = 900  # private
        self.aprice = 650

    def info(self):
        print("Actual Price :", self.aprice)
        print("Selling Price :", self.__sprice)

    def change_price(self, a, s):
        self.aprice = a
        self.__sprice = s

o1 = Laptop()  # constructor called
o1.info()

o1.aprice = 700  # aprice will change
o1.__sprice = 1000  # __sprice is private so not accessible
o1.info()

o1.change_price(1000, 1500)
o1.info()
