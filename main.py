from pywebio import *
from pywebio.input import *
from pywebio.output import *

def main():
    id = input("enter id's of the players")
    list = id.split()
    put_text(list)
    print(list)


if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
