
import_file = "allow_list.txt"
remove_list = "remove_list.txt"

# Task 2: Open the allow list file
with open(import_file, "r") as file:
    # Task 3: Read the file contents
    ip_addresses = file.read()

# Task 4: Convert the string into a list
ip_addresses = ip_addresses.split()

# Task 5 & 6: Iterate through the remove list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Task 7: Convert the list back to a string
ip_addresses = "\n".join(ip_addresses)

# Update the allow list file
with open(import_file, "w") as file:
    file.write(ip_addresses)
    
