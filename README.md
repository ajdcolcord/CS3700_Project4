Austin Colcord and Nick Scheuring

This is the project for creating a web crawler.

High-Level Approach:
First, our program creates an HTTP 1.1 GET request for the login page to
the fakebook website (on fring.ccs.neu.edu) using port 80. Once the response
has come back, we parse through the HTML in the response, looking for the
unique randomized CSRF token needed for verification to login to the website.
This token is then stored and used to create a POST request to login to the
website. Once logged in, our crawler stores the session ID and creates a
cookie to send out (containing the previously-found CSRF token) and starts
crawling the website, searching for any secret flags on each page. We use a
'Frontier' dictionary to store which URLs are found to search, setting their
values to True once they ahve been searched for the secret flags. Once 5
unique secret flags have been found, the system prints them out and closes.


Issues:
Not too many issues were encountered, except for figuring out how to formulate
proper requests and optimizing different parts of the program to improve
performance.

Testing:
Multiple runs through the crawler, using the developer tools in Google Chrome,
and playing around with different socket timeouts in order to figure out which
pieces of our program was breaking helped test our program.