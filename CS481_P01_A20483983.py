import sys
import timeit

def del_cost (letter : str) -> int:
    return 1
    #if implementing different costs as shown in psuedocode
    if len(letter) == 1:
        return -1

def ins_cost(letter: str) -> int:
    return 1
    # if implementing different costs as shown in psuedocode
    if len(letter) == 1:
        return -1

def sub_cost (incorrect : str, correct : str, isWeighted : bool, weightTable : list) -> int:
    if incorrect == correct:
        return 0
    elif not isWeighted:
        return 2
    else:
        if not ((97 <= ord(correct) <= 122) and (97 <= ord(incorrect) <= 122)):
            return 2
        correctindex = ord(correct) - 96
        numerator = int(weightTable[ord(incorrect) - 96][correctindex])
        if numerator == 0:
            return 2
        else:
            denominator = 0
            for i in range(1, 26):
                check = int(weightTable[i][correctindex])
                if check > denominator:
                    denominator = check
            return 2 * (1 - numerator / (denominator + 1))


#miniumum edit distance
def med (incorrect : str, correct : str, isWeighted : bool, weightTable : list):
    n = len(incorrect) + 1 #x-axis
    m = len(correct) + 1 #y-axis
    disMatrix = [] #will be accessed [x][y]
    temp = []
    for i in range(m):
        temp.append(0)
    for i in range(n):
        disMatrix.append(temp.copy())
    for i in range(1, n):
        disMatrix[i][0] = disMatrix[i - 1][0] + del_cost(incorrect[i - 1])
    for i in range(1, m):
        disMatrix[0][i] = disMatrix[0][i - 1] + ins_cost(correct[i - 1])
    for i in range(1, n):
        for j in range(1, m):
            three = [
                disMatrix[i - 1][j] + del_cost(incorrect[i - 1]),
                disMatrix[i - 1][j - 1] + sub_cost(incorrect[i - 1], correct[j - 1], isWeighted, weightTable),
                disMatrix[i][j - 1] + ins_cost(correct[j - 1])
            ]
            three.sort()
            disMatrix[i][j] = three.pop(0)
    return disMatrix[n - 1][m - 1]


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
    return None

if __name__ == '__main__':
    start = timeit.default_timer()
    if not len(sys.argv) == 3:
        print('not correct number of arguments')
        raise SystemExit(-1)

    weights = sys.argv[1]
    if weights == '1':
        weights = True
    else:
        weights = False

    inputword = sys.argv[2].lower()

    #setup words.csv as a list
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

    possible = []
    lowest = -1
    for x in words:
        result = med(inputword, x.lower(), weights, EDweights)

        if result < lowest:
            possible = [x]
            lowest = result
        elif result == lowest:
            possible.append(x)
        elif lowest == -1:
            possible = [x]
            lowest = result


    end = timeit.default_timer()
    print('Prymon, Alan, A20483983 solution:\nWeights: ' + str(int(weights)) + '\nMisspelled word: ' + inputword)
    print('\nProcessing time: ' + '{0:.3f}'.format(end - start) + ' seconds')
    print('\nMinimum edit distance suggested word(s):')
    for x in possible:
        print(x)