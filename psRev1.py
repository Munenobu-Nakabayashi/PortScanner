import socket
import gc

def main():

    host = "127.0.0.1"

    for ports in range(0,1023):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, ports))
        sock.close()

        if result == 0:
            print("Port %d is Opened." % (ports))
        else:
            print("Port %d is Closed." % (ports))
        
    print(gc.get_stats()[2])
    gc.collect

    print('Port Scanning is Finished ! ')

main()