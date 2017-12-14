# Classes & Objects

class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)

#brad = Person('Brad Travsery', 'brad@gmail.com')
# brad.set_name('Brad Travsery')
# brad.set_email('brad@gmail.com')

#print(brad.get_name())

#print(brad.toString())



class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self):
        self.__balance =  balance

    def get_balanace(self, balance):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of  {} can be contacted at {}'.format(self.__name, self.__balance, self.__email)

john = Customer('John Doe', 'jdoe@gmail.com', 100)
print(john.toString())