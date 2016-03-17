import socket, sys

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80
RECV_MESSAGE_SIZE = 5000

LOGIN_PAGE_PATH = "/accounts/login/?next=/fakebook.html"


def get_login_page():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the host
    try:
        sock.connect((HOSTNAME, PORT))
        print "Successfully connected to: " + str(HOSTNAME) + " on port: " + str(PORT)

        sock.send("GET " + str(LOGIN_PAGE_PATH) + "\n") #+
                #"From: acolcord@ccs.neu.edu\n" +
                #"User-Agent: HTTPTool/1.0\n")

        return sock.recv(RECV_MESSAGE_SIZE)

    except socket.error:
        print "Failed To Connect Socket to Host"
        sys.exit(1)


print get_login_page()
