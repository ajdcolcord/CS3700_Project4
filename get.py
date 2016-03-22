import socket

HOSTNAME = "fring.ccs.neu.edu"
PORT = 80
RECV_MESSAGE_SIZE = 1024

def send_and_receive(message):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((HOSTNAME, PORT))

    sock.settimeout(0.2)

    sock.send(message)
    result = ""

    while True:
        try:
            recv = sock.recv(RECV_MESSAGE_SIZE)
            if recv:
                result += recv
                if recv.find("</html>") >= 0:
                    break
            else:
                break
        except:
            break

    return result


def get_by_url(url, cookie):
    get_str = "GET " + url + " HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "Connection:keep-alive\n" \
              "Cookie: " + str(cookie) + "\n" \
              "User-Agent: HTTPTool/1.1\n\n"
    return send_and_receive(get_str)


def get_login_page():
    get_str = "GET /accounts/login/?next=/fakebook/ HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "Connection:keep-alive\n" \
              "User-Agent: HTTPTool/1.1\n\n"
    return send_and_receive(get_str)


def get_first_page(cookie):
    get_str = "GET /fakebook/ HTTP/1.1\n" \
              "Host: fring.ccs.neu.edu\n" \
              "Connection:keep-alive\n" \
              "Cache-Control: max-age=0\n" \
              "Cookie: " + str(cookie) + "\n" \
              "User-Agent: HTTPTool/1.1\n\n"

    return send_and_receive(get_str)



def post_login(path_name, username, password, mwtoken):

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
                    "Accept-Language: en-US,en;q=0.8\n" \
                    "Cookie: csrftoken=" + str(mwtoken) + "\n\n" \
                    "username=" + str(username) + "&password=" + str(password) + "&csrfmiddlewaretoken=" + str(mwtoken) + "&next=%2Ffakebook%2F\n"

    return send_and_receive(post_message)
