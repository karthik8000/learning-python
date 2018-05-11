names = ["karthik", "kumaran", "raj", "ram", 99, 7]

names.append("shruthi")
print(names)

for iteration, name in enumerate(names):
    greeting = "Hello " + str(name)
    print(greeting)
    print("Current iteration is "+ str(iteration))

new_name = "karthik"

for character in new_name:
    print(character)



print(names[4])
print(names[-3])
