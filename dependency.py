'''
demonstrate class dependency
'''
class Baggage(object):
    """Baggage class
    """
    def __init__(self, weight):
        self.weight = weight
    def get_weight(self):
        """return the baggage weight
        Returns: weight of the baggage
        """
        return self.weight

class Car(object):
    """Car class
    """
    def __init__(self):
        self.weight = 0
    def add_baggage_weight(self, baggage):
        """add one more baggage weight
        """
        self.weight += baggage.get_weight()
    def get_total_baggage_weight(self):
        """print total baggage weight
        """
        print(self.weight)

def main():
    #print('hello python')
    car = Car()
    car.add_baggage_weight(Baggage(60))
    car.add_baggage_weight(Baggage(20))
    car.get_total_baggage_weight()

if __name__ == "__main__":
    main()
