class pets:

    def __init__(my, name="", category=""):
        my.name = name
        my.category = category

    def pet_name(my):
        print("my name is {}".format(my.name))

    def pet_category(my):
        print("I belong to the {} category".format(my.category))

def main():
    print('______________')
    print('______________\n')


    goats = pets('shanko', 'Goat')
    goats.pet_name()
    goats.pet_category()

    print('______________')
    print('______________')
    print('______________\n')

    sheep = pets('Bruno', 'Dog')
    sheep.pet_name()
    sheep.pet_category()



main()