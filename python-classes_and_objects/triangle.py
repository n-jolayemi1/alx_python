class triangles:

    def __init__(my, base=0, height=0):
        my.base = base
        my.height = height

    @property
    def height(my):
        print('Retrieving the value of height')

        return my.__height
    
    @height.setter
    def height(my, value):

        if str(value):
            my.__height = int(value)
        else:
            print('Error!, Expecting number')

    @property
    def base(my):
        print('Retrieving the value of base')

        return my.__base
    
    @base.setter
    def base(my, value):
        if str(value):
            my.__base = int(value)
        else:
            print('Error!, Expecting number')

    def areaOfTriangle(my):
        return int(my.__base) * int(my.__height)


def main():
    atriangle = triangles()
    base = input("Enter a valur for base: ")
    height = input("Enter a valur for height: ")
    atriangle.base = base
    atriangle.height = height
    area = atriangle.areaOfTriangle()
    print(atriangle.height)
    print(atriangle.base)
    print(area)


main()