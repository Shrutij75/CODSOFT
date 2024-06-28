contact = {}

def display_contact():
    print("Name\t\t Contact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

print("------CONTACT BOOK-------")
print("1. For Add contact")
print("2. For View Contact List")
print("3. For Search contact")
print("4. For Update Contact")
print("5. For Delete Contact")
print("6. For Exit")

while True:
    ch = int(input("Enter the choice:"))
    
    if ch == 1:
        name = input("Enter the name: ")
        phone = int(input("Enter the phone number: "))
        contact[name] = phone
    
    elif ch == 2:
        if not contact:
            print("Empty contact book.")
        else:
            display_contact()
    
    elif ch == 3:
        nme = input("Enter the name of the user you want to search: ")
        if nme in contact:
            print(nme, "contact number is:", contact[nme])
        else:
            print("Contact not found.")
    
    elif ch == 4:
        nme = input("Enter the contact name you want to update the phone number: ")
        if nme in contact:
            phone = int(input("Enter mobile number: "))
            contact[nme] = phone
            print("Contact updated!!!!")
            display_contact()
        else:
            print("Contact not found!!!")
    
    elif ch == 5:
        nme = input("Enter the contact name you want to delete: ")
        if nme in contact:
            confirm = input("Do you want to delete this contact y/n: ")
            if confirm.lower() == 'y':
                contact.pop(nme)
                print("Contact deleted!!!")
                display_contact()
            else:
                print(nme, "not deleted from contact book.")
        else:
            print(nme, "not found in contact book!!")
    
    elif ch == 6:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice! Please enter a valid number.")
