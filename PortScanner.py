import socket
import threading
import queue


# Ask the user to input the IP, starting port, and ending port
target_host = str(input("Enter the target host:"))
start_port = int(input("Enter starting port:"))
end_port = int(input("Enter ending port:"))

# Create the queue and put in the starting & end port
q = queue.Queue()

port_range = range(start_port, end_port)
for i in port_range:
    q.put(i)

# Check to see if starting port is less than the end port
try:
    int(start_port) < int(end_port)
except ValueError:
    print("Error: starting port is greater than end port.")


# Function to grab ports from the queue and connect to them through sockets
def port_scan():

    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((target_host, port))
                print(f"[+] Port {port}: OPEN")
            except:
                #print(f'[-] Port {port}: CLOSED')
                pass
            q.task_done()


for i in range(100):
    t = threading.Thread(target=port_scan, daemon=True)
    t.start()


q.join()
print('finished')
