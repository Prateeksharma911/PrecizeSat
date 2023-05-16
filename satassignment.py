import json

# In-memory storage for SAT results
sat_results = {}

# Function to calculate the 'Passed' status
def calculate_passed_status(score):
    if score > 0.3:
        return 'Pass'
    else:
        return 'Fail'

# Function to insert data
def insert_data():
    name = input("Enter candidate name: ")
    address = {
        'City': input("Enter city: "),
        'Country': input("Enter country: "),
        'Pincode': input("Enter pincode: ")
    }
    sat_score = float(input("Enter SAT score: "))
    passed = calculate_passed_status(sat_score)
    
    sat_results[name] = {
        'Address': address,
        'SAT score': sat_score,
        'Passed': passed
    }
    print("Data inserted successfully!")

# Function to view all data
def view_all_data():
    print(json.dumps(sat_results, indent=4))

# Function to get rank
def get_rank():
    name = input("Enter candidate name: ")
    
    sorted_results = sorted(sat_results.items(), key=lambda x: x[1]['SAT score'], reverse=True)
    rank = [result[0] for result in sorted_results].index(name) + 1
    
    print(f"{name} has rank {rank}")

# Function to update score
def update_score():
    name = input("Enter candidate name: ")
    if name in sat_results:
        sat_score = float(input("Enter new SAT score: "))
        passed = calculate_passed_status(sat_score)
        
        sat_results[name]['SAT score'] = sat_score
        sat_results[name]['Passed'] = passed
        print("Score updated successfully!")
    else:
        print("Record not found.")

# Function to delete one record
def delete_record():
    name = input("Enter candidate name: ")
    if name in sat_results:
        del sat_results[name]
        print("Record deleted successfully!")
    else:
        print("Record not found.")

# Main menu
while True:
    print("==== SAT Results Application ====")
    print("1. Insert data")
    print("2. View all data")
    print("3. Get rank")
    print("4. Update score")
    print("5. Delete one record")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_data()
    elif choice == "2":
        view_all_data()
    elif choice == "3":
        get_rank()
    elif choice == "4":
        update_score()
    elif choice == "5":
        delete_record()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
