def fit_evaluate(puzzle,layers):
    fitness =0
    k=0
    if (puzzle[0][2]!=puzzle[2][2]):
        fitness += 10
    for i in range(1,layers):
        for j in range(0,i*2+1):
            k+=1
            if(puzzle[k].count('0')==2): ## corner
                if(j == 0):
                    if (puzzle[k][1]!=puzzle[k+1][1]):
                        fitness += 10

                    #k=k+1
                else:
                    #k=k+1
                    if (puzzle[k][0]!=puzzle[k-1][0]):
                        fitness += 10

            elif(puzzle[k].count('0')==1):
                if(puzzle[k][0]=='0'):
                    if (puzzle[k][1]!=puzzle[k+1][1]):
                        fitness += 10
                    if (puzzle[k][2]!=puzzle[k+(i+1)*2][2]):
                        fitness += 10
                    #k=k+1

                elif(puzzle[k][2])=='0':
                    if (puzzle[k][0]!=puzzle[k-1][0]):
                        fitness += 10
                    if (puzzle[k][1]!=puzzle[k+1][1]):
                        fitness += 10

                else:
                    if (puzzle[k][0]!=puzzle[k-1][0]):
                        fitness += 10
                    if (puzzle[k][2]!=puzzle[k+(i+1)*2][2]):
                        fitness += 10

            else:
                if(j%2!=0):
                    if (puzzle[k][2]!=puzzle[k-(i)*2][2]):
                        fitness += 10
                    if (puzzle[k][0]!=puzzle[k+1][0]):
                        fitness += 10
                    if (puzzle[k][1]!=puzzle[k-1][1]):
                        fitness += 10
                else:
                    if (puzzle[k][2]!=puzzle[k+(i+1)*2][2]):
                        fitness += 10
                    if (puzzle[k][1]!=puzzle[k+1][1]):
                        fitness += 10
                    if (puzzle[k][0]!=puzzle[k-1][0]):
                        fitness += 10

    #print(fitness)
    return fitness
