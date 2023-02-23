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


# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
