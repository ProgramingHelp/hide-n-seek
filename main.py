from pywebio import *
from pywebio.input import *
from pywebio.output import *
import json

file = open("manifest.json")
json_file = json.load(file)


def main():
    id = input("enter id's of the players")
    list = id.split()
    for x in range(len(list)):
        if list[x] in json_file:
            print(f"{list[x]} is in the manifest")
    put_text(list)
    print(list)


if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
