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
    socket.send("GET /accounts/login/?next=/fakebook/ HTTP/1.0\n" +
                "From: acolcord@ccs.neu.edu\n" +
                "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36\n")
    print socket.recv(1024)



if __name__ == "__main__":
    main()