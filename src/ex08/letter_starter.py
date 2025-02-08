import sys


def get_name():
    email = sys.argv[1]
    with open("employees.tsv", 'r') as file:
        for line in file:
            if email in line:
                return line.split("\t")[0]
        else:
            print("No such email in the file")
            return None


def leter_formater():
    exit = 0
    if (len(sys.argv) == 2):
        name = get_name()
        if name != None:
            print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
    else:
        print("U need to enter only the E-mail")
if __name__ == '__main__':
    leter_formater()
