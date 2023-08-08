#!/usr/bin/python3

class person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, How are you', self.name)

name = person('Jolayemi')
name.say_hi()
