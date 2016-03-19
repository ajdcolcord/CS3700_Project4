import socket, sys
import select

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80
RECV_MESSAGE_SIZE = 1024
USERNAME = "001196344"
PASSWORD = "7L3AD6ZH"


LOGIN_PAGE_PATH = "/accounts/login/?next=/fakebook/"

GET_LOGIN_STRING = "GET /accounts/login/?next=/fakebook/ HTTP/1.1 \nHost: fring.ccs.neu.edu\nUser-Agent: HTTPTool/1.1 \n \n"


def send_and_receive(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOSTNAME, PORT))
        sock.send(message)
        result = ""
        while True:
            recv = sock.recv(RECV_MESSAGE_SIZE)
            if recv:
                result += recv
            else:
                break
        return result
    except socket.error:
        print "Could not connect to host" + str(HOSTNAME)
        sys.exit(1)


def get_login_page():
    get_str = "GET /accounts/login/?next=/fakebook/ HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "User-Agent: HTTPTool/1.1\n\n"
    return send_and_receive(get_str)


def post_login(path_name, username, password, mwtoken):

    post_message = "POST " + str(path_name) + " HTTP/1.0 \n" \
                                         "Content-Type: application/x-www-form-urlencoded\n\n" \
                                         "username=" + str(username) + "&password=" + str(password) + \
                                         "&csrfmiddlewaretoken=" + str(mwtoken) + "&next=/fakebook/"

    return send_and_receive(post_message)



#print get_login_page()
#print get_login_page()
#print post_login(LOGIN_PAGE_PATH, USERNAME, PASSWORD, 0)