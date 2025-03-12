# import re


def read_file(path):
    with open(path) as file:
        test = int(file.readline())
        d = {}
        for i in range(test):
            eleg_logs = int(file.readline())
            d.update({i + 1: [file.readline().rstrip() for _ in range(eleg_logs)]})

    return d


def filter_list(l):
    try:
        for i in range(len(l)):
            print(l)
            l = [e for e in l if l[i] not in e]
            print(l)
        return l
    except:
        return l


def filter_valid(d):
    for k, v in d.items():
        d[k] = filter_list(v)


def print_output(d):
    with open("./output.txt", "w") as file:
        for k, v in d.items():
            file.write(f"Case #{k}: {len(v)}")
            for e in v:
                file.write(f" {e}")
            file.write("\n")
        

PATH_FILE = "./reply1.txt"
logs = read_file(PATH_FILE)

filter_valid(logs)

print_output(logs)