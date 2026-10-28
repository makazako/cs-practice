def winner(names, scores):
    max_score = max(scores)
    index = scores.index(max_score)
    return names[index]
def average(scores):
    if len(scores) == 0:
        return 0.0
    return round(sum(scores) / len(scores), 2)
def ranking(names, scores):
    result = []
    for i in range(len(scores)):
        result.append([scores[i], names[i]])
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[j][0] > result[i][0]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    answer = []
    for i in range(len(result)):
        answer.append(result[i][1])
    return answer
def above_average(names, scores):
    avg = average(scores)
    result = []
    for i in range(len(scores)):
        if scores[i] > avg:
            result.append(names[i])
    return result
