import socket
import threading
import queue
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('target_host', type=str, help='Choose target host')
parser.add_argument('start_port', type=int, help='Starting Port')
parser.add_argument('end_port', type=int, help='Ending Port')


args = parser.parse_args()

q = queue.Queue()

port_range = range(args.start_port, args.end_port)
for i in port_range:
    q.put(i)

try:
    int(args.start_port) < int(args.end_port)
except ValueError:
    print("Error: starting port is greater than end port.")


def port_scan():

    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((args.target_host, port))
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
