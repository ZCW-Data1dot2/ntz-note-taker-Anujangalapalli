# #!/usr/bin/python
import yaml

def readyaml():
    try:
        with open('data.yaml', 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        with open('data.yaml', 'w+'):
            return yaml.load(f, Loader=yaml.FullLoader)


def writeyaml(data):
    with open('data.yaml', 'w') as f:
        yaml.dump(data, f)

data = []
cmd = '-r'
def remember():
    with open('data.yaml', 'w') as f:
        yaml.dump(data, f)
        if cmd == '-r':
            return data.append("remember")

def create():
    with open('data.yaml', 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)
        if cmd == '-c':
            print(data.append("new list"))

def forget():
    if cmd == '-f':
        print(data.pop())

def edit():
    if cmd == '-e':
        print(data.forget())
def clear():
    if cmd == 'clear':
        print(data.clear())

remember()
create()
forget()
edit()
clear()