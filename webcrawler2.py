import socket, sys

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80

LOGIN_PAGE_PATH = "/accounts/login/?next=/fakebook.html"

def main():


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the host
    try:
        s.connect((HOSTNAME, PORT))
        print "Successfully connected to: " + str(HOSTNAME) + " on port: " + str(PORT)

        get_login_page(s)

    except socket.error:
        print "Failed To Connect Socket to Host"
        sys.exit(1)


def get_login_page(socket):
    recv_buffer=""
    socket.send("GET " + str(LOGIN_PAGE_PATH) + "\n") #+
                #"From: acolcord@ccs.neu.edu\n" +
                #"User-Agent: HTTPTool/1.0\n")

    print socket.recv(5000)



if __name__ == "__main__":
    main()