from pulp import LpProblem, LpVariable, lpSum, LpBinary, LpStatus


def solve_partition(case_id, panels):
#while True:
            
    # total_sum = sum(panels)
        # if total_sum % 2 != 0:
        #     return f"Case #{case_id}: IMPOSSIBLE"

    # target_sum = total_sum
    n = len(panels)

        # Creazione del problema di ottimizzazione
    prob = LpProblem("Partition", sense=1)

        # Variabili binarie per assegnare i pannelli al primo gruppo
    x = [LpVariable(f"x_{i}", cat=LpBinary) for i in range(n)]

        # Vincolo: la somma dei pannelli assegnati al primo gruppo deve essere target_sum
    # prob += lpSum([panels[i] * x[i] for i in range(n)]) == target_sum
    while True:
        # Risoluzione del problema
        status = prob.solve()
        #print(x.varValue)
        print(panels)
        if status != 1:
            break
        
        prob += x != panels
       # problem += x != 
      #  print(panels)
        # if LpStatus[prob.status] == "Optimal":
        #     group1 = [panels[i] for i in range(n) if x[i].varValue == 1]
        #     group2 = [panels[i] for i in range(n) if x[i].varValue == 0]
        #     # group2 = [panels[i] for i in range(n) if x[i].varValue == 0]

        #     return (
        #         f"Case #{case_id}:\n{len(group1)} "
        #         + " ".join(map(str, group1))
        #         + "\n"
        #         + f"{len(group2)} "
        #         + " ".join(map(str, group2))
        #     )
        # else:
        #     return f"Case #{case_id}: IMPOSSIBLE"
    return ""


# Lettura input
# def process_input(input_text):
#     lines = input_text.strip().split("\n")
#     C = int(lines[0])
#     output = []
#     index = 1

#     for case_id in range(1, C + 1):
#         N = int(lines[index])
#         panels = list(map(int, lines[index + 1].split()))
#         output.append(solve_partition(case_id, panels))
#         index += 2
#     return "\n".join(output)


def read_file(path):
    with open(path) as file:
        test = int(file.readline())
        d = {}
        for i in range(test):
            panels = int(file.readline())
            line = file.readline()
            d.update({i + 1: [int(e) for e in line.split()]})
    return d


FILE_PATH = "./input.txt"

data = read_file(FILE_PATH)


out = ""
for k, v in data.items():
    out += solve_partition(k, v) + "\n"

with open("./outpu.txt", "w") as file:
    file.write(out)
