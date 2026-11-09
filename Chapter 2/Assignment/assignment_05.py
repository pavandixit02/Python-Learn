server_input = input("Enter Server Name   : ")
cpu_usage = int(input("Enter CPU Usage     : "))
memory_usage = int(input("Enter Memory Usage  : "))
disk_usage = int(input("Enter Disk Usage    : "))

print("\n\nSEVER HEALTH REPORT\n")
print(f"\nServer Name    : {server_input.upper()}")

# Display CPU Status
if cpu_usage > 90:
    print(f"CPU Status     : CRITICAL")
elif cpu_usage >= 80:
    print(f"CPU Status     : WARNING")
else:
    print(f"CPU Status     : NORMAL")

# Display Memory Status
if memory_usage > 90:
    print(f"Memory Status  : CRITICAL")
elif memory_usage >= 80:
    print(f"Memory Status  : WARNING")
else:
    print(f"Memory Status  : NORMAL")

# Display Disk Status
if disk_usage > 90:
    print(f"Disk Status    : CRITICAL")
elif disk_usage >= 80:
    print(f"Disk Status    : WARNING")
else:
    print(f"Disk Status    : NORMAL")

