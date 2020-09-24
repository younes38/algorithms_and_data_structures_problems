# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_a = 0
    score_b = 0
    for i in range(3):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
        
    return score_a, score_b
