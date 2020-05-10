Dict = {}
print("Initial nested dictionary:-")
print(Dict)

Dict['Dict1'] = {}

# Adding elements one at a time
Dict[0]['name'] = 'Bob'
Dict[0]['age'] = 21
print("\nAfter adding dictionary Dict1")
print(Dict)

# Adding whole dictionary
Dict[1] = {'name': 'Cara', 'age': 25}
Dict[2] = {'name': 'Aditya', 'age': 25}
print("\nAfter adding dictionary Dict1")
print(Dict)