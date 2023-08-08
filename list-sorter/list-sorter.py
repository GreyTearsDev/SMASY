import random

students = []
class_a = []
class_b = []
class_c = []
    
            
def class_sorter2(list,a, b, c, number_of_classes): 
    turma_a = a
    turma_b = b
    turma_c = c
    
    #sets the initial length of 'turma_a' to never be greater than the the number of items in students divided by the number of classes
    
    while len(turma_a) < (len(list)) / number_of_classes:      
        student = random.choice(list)
        turma_a.append(student)
        list.remove(student)
    
    #ensures that the lenght of turma_b is the same as that of turma_a
        
    while len(turma_b) != len(turma_a):
        student = random.choice(list)
        if student not in turma_a:
            turma_b.append(student)
            list.remove(student)
    
    #adds the remaining students to the remaining class
        
    for student in list:
        if student not in turma_a and student not in turma_b:
            turma_c.append(student)
    
    #checks if the number of students in turma_c is greater than that of turma_a and moves the extra students to turma_a if so.
    
    if len(turma_c) > len(turma_a) or (turma_c) > len(turma_b):
        extra_student = random.choice(turma_c)
        turma_a.append(extra_student)
        turma_c.remove(student)
        
        
        
class_sorter2(students, class_a, class_b, class_c, 3)

print(f' Class A: {sorted(class_a)} \n')
print(f' Class B: {sorted(class_b)} \n')
print(f' Class C: {sorted(class_c)} \n')

students.close() # closes the document after being read

