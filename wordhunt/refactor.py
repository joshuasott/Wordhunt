four_by_four = {'A' : ['B','E','F'],
                'B' : ['A','C','E','F','G'],
                'C' : ['B','D','F','G','H'],
                'D' : ['C','G','H'],
                'E' : ['A','B','F','I','J'],
                'F' : ['A','B','C','E','G','I','J','K'],
                'G' : ['B','C','D','F','H','J','K','L'],
                'H' : ['C','D','G','K','L'],
                'I' : ['E','F','J','M','N'],
                'J' : ['E','F','G','I','K','M','N','O'],
                'K' : ['F','G','H','J','L','N','O','P'],
                'L' : ['G','H','K','O','P'],
                'M' : ['I','J','N'],
                'N' : ['I','J','K','M','O'],
                'O' : ['J','K','L','N','P'],
                'P' : ['K','L','O']}

two_by_two = {'A' :['B','C','D'],
              'B' :['A','C','D'],
              'C' :['A','B','D'],
              'D' :['A','B','C']}

graph = four_by_four

pathlength = 16




def main():
    coro = create_corospondancy()
    result =check('largepaths.txt','dictionary.txt',coro)
    result.sort(key=len, reverse=True)
    print(result)


def create_corospondancy():
    letters = input("Enter the letters: ").upper()

    correspondency = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for index in range(len(letters)):
        correspondency[alphabet[index]] = letters[index]

    return correspondency




def everypath(graph):
    paths =[]
    for start in graph:
        for end in graph:
            paths = paths + [findPath(graph,start,end)]
    return linklists(paths)



def tests(num):
    value = []
    for i in range(num):
        value = value + [i]
    return value


def check(path_sheet, dictionary, corospondancy):
    global pathlength
    answerlist = set()

    with open(path_sheet, 'r') as paths, open(dictionary, 'r') as valid_words:
        valid_word_set = set(line.strip() for line in valid_words)
        path_list = paths.readlines()


        for path in path_list:
            trimmed_path = path.strip()
            for i in range(pathlength):
                trimmed_path_segment = trimmed_path[:-i] if i > 0 else trimmed_path
                word = path_to_string(corospondancy, trimmed_path_segment)
                if word in valid_word_set:
                    answerlist.add(word)
        return list(answerlist)

def path_to_string(corospondancy, path):
    word = ''
    for node in path.st3rip():
        word = word + corospondancy[node]
    return word


def pathsheet_maker(paths, file):
    with open(file, 'w') as pathsheet:
        for path in paths:
            valid_path = ''.join(path)
            pathsheet.write(f"{valid_path}\n")






def linklists(list_to_link):
    main = []
    for i in list_to_link:
        main = main + i
    return main

def findPath(graph, start, end, length=0,path=None,ways =None):
    if path is None:
        path = []
    if ways is None:
        ways = []
    path = path + [start]
    if end not in graph:
        return None
    if start == end and length == 15:
        ways.append(path)
    for node in graph[start]:
        if node not in path:
            findPath(graph, node, end, length+1, path, ways)
    return ways

def FindPathBad(graph, start, end,path=None,ways =None):
    if path is None:
        path = []
    if ways is None:
        ways = []
    path = path + [start]
    if end not in graph:
        return None
    if start == end:
        ways.append(path)
    for node in graph[start]:
        if node not in path:
            FindPathBad(graph, node, end, path, ways)
    return ways

main()
