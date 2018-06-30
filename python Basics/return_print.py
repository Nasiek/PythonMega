def converter(original_unit, coefficient=0.3048):
    return original_unit * coefficient
print (converter(10, 0.62)) 



def returning():
    return 10

def printing():
    return 100

returning()
printing()
print(type(returning()))
print(type(printing()))
 
