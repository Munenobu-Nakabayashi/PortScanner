import socket
# import gc
import logging      # --- 2022.05.26
import os           # --- 2022.05.26

cwd = os.getcwd()

path = 'c:/Python/test/var/log/'
os.chdir(path)
# print(os.getcwd())
try:
    os.remove(f'{path}ps.log')
except:
    pass
finally:
    f = open(f'{path}ps.log', 'w')
    f.write('')

logger = logging.getLogger("00") 
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f'{path}ps.log')
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():

    host = "127.0.0.1"

    for ports in range(0,1024):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, ports))
        sock.close()

        if result == 0:
            print("Port %d is Opened." % (ports))
            logger.warning("Port %d is Opened." % (ports))
        else:
            print("Port %d is Closed." % (ports))
            logger.info("Port %d is Closed." % (ports))
        
    # print(gc.get_stats()[2])
    # gc.collect

    print('Port Scanning is Finished !')

main()

f.close()
os.chdir(cwd)
