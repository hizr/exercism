def latest(scores: list):
    return scores[-1]

def personal_best(scores: list):
    return personal_top_three(scores)[0]

def personal_top_three(scores: list):
    result = list(scores)
    result.sort(reverse=True)
    return result[:3]
