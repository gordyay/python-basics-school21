def write_tsv():
    with open("ds.csv", "r") as file:
        content = file.readlines()
    with open ("ds.tsv", "w") as efile:
        quot=1
        for i in range(len(content)):
            line=""
            for char in content[i]:
                if (quot == 1 and char == "\""):
                     quot=0
                if (char == "," and quot == 0):
                    line+="\t"
                else:
                    line+=char
            efile.write(line)


if __name__ == '__main__':
    write_tsv()
