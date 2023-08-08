#!/usr/bin/python3

class robot:

    # Represents a Robot with a name

    population = 0

    def __init__(self, name):
        self.name = name
        print('Initializing {}'.format(self.name))

        robot.population += 1

    def say_hi(self):

        print('Greetings, My master call me {}'.format(self.name))

    def die(self):
        
        print("{} is being destroyed!".format(self.name))

        robot.population -= 1

        if robot.population == 0:
            print("{} was the last one!".format(self.name))
        else:
            print("There are still {:d} robot working".format(robot.population))


    @classmethod

    def how_mony(cls):
        print("We have {} robots".format(cls.population))


robot1 = robot('AD-R34')
robot1.say_hi()
robot.how_mony()


robot2 = robot('GH-R43')
robot2.say_hi()
robot.how_mony()

print("\n Robots can do some work\n")

print("Robots have finished their work. so let destroy them")
robot1.die()
robot2.die()

robot.how_mony()
