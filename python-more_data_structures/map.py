""" def multiple(num): 
    for i in range(13):
        if i == 0: continue
        else:
            multiply = num * i
        print (multiply) """
numbers = (2,3,4,5)
do_it = map(multiple,numbers)
multiply = list(do_it)
print("{} x {} = {}".format())