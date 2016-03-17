import socket, sys

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80
RECV_MESSAGE_SIZE = 5000

LOGIN_PAGE_PATH = "/accounts/login/?next=/fakebook.html"


def get_login_page():
    return get(LOGIN_PAGE_PATH)


def get(path_name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOSTNAME, PORT))
        print "Successfully connected to: " + str(HOSTNAME) + " on port: " + str(PORT)

        sock.send("GET " + str(path_name) + "\n") #+

        return sock.recv(RECV_MESSAGE_SIZE)

    except socket.error:
        print "Failed To Connect Socket to Host"
        sys.exit(1)


print get_login_page()
