import json

file= "records.json"

def add_record():
    firstname= input("Enter the firstname name: ")
    lastname= input("Enter the lastname: ")
    age= input("Enter the age: ")
    

    record= {"firstname": firstname, "lastname": lastname, "age": age,  }

    try:
        with open(file, "r") as f:
            data= json.load(f)
    except FileNotFoundError:
        data= []
# 1. Write a function that gets an imput and adds it to an existing list
# 2. Write a simple function that points in the area of the array
# 3. Write a function that calculates the area of a rectangle
# 4. Draw a simple shape using turtle
# 5. Create simplle grading system.
    data.append(record)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def view_records():
    try:
        with open(file, "r") as f:
            data= json.load(f)
            for record in data:
                print(f"firstname: {record['firstname']}, lastname: {record['lastname']}, Amount: {record['age']}, class: {record['class']}")
    except FileNotFoundError:
        print("No records found.")

while True:
    choice= input("Welcome to the record management system.\n1. Add student\n2. View Records of students\n3. Exit\n Enter your choice: \n")
    
    match choice:
        case '1':
            add_record()
        case '2':
            print("Viewing all records of students:")
            view_records()
            print("-"*40)
        case '3':
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("❌❌❌❌Invalid choice. Please try again.")