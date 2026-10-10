# Clean String use strip()
server = "   devops-server   "
print(server)
print(server.strip())  # Output: "devops-server"

## lower , upper use for stings

### lower()
status = input("Enter the status: ").strip().lower()
print(status)  # Output: "active" (if user input is " Active ")

### upper()
status = input("Enter the status: ").strip().upper()
print(status)  # Output: "ACTIVE" (if user input is " active ")

# Replace string use replace()
hostname = "devops-server"
new_hostname = hostname.replace("devops", "prod")
print(new_hostname)  # Output: "prod-server"

# split() use with different seperators
server_data = "web01,web02,web03,db01,db02"
print(server_data.split(","))  # Output: ['web01', 'web02', 'web03', 'db01', 'db02']

server_data1 = "web01;web02;web03;db01;db02"
print(server_data1.split(";"))  # Output: ['web01', 'web02', 'web03', 'db01', 'db02']

server_data2 = "web01|web02|web03|db01|db02"
print(server_data2.split("|"))  # Output: ['web01', 'web02', 'web03', 'db01', 'db02']

server_data3 = "web01 web02 web03 db01 db02"
print(server_data3.split())  # Output: ['web01', 'web02', 'web03', 'db01', 'db02']

server_data4 = "web01:web02:web03:db01:db02"
print(server_data4.split(":"))  # Output: ['web01', 'web02', 'web03', 'db01', 'db02']


# in operator 
log = "ERROR ngnix service failed"
print("ERROR" in log)  # Output: True
print("WARNING" in log)  # Output: False

## startswith() and endswith() use for string
log = "ERROR ngnix service failed"
print(log.startswith("ERROR"))  # Output: True
print(log.endswith("failed"))  # Output: True


# Chaining string methods
status1 = "   RUNNING   "
status1 = status1.strip().lower()
print(status1)  # Output: "running"     

##direct Method chaining
status2 = input("Enter the status: ").strip().upper()
print(status2)  # Output: "ACTIVE" (if user input is " active ")



