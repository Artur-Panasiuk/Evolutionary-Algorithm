import numpy as np
import random
import copy

N = 8
POP = 100
GENMAX = 1000
PC = 0.7
PM = 0.2

def evaluate(P):
    attacks = np.zeros(len(P))
    n = len(P[0])
    
    for i, unit in enumerate(P):
        for j in range(n):
            for k in range(j+1, n):
                if unit[j] == unit[k] or abs(unit[j] - unit[k]) == abs(j - k):
                    attacks[i] += 1
    
    return attacks

def selection(P, tournamentPool = 5):
    newPopArr = []

    while len(newPopArr) < len(P):
        pool = np.empty((tournamentPool, N))
        for i in range(tournamentPool):
            random_row = np.random.choice(len(P))
            pool[i] = P[random_row]
        poolScore = evaluate(pool)
        poolBest = np.argmin(poolScore)
        newPopArr.append(pool[poolBest])

    return np.array(newPopArr)

def crossover(P):
    i = 0
    Pcopy = copy.deepcopy(P)
    while i < POP - 2:
        if random.random() <= PC:
            temp = Pcopy[i]
            Pcopy[i] = P[i+1]
            Pcopy[i+1] = temp
            i = i + 2

    return Pcopy

def mutation(P):
    i = 0
    Pcopy = copy.deepcopy(P)
    while i < POP:
        if random.random() <= PM:
            Pcopy[i] = np.random.randint(1, N+1, N)
            i = i + 1

    return Pcopy

def evolutionary_algorithm():
    popArr = np.random.randint(1, N+1, size=(POP, N))
    score = evaluate(popArr)
    best = np.argmin(score)

    print(f'0 - {popArr[best]}: {score[best]}')

    gen = 0
    ffMax = 0

    outputArr = popArr[best]
    outputScore = score[best]

    while (gen < GENMAX) and outputScore != ffMax:
        selectioned = selection(popArr)
        crossed = crossover(selectioned)
        mutated = mutation(crossed)

        localScore = evaluate(mutated)
        localBest = np.argmin(localScore)
        popArr = mutated

        if(localScore[localBest] < outputScore):
            outputArr = popArr[localBest]
            outputScore = localScore[localBest]

        gen = gen + 1

        print(f'{gen} - {popArr[localBest]}: {localScore[localBest]}')

    return outputArr, outputScore

result, score = evolutionary_algorithm()

print(result)
print(score)



