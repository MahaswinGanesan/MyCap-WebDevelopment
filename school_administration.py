import csv
x=0
def storeDetails(info):
    global x
    with open('Student_details.csv','a') as f:
        heading=["Name","Class","Age","Register no.","Contact no."]
        writer=csv.writer(f)
        if x==0:
            writer.writerow(heading)
        writer.writerow(info)
        x=1

choice='y'
while choice=='y':
    studentDetails=input("Enter your Name, Class, Age, Register no., Contact no.:")
    student_details=studentDetails.split(' ')
    storeDetails(student_details)
    choice=input("Enter y to give another detail or n to exit:")

