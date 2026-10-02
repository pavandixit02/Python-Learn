# what is string?
print("String charcter ko represent karta he \n")
name = "Pankaj"
print(type(name))

## Single Quotes and Double Quotes
print("\n single quotes (' ') or double quotes (\" \"). Both are valid")
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"

# String Concatenation
print("\nConcatenation is Addition both strings together. For example:")
first_name = "Priyanshu"
last_name = "Pandit"
full_name = first_name + " " + last_name
print(full_name)  

# String Length
print("\nhow many character in string. For example:")
server = "Aritificial Intelligence"
print(len(server))    

# String Indexing
print("\ncharacter ko starting index 0 se count karta he. For example:")
server1 = "WebTech"
print(server1[0])  
print(server1[5])

# Negative Indexing
print("\nindexing start from end , oppsite of indexing.")  
server2 = "DataStructureAlgorithms"
print(server2[-1])
print(server2[-6])


# String Slicing
print("\n String ka ak partation nikalana")
server3 = "MachineLearning"
print(server3[0:4])

## Useful Slicing 
server4 = "Producation-Cloud"
print(server4[:10])
print(server4[11:])
print(server4[:])


# String Methods
print("\nMethod String ko Mainpulation / Process karne me Help karta he.")
## UPPER()
status = "running"
print(status.upper())
## lower()
status1 = "RUNNING"
print(status1.lower())

# Strip()
print("\nStrip() method use for remove extra space from string.")
server5 = "   DevOps Engineer   "
print(server5.strip())

# Replace()
print("\nReplace() method use for replace string with another string.")
server6 = "Cloud Infra Engineer"
print(server6.replace("Architecte", "DevSecOps"))

# Split()
print("\nSplit() method use for split string into list.")
server7 = "DevOps Architecte"
server_list = server7.split(",")

# Joim()
print("\nReverse Concept of Split.")
server8 = ["Fresher","Intermidiate","Expert"]
result = ",".join(server8)
print(result)

# startswith()
print("\nstartswith() method use for check string start with specific character or word.")
server9 = "DevOps Engineer"
print(server9.startswith("Dev"))

# endswith()
print("\nendswith() method use for check string end with specific character or word.")
server9 = "DevOps Engineer"
print(server9.endswith("neer"))

# find()
print("\nfind() method use for find the position of a character or word in a string.")
server7 = "DevOps Architecte"
print(server7.find("Ops"))

# in operator
print("\nUse for check specific character or word in substring.")
log = "Error: Server not found"
print("Error" in log)




