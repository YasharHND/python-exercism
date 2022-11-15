class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        output = []
        scores = list(self.scores)
        for _ in range(3):
            if len(scores) == 0:
                break
            top = max(scores)
            scores.remove(top)
            output.append(top)
        return output


h = HighScores([10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70])
print(h.personal_top_three())
