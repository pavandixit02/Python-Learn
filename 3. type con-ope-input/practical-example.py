# DevOps Practical Example:-
print("\nDevOps Practical Example :")
server_name = input("Enter Server Name : ")
cpu_usage = int(input("Enter CPU Usage : "))
memory_usage = int(input("Enter Memory Usage : "))

print("=======SERVER MATRICS=======")
print(f"Server Name     : {server_name}")
print(f"CPU Usage       : {cpu_usage}%")
print(f"Memory Usage    : {memory_usage}%")

print(f"CPU Critical    : {cpu_usage>90}")
print(f"Memory Critical : {memory_usage>90}")
print("==============================")


print("\nBasic Foundation of DevOps Automation.")
print("input() -> string -> int() -> number -> Compare -> TRUE/FALSE")