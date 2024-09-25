import sys
import pandas as ps

#cleans any empty strings from the list
def clean_list (clean : list) -> None:
    which = []
    for x in range(len(clean)):
        if clean[x] == '':
            which.append(x)
    count = 0
    for x in which:
        clean.pop(x - count)
        count += 1
    #print(clean)
    return None

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('not correct number of arguments')
        raise SystemExit(-1)

    weights = sys.argv[1]
    if weights == '1':
        weights = True
    else:
        weights = False
    # print(weights) #boolean

    inputword = sys.argv[2].lower()
    # print(inputword) #string

    #setup words.csv as an list of all words
    try:
        words_file = open('words.csv', 'rt')
    except FileNotFoundError:
        print('words.csv not found')
        raise SystemExit(-1)
    words = words_file.read().split('\n')
    words_file.close()
    clean_list(words)

    #setup EDweights.csv as a 2D list
    try:
        weights_file = open('EDweights.csv', 'rt')
    except FileNotFoundError:
        print('EDweights.csv not found')
        raise SystemExit(-1)
    EDweights = weights_file.read().split('\n')
    clean_list(EDweights)
    for x in range(len(EDweights)):
        EDweights[x] = EDweights[x].split(',')

