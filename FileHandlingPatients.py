import json, os


def load_patients():
    if os.path.exists("PatientList.json"):
        try:
            with open("PatientList.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []


def save_patients(patients):
    with open("PatientList.json", "w") as file:
        json.dump(patients, file, indent = 4)


def print_menu():
    print("1. Add Patient")
    print("2. View all Patients")
    print("3. View Patient by ID")
    print("4. Remove Patient")
    print("5. Exit")


def get_choice():
    choices = ["1","2","3","4","5"]
    while True:
        choice = input("Enter your Choice(1-5): ")
        if choice not in choices:
            print("Invalid Choice. Try Again")
        else:
            return choice
        

def add_patient():
    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            patient_id = int(input("Enter ID: "))
            break
        except ValueError:
            print("Invalid Age or Id. Try Again")

    patient = {
        "name": name,
        "age": age,
        "id": patient_id
    }

    patients = load_patients()
    patients.append(patient)
    save_patients(patients)
    print("Patient Added Sucessfully!")


def view_all_patients():
    patients = load_patients()

    if not patients:
        print("No Patients to View")
        return
    else:
        print("=====PATIENT-LIST=====")
        for patient in patients:
            print(f"Name: {patient['name']} | Age: {patient['age']} | ID: {patient['id']}")


def view_patient_by_id():
    patients = load_patients()
    if not patients:
        print("No Patients to View")
        return
    
    while True:
        try:
            patient_id = int(input("Enter Patient ID you want to View: "))
            break
        except ValueError:
            print("Invalid ID. Try Again")
    
    matches = [p for p in patients if p['id'] == patient_id]
    if not matches:
        print(f"No Patient found-{patient_id}")
        return
    
    print("=====Patient-Details=====")
    for patient in matches:
        print(f"Name: {patient['name']} | Age: {patient['age']} | ID: {patient['id']}")


def remove_patient():
    patients = load_patients()
    if not patients:
        print("No Patients to Remove")
        return
    
    while True:
        try:
            patient_id = int(input("Enter Patient ID you want to Remove: "))
            break
        except ValueError:
            print("Invalid ID. Try Again")

    matches = [p for p in patients if p['id'] == patient_id]
    if not matches:
        print(f"No Patient ID found-{patient_id}")
        return
    
    patients = [p for p in patients if p['id'] != patient_id]

    save_patients(patients)
    print(f"Patient with ID-{patient_id} Removed Sucessfully!")


def execution(choice):
    if choice == '1':
        add_patient()
    elif choice == '2':
        view_all_patients()
    elif choice == '3':
        view_patient_by_id()
    elif choice == '4':
        remove_patient()
    elif choice == '5':
        print("Exited. Thank You!")
        return False
            

def main():
    while True:
        print_menu()
        choice = get_choice()
        result = execution(choice)
        if result is False:
            break


if __name__ == "__main__":
    main()



            



