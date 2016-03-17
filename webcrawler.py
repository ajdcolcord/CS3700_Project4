#!/usr/bin/python -u
import sys
import urllib2
from HTMLParser import HTMLParser

ADDRESS = "http://fring.ccs.neu.edu/accounts/login/?next=/fakebook/"

LOGIN_USERNAME = "id_username"
LOGIN_PASSWORD = "id_password"
MIDDLEWARE_TOKEN = None

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        global TOKEN
        #print("Start tag:", tag)
        #for attr in attrs:
        #    print("     attr:", attr)

        if tag == "input":
            #print tag
            #print attrs
            for attr in attrs:
                if attr[0] == "name":
                    if attr[1] == "csrfmiddlewaretoken":
                        for attr in attrs:
                            if attr[0] == "value":
                                MIDDLEWARE_TOKEN = attr[1]
                                #print MIDDLEWARE_TOKEN

                    #print attr

    """
    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    def handle_decl(self, data):
        print("Decl     :", data)

    """


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    login(username, password)



def login(username, password):
    global ADDRESS

    login_html = urllib2.urlopen(ADDRESS).read()

    parser = MyHTMLParser()

    # parse login_html for username
    parser.feed(login_html)

    parser.close()




if __name__ == "__main__":
    main()