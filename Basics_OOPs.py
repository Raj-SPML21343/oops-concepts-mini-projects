class User:
    def log(self):
        print(self)


class Teacher(User):
    def log(self):
        print("I'm a teacher")


class Customer(User):
    def __init__(self, name, membership_type):
        # name, membership_type are attributes of the class, Customer
        self.name = name
        self.membership_type = membership_type
    # using private attributes

    @property
    def name(self):
        # getting name
        return self._name

    @name.setter
    def name(self, name):
        print("setting name")
        self._name = name

    @name.deleter
    def name(self):
        del self._name
    # Method Overwriting

    # If __str__() is overwritten, then its return value is printed, when we    print the object
    def __str__(self):
        return f"customer name = {self.name} and customer membership type = {self.membership_type} "

    # The __eq__() method is used to compare 2 objects are equal or not using == operator
    def __eq__(self, other_object):
        if self.name == other_object.name and self.membership_type == other_object.membership_type:
            return True

        return False

    # If you print customers_list, then overwritten __str__() method is called on each element
    __repr__ = __str__

    # update_membership is the method(Dynamic Method)
    def update_membership(self, new_membership):
        self.membership_type = new_membership

    # Static Method, doesn't have self parameter in it
    def read_customer(cust_name):
        print(f"Customer class is read {cust_name} personal data from DB")

    def print_all_customers(customers):
        for customer in customers:
            print(customer)


cust1 = Customer("Rajesh", "gold")
cust2 = Customer("Gayathri", "platinum")
customers_list = [cust1, cust2]
print(cust1.name, cust1.membership_type)
cust1.update_membership("platinum")
print(cust1.membership_type)
Customer.read_customer("Raj")
Customer.print_all_customers(customers=customers_list)
print(cust1 == cust2)
print(customers_list)
cust1.name = 'raj'
print(cust1.name)
# del cust1.name
# print(cust1.name)
teacher1 = Teacher()
users = [cust1, cust2, teacher1]
for user in users:
    user.log()
