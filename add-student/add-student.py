
class_a = []
class_b = []
class_c = []

def add_student():
    print('What class do you want to access? \nA, B or C \nPress a key ')
    prompt = input()
  
    if prompt in ['A', 'a']:
        name_student = input('Write the name of the student: ').title()
        class_a.append(name_student)
        print(f'"{name_student}" was added to Class A.'  )
        
    elif prompt in ['B', 'b']:
        name_student = input('Write the name of the student: ').title()
        class_b.append(name_student)
        print(f'"{name_student}" was added to Class B.'  )
       
    elif prompt in ['C', 'c']:
        name_student = input('Write the name of the student: ').title()
        class_c.append(name_student)
        print(f'"{name_student}" was added to Class C.'  )
    else:
        print(f'Class "{prompt}" does not exit.')
        print('Please, check your spelling and try again.\n')
        add_student()
         
    add_more_prompt() 
    return

                      
def add_more_prompt():
    while True:
        prompt = input('\nPress "A" to add another student \nPress "B" to go back and quit the program ')
        if prompt not in ['A', 'a', 'B', 'b']:
            print('Please, check your spelling and try again.\n')
            add_more_prompt()
        elif prompt in ['A', 'a']:
            add_student()
        else:
            return



add_student()		
			 

print(f'\nThese are the current classes \nClass A: {class_a} \nClass_B: {class_b} \nClass C: {class_c}')
print('\nGoodbye.')
a = open('a.txt', 'w')
print(class_a, file = a)
a.close()

b = open('b.txt', 'w')
print(class_b, file = b)
b.close()

c = open('c.txt', 'w')
print(class_c, file = c)
c.close()









    
    