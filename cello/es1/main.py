def read_file(path):
    with open(path) as file:
        test = int(file.readline())
        d = {}
        for i in range(test):
            eleg_logs = int(file.readline())
            d.update({i + 1: [file.readline().rstrip() for _ in range(eleg_logs)]})

    return d


def clean(e, l):
    return [el for el in l if e not in el or el == e]


def filter_list(l):
    print(l)

    i = 0
    while i < len(l):
        l = clean(l[i], l)
        i += 1

    print(l)

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


PATH_FILE = "./input.txt"
logs = read_file(PATH_FILE)

filter_valid(logs)

print_output(logs)
