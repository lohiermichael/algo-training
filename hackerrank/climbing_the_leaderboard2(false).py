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


def search_index_score(scores: list, a_score: int):
    """
    Research from bottom to top
    :param scores:
    :param a_score:
    :return a_score_index:
    """
    a_score_index = 0
    for index_rev, score in enumerate(reversed(scores)):
        index = len(scores) - 1 - index_rev
        if a_score <= score:
            a_score_index = index + 1

    return a_score_index


def climbingLeaderboard(scores: list, alice: list):
    """
    The function gives the list of the rankings of Alice's scores
    :param scores: list of other people's scores
    :param alice: list of Alice's scores
    :return alice_ranking: list of Alice's rankings
    """
    # Calculate ranking without Alice
    ranking = find_ranking(scores)
    print("ranking:", ranking)

    alice_ranking = []
    for a_score in alice:
        # Search from bottom to top 

        # find ranking with Alice score
        ranking_with_alice = find_ranking(scores_with_alice)

        # Spot Alice's ranking in ranking_with_alice
        alice_ranking.append(ranking_with_alice[i_alice])
    return alice_ranking


# print(climbingLeaderboard(scores_test2, alice_test2))
search_index_score(scores_test, 5)
