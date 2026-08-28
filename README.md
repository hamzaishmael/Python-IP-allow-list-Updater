# Python Allow List Updater

## Project Overview

This project demonstrates the use of Python to automate the process of updating an IP address allow list. The scenario is based on a healthcare organisation that restricts access to sensitive patient information by allowing only authorised IP addresses to access a restricted subnetwork. A separate remove list identifies IP addresses that should no longer have access. I developed a Python algorithm that reads the existing allow list, checks it against the remove list, removes matching IP addresses, and writes the updated list back to the file.

---

## Scenario

A healthcare organisation maintains an IP address allow list for employees who require access to restricted patient records. When an employee no longer requires access, their IP address is added to a remove list.

Manually checking and updating the allow list can be inefficient and prone to human error. Python can automate this process by comparing the two lists and removing any IP addresses that appear on the remove list.

---

## Objective

The objective of this project was to create a Python algorithm that:

1. Opens the allow list file.
2. Reads the contents of the file.
3. Converts the contents into a list of IP addresses.
4. Iterates through the remove list.
5. Identifies IP addresses that appear in both lists.
6. Removes matching addresses from the allow list.
7. Converts the updated list back into a string.
8. Writes the revised list back to the original file.

---

# Python Implementation

## 1. Open the File That Contains the Allow List

```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    ip_addresses = file.read()
```

### Explanation

`import_file` stores the name of the file containing the IP allow list.

The `open()` function is used to access the file. The `"r"` argument opens the file in **read mode**, allowing the program to retrieve its contents.

The `with` statement manages the file automatically. Once the indented block finishes, Python closes the file automatically, reducing the risk of leaving the file open.

The variable `file` represents the opened file while the `with` block is running.

---

## 2. Read the File Contents

```python
ip_addresses = file.read()
```

The `.read()` method retrieves the contents of the file and stores them in the `ip_addresses` variable as a string.

At this stage, the IP addresses are stored together as one string rather than as individual list elements.

---

## 3. Convert the String into a List

```python
ip_addresses = ip_addresses.split()
```

The `.split()` method converts the string into a list.

Because the IP addresses are separated by whitespace/new lines in the file, `.split()` separates each IP address into an individual list element.

For example:

```text
192.168.1.10
192.168.1.20
192.168.1.30
```

becomes:

```python
[
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30"
]
```

This makes it possible to individually identify and remove IP addresses.

---

## 4. Iterate Through the Remove List

```python
for element in remove_list:
```

A `for` loop is used to iterate through every IP address contained in `remove_list`.

The variable `element` represents the current IP address being checked during each iteration.

For example, if:

```python
remove_list = ["192.168.1.20", "192.168.1.40"]
```

the loop checks each address individually.

---

## 5. Remove IP Addresses from the Allow List

```python
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
```

The `if` statement checks whether the current `element` from the remove list exists in the `ip_addresses` list.

The `in` operator performs the membership check.

If the IP address exists in the allow list, the `.remove()` method removes it.

The `.remove()` method can be used safely in this algorithm because there are no duplicate IP addresses in the `ip_addresses` list. Therefore, each IP address only needs to be removed once.

---

## 6. Update the File with the Revised List

```python
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

The `.join()` method converts the updated list back into a single string.

The string `"\n"` is used as the separator, which places each IP address on a separate line when the data is written back to the file.

The file is then opened using a second `with` statement.

The `"w"` mode opens the file in **write mode**, replacing the existing contents with the updated allow list.

The `.write()` method writes the revised string to the file.

---

# Complete Python Script

```python
# Store the name of the allow list file
import_file = "allow_list.txt"

# Read the contents of the allow list
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string into a list
ip_addresses = ip_addresses.split()

# Remove IP addresses found on the remove list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert the list back into a string
ip_addresses = "\n".join(ip_addresses)

# Write the updated allow list back to the file
with open(import_file, "w") as file:
    file.write(ip_addresses)
```

> **Note:** `remove_list` is assumed to already be provided by the security workflow or lab environment.

---

# Algorithm Workflow

```text
allow_list.txt
      │
      ▼
Open file with open()
      │
      ▼
Read contents with .read()
      │
      ▼
Convert string to list with .split()
      │
      ▼
Iterate through remove_list
      │
      ▼
Is the IP address in ip_addresses?
      │
   ┌──┴──┐
  YES    NO
   │      │
   ▼      │
.remove() │
   │      │
   └──┬───┘
      ▼
Convert list to string
using "\n".join()
      │
      ▼
Open file in write mode
      │
      ▼
Write updated list
with .write()
      │
      ▼
Updated allow_list.txt
```

---

# Security Relevance

This algorithm demonstrates how Python can be used to automate an access-control task in a cybersecurity environment.

Maintaining an accurate allow list is important because outdated access permissions can provide unnecessary access to restricted resources. Automating the removal process reduces manual effort and helps security teams consistently apply access-control changes.

The same approach can be adapted for other security automation tasks involving lists of IP addresses, usernames, devices, or other authorised and unauthorised entities.

---

# Python Concepts Demonstrated

| Python Concept | Purpose                                             |
| -------------- | --------------------------------------------------- |
| `open()`       | Opens the allow list file                           |
| `with`         | Manages the file safely and automatically closes it |
| `.read()`      | Reads the contents of the file                      |
| `.split()`     | Converts the string into a list                     |
| `for` loop     | Iterates through the remove list                    |
| `if` statement | Checks whether an IP address exists                 |
| `in` operator  | Performs a membership check                         |
| `.remove()`    | Removes an IP address from the allow list           |
| `.join()`      | Converts the list back into a string                |
| `.write()`     | Writes the updated list to the file                 |

---

# Skills Demonstrated

* Python programming
* Security automation
* File handling
* Access-control management
* List manipulation
* Conditional statements
* Iteration
* Basic cybersecurity scripting
* Automation of security procedures

---

# Project Outcome

The completed algorithm automates the process of removing unauthorised IP addresses from an allow list. It reads the existing file, converts the data into a format that Python can manipulate, compares the addresses against a remove list, and removes any matching entries. The updated list is then converted back into a string and written to the original file. This demonstrates how Python can reduce repetitive manual security tasks and improve the consistency of access-control management.

---
