def write_json(obj, filename):
    with open(filename, mode='w') as f:
    json.dump(obj, f)
def read_json(filename):
    with open(filename) as f:
    return json.load(f) 

if __name__ == "__main__":
    # read in input file 
    inputFile = read_json(sys.argv[1])
    dict1 = inputFile[0]
    dict2 = inputFile[1]
    
    # run Gale-Shapley calculations
    
    # write output file
