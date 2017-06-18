'''
demonstate inheritance, e.g. Taxi inherits Car
'''
class Car():
    '''show car brand and model'''
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_brand(self):
        '''get car brand'''
        print('Car brand is {}'.format(self.brand))
    def get_model(self):
        '''get car model'''
        print('Car model is {}'.format(self.model))
# Taxi inherits Car, put Car as Taxi Class argument
class Taxi(Car):
    '''show taxi company, additional attribute/method to car'''
    def __init__(self, brand, model, company):
        # call parent class constructor, self needs to be included
        # brand and model needs to repeat here
        Car.__init__(self, brand, model)
        self.company = company
    def get_company(self):
        '''get taxi company'''
        print('Taxi company is {}'.format(self.company))
def main():
    '''main function to test code'''
    taxi = Taxi('Toyota', 'Corolla', 'Taxi Plus')
    taxi.get_brand()
    taxi.get_model()
    taxi.get_company()

if __name__ == '__main__':
    main()
