# Task 01
print("Task 01 :- Print numbers from 1 to 10 using for loop.\n")
for i in range(1, 11):
    print(i)

# Task 02
print("\nTask 02 :- Print even numbers from 2 to 20 using for loop.\n")
for i in range(2, 21, 2):
    print(i)

# Task 03
print("\nTask 03 :- Create a list of servers and print each server.\n")
servers = ["web01", "web02", "db01", "app01", "nginx01"]
for server in servers:
    print(f"Checking Server : {server}")

# Task 04
print("\nTask 04 :- Create a list of servers and print each server with its index using enumerate.\n")
print("\n===== SERVER INVENTORY =====\n")
for index, server in enumerate(servers, start=1):
    print(f"{index}. {server}")


# Task 05
print("\nTask 05 :- Print the total number of servers in the list.\n")
print(f"Total Servers : ", len(servers))
