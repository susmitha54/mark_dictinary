marks_dictionary={}
x=int(input("Enter no.of subject: "))
tot=0
for i in range(x):
    subject_name=input("Enter the subject name: ")
    marks=int(input("Enter the mark:"))
    marks_dictionary[subject_name]=marks
    
for subject in marks_dictionary:
    marks=marks_dictionary[subject]
    print(subject,':',marks)
    tot=tot+marks
    avg=tot/x
print("The total mark:",tot) 
print("The average of the mark:",avg)