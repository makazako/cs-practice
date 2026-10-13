def winner(names, scores):
    winner = names.index(max(scores)) + 1
    return winner
def average(names, scores):
    averege = 0
    if len(scores) > 0:
        avarage = sum(scores) / len(scores)
    return average
def ranking(names, scores):
    ranking = []
    for el in range(len(scores) - 1):
        m = max(scores)
        ranking.append(names(scores.index(m)))
    return ranking
def above_average(names, scores):
    above_averege = [names[scores.index(x)] for x in scores if x > average ]
    return above_average
