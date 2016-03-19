import socket, sys
import select

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80
RECV_MESSAGE_SIZE = 1024
USERNAME = "001196344"
PASSWORD = "7L3AD6ZH"




LOGIN_PAGE_PATH = "/accounts/login/?next=/fakebook/"

GET_LOGIN_STRING = "GET /accounts/login/?next=/fakebook/ HTTP/1.1 \nHost: fring.ccs.neu.edu\nUser-Agent: HTTPTool/1.1 \n \n"


def send_and_receive(message, sock):
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

def get_by_url(url, cookie, sock):
    get_str = "GET " + url + " HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "Connection:keep-alive\n" \
              "Cookie: " + str(cookie) + "\n" \
              "User-Agent: HTTPTool/1.1\n\n"
    return send_and_receive(get_str, sock)


def get_login_page(sock):
    get_str = "GET /accounts/login/?next=/fakebook/ HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "Connection:keep-alive\n" \
              "User-Agent: HTTPTool/1.1\n\n"
    return send_and_receive(get_str, sock)


def get_first_page(cookie, sock):
    get_str = "GET /fakebook/ HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "Connection:keep-alive\n" \
              "Cache-Control: max-age=0\n" \
              "Cookie: " + str(cookie) + "\n" \
              "User-Agent: HTTPTool/1.1\n\n"

    #"Accept-Encoding: gzip\n" \

    return send_and_receive(get_str, sock)



def post_login(path_name, username, password, mwtoken, sock):

    post_message = "POST /accounts/login/ HTTP/1.1\n" \
                    "Host: fring.ccs.neu.edu\n" \
                    "Connection: keep-alive\n" \
                    "Content-Length: 92\n" \
                    "Cache-Control: max-age=0\n" \
                    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\n" \
                    "Origin: http://fring.ccs.neu.edu\n" \
                    "Upgrade-Insecure-Requests: 1\n" \
                    "User-Agent: HTTPTool/1.1\n" \
                    "Referer: http://fring.ccs.neu.edu/accounts/login/?next=/fakebook/\n" \
                    "Accept-Encoding: gzip, deflate\n" \
                    "Accept-Language: en-US,en;q=0.8\n" \
                    "Cookie: csrftoken=" + str(mwtoken) + "\n\n" \
                    "username=" + str(username) + "&password=" + str(password) + "&csrfmiddlewaretoken=" + str(mwtoken) + "&next=%2Ffakebook%2F\n"

    return send_and_receive(post_message, sock)




#print get_login_page()
#print get_login_page()
#print post_login(LOGIN_PAGE_PATH, USERNAME, PASSWORD, 0)