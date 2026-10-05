import os


FILE_NAME="contacts.csv"

# check for contacts.csv file if not create

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,'w') as f:
        pass

def load_contacts():

    contacts_list=[]

    with open(FILE_NAME,'r') as file:
        for line in file:
            line=line.strip()
            values=line.split(',')

            contact={
                   "Name":values[0],
                   "Phone number":values[1],
                   "Email id":values[2]
            }

            contacts_list.append(contact)

    return contacts_list
# save_contacts update contact to csv file
def save_contacts(contacts_list):

      with open(FILE_NAME,'w') as file:
          for contact in contacts_list:
              line=f"{contact['Name']},{contact['Phone number']},{contact['Email id']}\n"
              file.write(line)

def add_contacts():
    contacts_list=load_contacts()
    
    name=input("Enter name:")
    phone=input("Enter phone number:")
    email=input("Enter email id:")

    

    contact={
        "Name":name,
        "Phone number":phone,
        "Email id":email
    }

    contacts_list.append(contact)

    save_contacts(contacts_list)

    print("Contact added successfully.")


def delete_contacts(Target_name):

    list_of_contacts=load_contacts()
    original_length=len(list_of_contacts)

    list_of_contacts=[c for c in list_of_contacts if c['Name'].lower()!=Target_name.lower()]

    

    if original_length>len(list_of_contacts):
        print(f"Deleted {Target_name}")
        save_contacts(list_of_contacts)
    else:
        print(f"Contact '{Target_name}' not found.")

def update_contacts(Target_name):

       phone=input("Enter phone number:")
       email=input("Enter email id:")
       list_of_contacts=load_contacts()      
       list_of_contacts=[c for c in list_of_contacts if c['Name'].lower()!=Target_name.lower()]
       contact={"Name":Target_name,
               "Phone number":phone,
               "Email id":email
               }

       list_of_contacts.append(contact)
       save_contacts(list_of_contacts)
       print(f"Contact '{Target_name}' updated.")

while True:
    print("Enter 1 to view contacts.")
    print("Enter 2 to save contact.")
    print("Enter 3 to delete contact.")
    print("Enter 4 to update contact")
    print("Enter 5 to  exit.")

    option=int(input("Enter option to proceed = "))

    if option==1:
        print(load_contacts())
        continue
    elif option==2:
        add_contacts()
        continue
    elif option==3:
        name=input("Enter name of person = ")
        delete_contacts(name)
        continue
    elif option==4:
        name=input("Enter name of person =")
        update_contacts(name)
        continue
    elif option==5:
        break