#Tuples in python are like list but immutable

dimensions = (100,200)
print(dimensions[0])
#dimensions[0]=200 return error
for dimension in dimensions:
    print(dimension)
dimensions = (200,100)
for dimension in dimensions:
    print(dimension)