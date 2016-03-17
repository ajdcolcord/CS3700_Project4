import socket, sys

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the host
    try:
        s.connect((HOSTNAME, PORT))
        print "Successfully connected to: " + str(HOSTNAME) + " on port: " + str(PORT)

        send_message(s)

    except socket.error:
        print "Failed To Connect Socket to Host"
        sys.exit(1)

def send_message(socket):
    socket.send("GET /fakebook.html HTTP/1.0")
    print socket.recv(1024)



if __name__ == "__main__":
    main()