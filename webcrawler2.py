import socket, sys

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the host
    try:
        s.connect((HOSTNAME, PORT))
        print "success"
    except socket.error:
        print "Failed To Connect Socket to Host"
        sys.exit(1)


if __name__ == "__main__":
    main()