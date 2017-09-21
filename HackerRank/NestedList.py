if __name__ == '__main__':
    students = list()
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students.append([name,score])

    scores = sorted(list(set([ x[1] for x in students ])))
    second_lowest = scores[1]
    second_lowest_names = [ x[0] for x in students if x[1] == second_lowest ]
    
    for x in sorted(second_lowest_names):
        print(x)
