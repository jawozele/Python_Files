class Car:
    def __init__(self,type,model,price,milesDrive,owner):
        self._Type=type
        self._Model=model
        self._Price=price
        self._MilesDrive=milesDrive
        self._Owner=owner

    def GetType(self):
        return self._Type
    def GetModel(self):
        return self._Model
    def GetPrice(self):
        self._Price=price
    def GetPrice(self):
        return self._Price
    def GetMilesDrive(self):
        return self._MilesDrive
    def GetOwner(self):
        return self._Owner

    def GetCurrentPrice(self):
        return self.GetPrice()-(self.GetMilesDrive()*10)

def main():
    JoshCar= Car("Mercedes Benz", 0000, 00000, 15, "J Awozele")
    CurrentPrice=JoshCar.GetCurrentPrice()
    print(" {}'s Car, New Price {}".format(JoshCar.GetOwner(),CurrentPrice))



    MaryCar = Car("BMW", 0000, 0000, 12, "Mary Doe")
    CurrentPrice = MaryCar.GetCurrentPrice()
    print(" {}'s Car, New Price {}".format(MaryCar.GetOwner(),CurrentPrice))
    print("App done")


if __name__ == '__main__':main()