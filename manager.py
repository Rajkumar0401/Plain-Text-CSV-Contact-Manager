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

def save_contacts(contacts_list):

      with open(FILE_NAME,'w') as file:
          for contact in contacts_list:
              line=f"{contact['Name']},{contact['Phone number']},{contact['Email id']}\n"
              file.write(line)


def delete_contacts(Target_name):

    list_of_contacts=load_contacts()
    original_length=len(list_of_contacts)

    list_of_contacts=[c for c in list_of_contacts if c['Name'].lower()!=Target_name.lower()]

    

    if original_length>len(list_of_contacts):
        print(f"Deleted {Target_name}")
        save_contacts(list_of_contacts)
    else:
        print(f"Contact '{Target_name}' not found.")

