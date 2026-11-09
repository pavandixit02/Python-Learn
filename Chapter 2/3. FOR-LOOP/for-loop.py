# Loop Introducation
print("LOOP :- When same task excuted repeatedly.")
print("FOR LOOP :- When we know how many times we want to excute the task.")
print("Example :-")
for i in range(5):
    print(f"Server")

## Range Function
print("\nRange Function :- Range function is used to generate a sequence of numbers.")
print("Example :-")
for i in range(8):
    print(i)

print("\nExample-1 :-")
for i in range(1, 11):
    print(i)

print("\nExample-2 :-")
for i in range(2, 11, 2):
    print(i)

###Parameter in Range :-
print("\nParameter in Range :- Range function can take 3 parameters start, stop and step.")
print("Syntax :- range(start, stop, step)")
print("start :- Starting Numeber. Default is 0.")
print("stop :- Ending Number. Default is 0.")
print("step :- Increment | Decrement. Default is 1.")


# DevOps Multiple Server :-
print("\nDevOps Multiple server :-")

servers = ["web01", "db01", "app01", "web02", "db02", "app02"] 
for server in servers:
    print(f"Checking Server : {server}") 


# Enumerate Function () :-  
print("\nEnumerate Function () :- Enumerate function is used to get the index of the element in the list.")
servers = ["web01", "db01", "app01"]
for index, server in enumerate(servers,start=1):
    print(f"Checking Server : {server} at index : {index}")