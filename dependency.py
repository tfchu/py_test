'''
demonstrate class dependency
'''
class Baggage(object):
    """Baggage class
    """
    def __init__(self):
        self.weight = 0
    def get_weight(self):
        """return the baggage weight
        """
        return self.weight

class Car(object):
    """Car class
    """
    def __init__(self):
        self.weight = 0
        self.baggages = []
    def add_baggage(self, baggage):
        """add baggage to list, dependency 1: Y object as method argument
        """
        self.baggages.append(baggage)
    def add_baggage_weight(self, weight):
        """add one more baggage weight, dependency 2: Y object inside method
        """
        baggage = Baggage()
        baggage.weight = weight
        self.weight += baggage.get_weight()
    def get_weight_from_baggage_list(self):
        """print total baggage weight from list
        """
        weight = 0
        for baggage in self.baggages:
            weight += baggage.get_weight()
        print("Total weight from baggages: " + str(weight))
    def get_weight_from_weight(self):
        """print total baggage weight from weight attribute
        """
        print("Total weight from weight: " + str(self.weight))

def main():
    """main function to test the code
    """
    car = Car()
    # dependency 1
    baggage1 = Baggage()
    baggage1.weight = 60
    baggage2 = Baggage()
    baggage2.weight = 20
    car.add_baggage(baggage1)
    car.add_baggage(baggage2)
    car.get_weight_from_baggage_list()
    # dependency 2
    car.add_baggage_weight(60)
    car.add_baggage_weight(20)
    car.get_weight_from_weight()

if __name__ == "__main__":
    main()
