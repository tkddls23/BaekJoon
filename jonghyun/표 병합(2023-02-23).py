global cells
global answer


def update1(r, c, value):
    global cells

    cell = cells[r][c]
    cell["value"] = value
    for m in cell["merge"]:
        cells[m[0]][m[1]]["value"] = value


def update2(value1, value2):
    global cells

    for cell in cells:
        for c in cell:
            if c["value"] is None:
                continue
            if c["value"] == value1:
                c["value"] = value2


def merge(r1, c1, r2, c2):
    global cells

    cell1 = cells[r1][c1]
    cell2 = cells[r2][c2]

    # for m in cell1["merge"]:
    #     if r1 == m[0] and r2 == m[1] :
    #         return

    cell1["merge"].extend(cell2["merge"])
    cell1["merge"] = list(set(cell1["merge"]))
    cell2["merge"] = cell1["merge"][:]

    if cell1["value"] is None and cell2["value"] is not None:
        cell1["value"] = cell2["value"]
        for i in cell1["merge"]:
            merge_ = cell1["merge"][:]
            i = cells[i[0]][i[1]]
            i["merge"] = merge_
            i["value"] = cell1["value"]
    else:
        cell2["value"] = cell1["value"]
        for i in cell1["merge"]:
            merge_ = cell1["merge"][:]
            i = cells[i[0]][i[1]]
            i["merge"] = merge_
            i["value"] = cell1["value"]


def unmerge(r, c):
    global cells
    target_cell = cells[r][c]
    for index in target_cell["merge"]:
        if index[0] == r and index[1] == c:
            continue
        cell = cells[index[0]][index[1]]
        cell["value"] = None
        cell["merge"] = [(index[0], index[1])]
    target_cell["merge"] = [(r, c)]


def printCell(r, c):
    global cells
    global answer
    if cells[r][c]["value"] is not None:
        answer.append(cells[r][c]["value"])
    else:
        answer.append("EMPTY")


def command_run(param):
    param_split = param.split()
    command = param_split[0]
    if command == "UPDATE":
        if len(param_split) == 4:
            update1(int(param_split[1]), int(param_split[2]), param_split[3])
        else:
            update2(param_split[1], param_split[2])
    if command == "MERGE":
        merge(int(param_split[1]), int(param_split[2]), int(param_split[3]), int(param_split[4]))
    if command == "UNMERGE":
        unmerge(int(param_split[1]), int(param_split[2]))
    if command == "PRINT":
        printCell(int(param_split[1]), int(param_split[2]))


def solution(commands):
    global cells
    global answer
    answer = []
    i = 55
    cells = [[{
        "value": None,
        "merge": [(int(a), int(b))]
    } for b in range(i)] for a in range(i)]
    for command in commands:
        command_run(command)

    # for cell in cells :
    #     print(cell)

    return answer