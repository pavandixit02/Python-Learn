
# Enter Server Details by User
server_name = input("Enter Server Name : ").strip().lower()
server_running = input("Is Server Running (True/False) : ").strip().lower()
cpu_usage = int(input("Enter CPU Usage : "))
memory_usage = int(input("Enter Memory Usage : "))
disk_usage = int(input("Enter Disk Usage : "))

# Print Server Health Report
print("\n================================")
print("      SERVER HEALTH REPORT     ")
print("================================\n")

print(f"Server Name  : {server_name.upper()}")

if server_running == "true":
    print(f"Server       : RUNNING")
else:
    print(f"Server       : STOPPED")

print(f"CPU          : {cpu_usage}% ")
print(f"Memory       : {memory_usage}% ")
print(f"Disk         : {disk_usage}% ")

if server_running == "false":
    print("\nFINAL STATUS : SERVER DOWN")
    
elif cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
        print("\nFINAL STATUS : SERVER CRITICAL")
        
elif cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
        print("\nFINAL STATUS : SERVER WARNING")
        
else:
        print("\nFINAL STATUS : SERVER HEALTHY")

print("================================")