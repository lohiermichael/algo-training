
scores_test = [100, 100, 50, 40, 40, 20, 10]
alice_test = [5, 25, 50, 120]

scores_test2 = [100, 90, 90, 80, 75, 60]
alice_test2 = [50, 65, 77, 90, 102]


def find_ranking(scores: list):
    """
    Given a score list, this function returns the ranking list
    :param scores: list with different scores ordered desc
    :return ranking: list of the ranking
    """
    ranking = [1]
    for index, score in enumerate(scores):
        if index >= 1:
            previous_score = scores[index - 1]
            previous_ranking = ranking[index - 1]
            if score == previous_score:
                ranking.append(previous_ranking)
            else:
                ranking.append(previous_ranking + 1)
    return ranking


def integrate_alice_in_scores(scores: list, a_score: int):
    """
    This function returns the index where a_score would be if integrated in scores and the list with the element,
    with a quick search method
    :param scores: list of scores without that of Alice
    :param a_score: an Alice's score
    :return i_alice: index where a_score is  in the list
    :return scores_with_alice: list with alice
    """
    # TODO complete function
    def loop(index_start, index_end):
        if index_end == index_start:
            if scores[index_start] >= a_score:
                return index_start + 1
            else:
                return index_start
        elif index_end < 0:
            return 0

        else:
            index_half = int((index_start + index_end) / 2)
            if a_score > scores[index_half]:
                return loop(index_start, index_half -1)
            elif a_score <= scores[index_half]:
                return loop(index_half + 1, index_end)

    i_alice = loop(0, len(scores) - 1)
    scores_with_alice = scores.copy()
    scores_with_alice.insert(i_alice, a_score)

    return i_alice, scores_with_alice


def climbingLeaderboard(scores: list, alice: list):
    """
    The function gives the list of the rankings of Alice's scores
    :param scores: list of other people's scores
    :param alice: list of Alice's scores
    :return alice_ranking: list of Alice's rankings
    """
    alice_ranking = []
    for a_score in alice:
        # Integrate Alice's score in scores
        i_alice, scores_with_alice = integrate_alice_in_scores(scores, a_score)

        # find ranking with Alice score
        ranking_with_alice = find_ranking(scores_with_alice)

        # Spot Alice's ranking in ranking_with_alice
        alice_ranking.append(ranking_with_alice[i_alice])
    return alice_ranking


print(climbingLeaderboard(scores_test2, alice_test2))
