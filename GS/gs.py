import json
import sys
import time


def read_json(filename):
    with open(sys.argv[1]) as json_file:
        return json.load(json_file)

def write_json(obj, filename):
    with open(filename, mode='w') as json_file:
        json.dump(obj, json_file)

def galeShapely(dict1, dict2):
    freeMen = []; freeWomen = []
    matches = {}  # pairs
    for key in dict1:
        freeMen.append(key)
    for key in dict2:
        freeWomen.append(key)

    while (len(freeMen) != 0):
        man = freeMen[0]
        mPrefList = dict1[man]  # list of first dictionary?

        for i in mPrefList:
            woman = i
            if woman in freeWomen:  # if she's not taken
                freeWomen.remove(woman)
                freeMen.remove(man)
                matches[woman] = man
                break
            else:  # if she's taken
                currMan = matches.get(woman)
                wPrefList = dict2[woman]
                if (wPrefList.index(man) > wPrefList.index(currMan)):  #if she likes the new man better
                    freeMen.remove(man)
                    matches[woman] = man
                    freeMen.append(currMan)
                    break
    return matches


if __name__ == "__main__":
    # read in input file
    inputFile = read_json(sys.argv[1])

    start_time = time.process_time()
    for i in range(0, len(inputFile)):
        dict1 = inputFile[i][0]
        dict2 = inputFile[i][1]
        matches = galeShapely(dict1, dict2)
        print (matches)
    
    # write output file
