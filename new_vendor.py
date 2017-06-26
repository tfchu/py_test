'''
client class exist
    - this class uses a vendor class's method
New vendor class is added
    - but new method is used with different interface
add this new vendor
    - without changing existing client and vendor's class
'''
from abc import ABCMeta, abstractmethod

class ABCVendor(metaclass=ABCMeta):
    @abstractmethod
    def go(self):
        pass
class Vendor(ABCVendor):
    def method(self):
        print('existing vendor\'s method')
    def go(self):
        self.method()
class NewVendor(ABCVendor):
    def new_method(self):
        print('this is a better method')
    def go(self):
        self.new_method()
class Client():
    def __init__(self):
        self.vendor = None
    def set_vendor(self, vendor):
        self.vendor = vendor
    def vendor_method(self):
        self.vendor.go()

def main():
    client = Client()
    client.set_vendor(Vendor())
    client.vendor_method()
    client.set_vendor(NewVendor())
    client.vendor_method()

if __name__ == '__main__':
    main()
