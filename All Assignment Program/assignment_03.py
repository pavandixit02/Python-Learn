server_name = input("Enter Server Name : ")
cpu_usage = int(input("Enter CPU Usage : "))
memory_usage = int(input("Enter Memory Usage : "))
disk_usage = int(input("Enter Disk Usage : "))

print("=============================")
print(" SERVER MATRICS ")
print("=============================")
print(f"Server Name     : {server_name}")
print(f"CPU Usage       : {cpu_usage}%")
print(f"Memory Usage    : {memory_usage}%")
print(f"Disk Usage      : {disk_usage}%")

print(f"\nCPU Critical    : {cpu_usage>90}")
print(f"Memory Critical : {memory_usage>90}")
print(f"Disk Critical   : {disk_usage>90}")

print("=============================")