import numpy as np
import pandas as pd

# Initialize an empty list to store student data
students = []

def add_student():
    """Add a new student"""
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = list(map(float, input("Enter marks for 3 subject (separated by space): ").split()))

    student = {"Name": name, "Age": age, "Marks": np.array(marks)}
    students.append(student)
    print(f"Student '{name}' added successfully!\n")

def show_students():
    """Display student data"""
    if not students:
        print("\nNo students available!")
        return
    
    df = pd.DataFrame([{"Name": s["Name"], "Age": s["Age"], "Average Marks": np.mean(s["Marks"])} for s in students])
    print("\nStudent Records:\n", df)

def analyze_data():
    """Analyze student data"""
    if not students:
        print("\nNo data available for analysis!")
        return
    
    ages = np.array([s["Age"] for s in students])
    avg_ages = np.mean(ages)

    all_marks = np.concatenate([s["Marks"] for s in students])
    avg_marks = np.mean(all_marks)
    max_marks = np.max(all_marks)
    min_marks = np.min(all_marks)

    print("\nData Analysis:")
    print(f"Average Age of Students: {avg_ages:.2f}")
    print(f"Average Marks: {avg_marks:.2f}")
    print(f"Highest Marks: {max_marks}")
    print(f"Lowest Marks: {min_marks}\n")

def save_data():
    """Save data to CSV"""
    if not students:
        print("\nNo data to save!")
        return
    
    df = pd.DataFrame([{"Name": s["Name"], "Age": s["Age"], "Marks": ', '.join(map(str, s["Marks"]))} for s in students])
    df.to_csv("students.csv", index=False)
    print("\nStudent data saved to 'students.csv' successfully!\n")

def main():
    """Main menu loop"""
    while True:
        print("\nStudent Data Management")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Analyze Data")
        print("4. Save Data to CSV")
        print("5.Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            analyze_data()
        elif choice =="4":
            save_data()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again. ")

if __name__ == "__main__":
    main()
