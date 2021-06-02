def latest(scores: list):
    return scores[-1]

def personal_best(scores: list):
    scores.sort()
    return latest(scores)

def personal_top_three(scores: list):
    scores.sort(reverse=True)
    return scores[:3]
