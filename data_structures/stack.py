import random
stack = []

def push():
    if Length == len(stack):
        print("List Reached it's Maximum")
    thing = input("Enter the Element you want to add:")
    stack.append(thing)
    print(stack)

def pop():
    stack.pop()
    print("It will delete the final Element in this Stack")
    print(stack)  


Length = int(input("Enter The lenght of the list:"))
if Length > len(stack):
    file = open("/home/mano/Python/Data_structures/stack_prog_data/stack_data.txt",'w')
    file.writelines(stack)
    file.close()

while Length > len(stack):
    print("Select the operation \n1.Adding\n2.Deleting\n3.Exit")
    choice = int(input("Enter Your Operation you want to Perform:"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter the Valid Operation:")

    
