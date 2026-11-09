# Nested IF and Logical Operators

# 1. Nested IF 
print("Nested IF :- Use of IF inside another IF called Nested IF.")
print("Example :-")

server_running = True
cpu_usage = 95

if server_running:
    print("Server is running.")

    if cpu_usage > 90:
        print("CPU CRITICAL")



# 2. Logical Operators
print("\n\n Logical Operators :- Python 3 Main Logical Operators are AND, OR, NOT.")

print("1. AND :- If both conditions are True then it will return True otherwise False.")
print("Example :- ")
cpu_usage = 70
memory_usage = 60

if cpu_usage < 80 and memory_usage < 80:
    print("Server is HEALTHY")
else:
    print("Server is UNHEALTHY")


print("\n\n2. OR :- If any one condition is True then it will return True otherwise False.")
print("Example :- ")
cpu_usage = 95
memory_usage = 60

if cpu_usage > 90 or memory_usage > 90:
    print("Server is CRITICAL")
else:
    print("Server is HEALTHY")


print("\n\n3. NOT :- It will return opposite of the condition.")
print("Example :- ")

server_running = True

if not server_running:
    print("Server is Stopped")
else:
    print("Server is running")


# 3. Practice Problem in DevOps :- Server Health Report
print("\n\nPractice Problem in DevOps :- Server Health Report")

# Suppose server is running and we have to check the health of the server based on CPU, Memory and Disk usage.
# If any of these usages are above 90% then it will be CRITICAL, if any of these usages are above 80% then it will be WARNING otherwise it will be NORMAL

server_running = True
cpu_usage = 65
memory_usage = 70
disk_usage = 60

if cpu_usage > 90 and memory_usage > 90 and disk_usage > 90:
       print("Server is CRITICAL")
elif cpu_usage > 80 and memory_usage > 80 and disk_usage > 80:
       print("Server is WARNING")
else:
    print("Server is HEALTHY")