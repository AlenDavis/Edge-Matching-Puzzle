import csv
import random
import math
import fit_eval
import puzzle_generate
import triangle_rotation as t_rot
import tournament_selection as s
#import cross_over_v02 as cxr
import region_cross_over as cxr
import mutate_v02
#import imp_fit_fitter_v02
import draw_puzzle_v01 as pd
import time
#######################
start_time = time.time()
#global variable

def get_color():
    inp_file = open("Untitled 1.csv")
    reader = csv.reader(inp_file,delimiter=',')
    for row in reader:
        color.append(row)

## insitialization
class individuals:
    def __init__(self):
        self.corners,self.sides,self.inner= init_individuals()
        self.fitness = -1

def init_individuals():
    postion = []

    pos = 0
    c_0_2 = []
    c_0_1 = []
    c_0_0 = []
    for i in color:
        if i.count('0') == 2:
            c_0_2.append(i)
        elif i.count('0') == 1:
            c_0_1.append(i)
        else:
            c_0_0.append(i)

    corners = []
    sides   = []
    inner   = []
#filling corners
    for i in range(0,3):
        place = random.choice(c_0_2)
        c_0_2.remove(place)

        if i == 0:
            if place[0] != '0':
                place = t_rot.rotate(place,2)
            elif place[1] != '0':
                place = t_rot.rotate(place,1)

        elif i == 1:
            if place[2] != '0':
                place = t_rot.rotate(place,2)
            elif place[0] != '0':
                place = t_rot.rotate(place,1)

        else:
            if place[1] != '0':
                place = t_rot.rotate(place,2)
            elif place[2] != '0':
                place = t_rot.rotate(place,1)
        corners.append(place)


    s1=(layers-2)
    s2=s1*2
    s3=s2*2

    for i in range(0,len(c_0_1)):
        place = random.choice(c_0_1)
        c_0_1.remove(place)

        if i<(s1):
            if place[1] == '0':
                place = t_rot.rotate(place,2)
            elif place[2] == '0':
                place = t_rot.rotate(place,1)

        elif i<s2:
            if place[0] == '0':
                place = t_rot.rotate(place,2)
            elif place[1] == '0':
                place = t_rot.rotate(place,1)


        else:
            if place[2] == '0':
                place = t_rot.rotate(place,2)
            elif place[0] == '0':
                place = t_rot.rotate(place,1)

        sides.append(place)

    for i in range(0,len(c_0_0)):
        place = random.choice(c_0_0)
        c_0_0.remove(place)
        if(random.uniform(0,1)>0.6):
            if(random.uniform(0,1)>0.5):
                place=t_rot.rotate(place,1)
            else:
                place=t_rot.rotate(place,2)
        inner.append(place)

    return corners,sides,inner

def calculate_fitness_score(pop):
    for p in pop:
        puzzle = puzzle_generate.puzzle_gen(p.corners,p.sides,p.inner,layers)
        p.fitness = fit_eval.fit_evaluate(puzzle,layers)

    return pop

def variation(parents):
    offsprings = []

    while (len(parents)>0):
        child1 = individuals()
        child2 = individuals()
        p1 = random.choice(parents)
        parents.remove(p1)
        p2 = random.choice(parents)
        parents.remove(p2)

        if (random.uniform(0,1)>0.4):


            child1.corners,child1.sides,child1.inner, \
            child2.corners,child2.sides,child2.inner \
            = cxr.cross(p1.corners,p1.sides,p1.inner, \
                p2.corners[:],p2.sides[:],p2.inner[:],color,layers)

            #exit()
            child1.corners,child1.sides,child1.inner  \
                = mutate_v02.swap_mutation(child1.corners[:],child1.sides[:],child1.inner[:],color,layers)

            child2.corners,child2.sides,child2.inner  \
            = mutate_v02.swap_mutation(child2.corners[:],child2.sides[:],child2.inner[:],color[:],layers)


            offsprings.append(child1)
            offsprings.append(child2)
    return offsprings

def survivor_selection(population,offsprings):
    for i in offsprings:
        flag=0
        for j in population:
            if (i.corners == j.corners and \
                i.sides == j.sides and \
                i.inner == j.inner) :
                flag = 1
                break
        if flag == 0:
            population.append(i)
    population = sorted(population, key=lambda individual: individual.fitness, reverse=False)

    population = population[0:100]
    return population

color  = []
layers = 0
generation = 100000
get_color()
layers = int(math.sqrt(len(color)))

population = [individuals() for i in range(0,100)]
population = calculate_fitness_score(population)

population = sorted(population, key=lambda individual: individual.fitness, reverse=False)
print("Gen1")
best_gen_fitness=[]
best_gen_count=[]
for i in population:
#    print (i.fitness)
    best_gen_count.append(0)
    best_gen_fitness.append(i.fitness)
gen = 0
#for gen in range(0,generation):
while(True):
    gen+=1
    fit = [individual.fitness for individual in population]
    select =  s.selection(fit)
    parents = [population[i] for i in select]
    offsprings = variation(parents)
    offsprings = calculate_fitness_score(offsprings)
    offsprings = sorted(offsprings, key=lambda individual: individual.fitness, reverse=False)
    population=survivor_selection(population,offsprings)

    if population[0].fitness <= 0:
        print ("Generation ",gen)
        for j in population:
            print (j.fitness)
        print "Threshold readched"
        break

print("--- %s seconds ---" % (time.time() - start_time))
p=population[0]
puzzle = puzzle_generate.puzzle_gen(p.corners,p.sides,p.inner,layers)
print puzzle
pd.draw_puzzle(puzzle,layers)
