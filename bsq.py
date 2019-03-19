import sys
import string
Class Bsq()
    def parse():
        with open(sys.argv[1], "r") as f:
            start_verif = f.readline()
            nblines = [i for i in start_verif if i.isdigit()]
            num = "".join(nblines)
            valids = [i for i in start_verif if i.isdigit() is False]
            # print(f)
            map = [[y for y in line] for line in f]
            for elem in f:
                for box in elem:
                    if box != valids[0] and box != valids[1] and box != valids[3]:
                        print("Bad map !")
                        return False
            return map

    def bsq(map):
        map = parse()
        for y, line in enumerate(map):
            print("y : ")
            print(y)
            print("line : ")
            print(line)
            for x, char in enumerate(line):
                print("x : ")
                print(x)
                if char == parse().valids[0] and line[x * x + 1] != parse().valids[1]:
                    line[x] = parse().valids[2]
        
        print("lol")

print(bsq(parse()))