#!/usr/bin/python3
'''
It takes in URL, sends request to URL and displays -
body of response (decoded in utf-8)
--manage urllib.error.HTTPError exceptions and print: Error code
'''


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
