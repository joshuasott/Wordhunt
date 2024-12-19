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


coro = {'A':'N',
        'B':'A',
        'C':'E',
        'D':'T',
        'E':'N',
        'F':'Y',
        'G':'S',
        'H':'I',
        'I':'I',
        'J':'P',
        'K':'A',
        'L':'C',
        'M':'C',
        'N':'U',
        'O':'H',
        'P':'T'}



graph = four_by_four


def main():
    with open("dictionary.txt", 'r') as dictionary:
        words = []
        valid_word_set = set(line.strip() for line in dictionary)
        for start in graph:
            words.append(checks(start,graph, coro,valid_word_set))



def checks(start, graph, corospondancy, words:set, valid_words=None, path=None):
    #Initialization
    if valid_words is None:
        valid_words = []
    if path is None:
        path = []
    if start in path:
        return

    path = path + [start]
    #check if the word so far is the start of any valid word
    substatuted_path = path_to_string(corospondancy, path)
    if not any(word.startswith(substatuted_path) for word in words):
        return

    #if the path is a valid word
    if substatuted_path in words:
        valid_words.append(substatuted_path)

    #Depth First Search
    for node in graph[start]:
        checks(node, graph, corospondancy, words, valid_words, path)

    return valid_words


def path_to_string(corospondancy, path):
    word = ''
    for node in path:
        word += corospondancy.get(node, '')
    return word



main()
