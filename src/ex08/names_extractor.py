import sys


def extractor():
    if (len(sys.argv) == 2):
        path = sys.argv[1]
        try:
            with open(path, 'r') as file:
                emails = [line.strip() for line in file.readlines()]
            with open("employees.tsv", 'w') as export:
                export.write("Name\tSurname\tE-mail\n")
                for i in range(len(emails)):
                    export.write(
                        "\t".join([names.capitalize() for names in emails[i][:-9].split(".")])+f"\t{emails[i]}\n")
        except:
            print(f"No such file or directory: '{path}'")
    else:
        print("U only need to enter the path")


if __name__ == '__main__':
    extractor()
