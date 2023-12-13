"""
We are going to implement a function that determines the winner of a round of Shipit.
Our function is going to look something like this:

/** * For a list of ballots, return an ordered set of candidate in descending order of their votes. */
List<String> findWinner(List<Ballot> ballots)

A voter is allowed to vote for up to three different candidates in their ballot. The order of the votes is important.
The first vote that a voter places is worth three points. The second vote is worth two points.
The third vote is worth one point.

We pass in a list of ballots and we are returned a list of names in the descending order
of the score that each candidate received.

Assume that we extract the candidates' names from the ballots as we process them.

The function should return a list of candidates in descending order of the total number of points received by the candidate.
"""


class Ballot:

    def __init__(self, choice_1, choice_2, choice_3):
        """

        :param choice_1: Gold - 3
        :param choice_2: Silver - 2
        :param choice_3: Bronze - 1
        """
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3

    def __str__(self):
        return f" {self.choice_1}, {self.choice_2}, {self.choice_3}"


def _add_score(cand_score_dict, cand_name, score):

    if cand_name is None:
        return
    else:
        if cand_name in cand_score_dict:
            two_score_tuple = cand_score_dict[cand_name]
            new_overall_score = two_score_tuple[0] + score
            new_top_score = two_score_tuple[1]
            if score == 3:
                new_top_score += 1
            cand_score_dict[cand_name] = (new_overall_score, new_top_score)
        else:
            """
            Create a tuple of 2 scores per candidate
            1. Total number of scores - 3 * Gold + 2 * Silver + 1 * Bronze
            2. Gold only score
            """
            cand_score_dict[cand_name] = (score, 0)
            if score == 3:
                cand_score_dict[cand_name] = (score, 1)


def find_winner(ballots: list[Ballot]) -> list[str]:
    """
    1. Create a dict of  <candidate to score>
    2. loop through ballots and fill up the score - linear
    3. move the dict to a list - linear
    4. sort the list by score - descending - nlogn - dominant
    5. return the candidate names alone - linear

    :param ballots:
    :return:
    """

    if ballots is None or len(ballots) == 0:
        raise ValueError("Invalid list provided as input")

    # build dict of scores
    cand_score_dict = {}
    for ballot in ballots:
        _add_score(cand_score_dict, ballot.choice_1, 3)
        _add_score(cand_score_dict, ballot.choice_2, 2)
        _add_score(cand_score_dict, ballot.choice_3, 1)

    # print(cand_score_dict)

    # convert the dict to list
    cand_score_list = []
    for e in cand_score_dict:
        cand_score_list.append({"name": e, "score": cand_score_dict[e]})

    print(cand_score_list)

    # sort the list of objects
    def _custom_comp(b):
        """
        Sort by overall medals and Gold

        Mistake commited: In a dict, b.score will not work
        b["score"] will work
        :param b:
        :return:
        """
        return -1 * b["score"][0], -1 * b["score"][1]

    sorted_list = sorted(cand_score_list, key=_custom_comp)
    print(sorted_list)

    out_list = []

    for candidate in sorted_list:
        out_list.append(candidate['name'])

    return out_list


if __name__ == "__main__":
    """
    b1 = Ballot("Xx", "Yy", "Zz")
    print(b1)

    b2 = Ballot("Aa", "Yy", "Zz")

    b3 = Ballot("Bb", "Cc", None)

    winners = find_winner([b1, b2, b3])
    print(winners)
    """
    b1 = Ballot("Xx", "Yy", "Zz")
    print(b1)

    b2 = Ballot("Aa", "Zz", None)

    winners = find_winner([b1, b2])
    print(winners)
