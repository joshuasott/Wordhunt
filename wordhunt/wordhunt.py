
#graph size is M by N
M = 4
N = 4
Generate = True
Graph = {'A' : ['B','E','F'],
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

def main():
        print("hello world")
        Mapping = (create_corospondancy(Graph))
        print("mapping created")
        #findPath(Graph,'A','P')
        if Generate:
            print("pathsdefined")
            paths = (everyPath(Graph))
        else:
            print("TODO")
        file = 'FourByFourPathSheet.txt'
        #paths_to_text(paths, file)
        #print(paths)
        #words = everyWord(paths, Mapping)
        #print(word_validity(words))

def text_to_paths(file):
    with open(file, 'r') as pathssheet:
        paths = []
        for line in pathssheet:
            paths.append(line.rstrip())


def paths_to_text(paths, file):
    with open(file, 'w') as pathssheet:
        for pathset in paths:
            for path in pathset:
                pathssheet.write(f"{path}\n")

def word_validity(words):
    with open(r'dictionary.txt', 'r') as dictionary:
        valid_word_set = set(line.strip() for line in dictionary)
    return [word for word in words if word in valid_word_set]

def create_corospondancy(graph):
    global M
    global N
    LetterMapping = {}
    for width in range(M):
        while True:
            mapping = input("")
            if mapping.isalpha() is False:
                continue
            if len(mapping) != N:
                continue
            break
        for length in range(N):
            LetterMapping.update({list(graph.keys())[width*N + length]:mapping[length]})
    return (LetterMapping)



def pathToWord(path, letterMapping):
    word = ''
    for node in path:
        word = word + str(letterMapping[node])
    return word

def everyWord(paths,letterMapping):
    words = []
    for startEnd in paths:
        for path in startEnd:
            words.append(pathToWord(path, letterMapping))
    words.sort(key=len, reverse=True)
    return words


def everyPath(graph, paths=[]):
    for startNode in graph:
        for endNode in graph:
            paths = paths + [(findPath(graph, startNode, endNode))]
    return paths


def findPath(graph, start, end, length=0 ,path=None, ways=None):
    if path is None:
        path = []
    if ways is None:
        ways = []
    path = path + [start]
    if end not in graph:
        return None
    if start == end and length == 16:
        ways.append(path)
    for node in graph[start]:
        if node not in path:
            findPath(graph, node, end, length+1, path, ways)
    return ways




main()
