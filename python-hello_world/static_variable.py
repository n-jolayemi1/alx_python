class me:

    def __init__(sel, brand, skill):
        sel.brand = brand
        sel.skill = skill

    def who_am_i(sel):
        print("Brand-name: {}\nSkill-Rendering: {}\n".format(sel.brand, sel.skill))


information = me("Jolayemi", "footwear Crafting")
information.who_am_i()

class matured:

    def __init__(self, age):
        self.age = int(age)

    def age_confm(self):

        if self.age < 18:
            print("You are not matured")
        else:
            print("You are matured")

enter = matured(input("Enter your Age: "))
enter.age_confm()