#!/usr/bin/python3

class Robot:
    def __init__(self, name=None, energy=None, brand=None):
        self.name = name
        self.energy = energy
        self.brand = brand

    def hi(self):
        if self.name:
            print("Hi, I am {}!".format(self.name))
        else:
            print("I'm still a Robot with no names")

    def say_energy(self):
        if self.energy:
            print("I have {} amount of energy".format(self.energy))
        else:
            print("I'm weak for now, No Energy Available yet!")

    def say_brand(self):
        if self.brand:
            print("My Brand name is {}".format(self.brand))
        else:
            print("Brand is not diclosed yet!")

x = Robot("Ninja","89%", "mercedes") #An attribute in the class robot
y = Robot("Meco", "92%") #An attribute in the class robot

x.hi()
x.say_energy()
x.say_brand()

print("\n______\n")

y.hi()
y.say_energy()
y.say_brand()


""" x.name = "Ninja" 
x.function = "Farm Machinery"
x.brand = "Tesla"
x.energy = "89%"

y.name = "Meco"
y.function = "Automobile"
y.energy = "92%" """

#Robot.brand = "Mercedes" # general brand name for all attributes


""" print("\n\033[1m\033[3m\033[35m x attributes in the class (Robot)\n\033[0m{}\n{}\n{}".format(hi(x), energy(x), x.__dict__))

print("\n______\n")

print("\033[1m\033[4m\033[31m y attributes in the class (Robot)\n\033[0m{}\n{}\n{}".format(hi(y), energy(y), y.__dict__))

print("\n______\n")

print("\033[1m\033[4m\033[32m The main class (Robot)\n\033[0m",Robot.__dict__) """

class my_self:
    
    def __init__(self, name=None, age=None):
        print("Initializing information about my self")

        self.name = name
        self.__age = age

    def list_out(self):

        if self.name:
            print("My name is {}!".format(self.name))
        else:
            print("You did't ask for my name")

        if self.__age:
            print("I am {} years old".format(str(self.age)))
        else:
            print("You did't ask for my age")

    def say_name(self,name):
        self.name = name
    def get_name(self, name):
        return self.name
    
    def say_age(self, age):
        self.__age = age
    def get_age(self, age):
        return self.__age
    

if __name__ == "__main__":

    print("\n______\n")
    print("\n______\n")

    _1st = my_self('Muri', 4)
    #_1st.say_name()
    #_1st.say_age(4)
    _1st.list_out()

    print("\n______\n")
    print("\n______\n")

    _2nd = my_self('Rabiu')
    #_2nd.say_name()
    _2nd.list_out()

