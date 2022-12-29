class Question:
    def __init__(self, qu_text, qu_difficulty, qu_answer):
        self.qu_text = qu_text
        self.qu_difficulty = qu_difficulty
        self.qu_answer = qu_answer

        self.is_asked = False
        self.player_ans = None
        self.score = qu_difficulty * 10

    def get_poitns(self):

        return self.score

    def is_correct(self):
        if self.player_ans == self.qu_answer:
            return True
        else:
            return False

    def build_question(self):
        answer = f"\nQuestion: {self.qu_text}\nDifficulty is: {self.qu_difficulty}/5"
        return answer

    def build_positive_feedback(self):
        answer = f"The answer is true. Claimed {self.score} points"
        return answer

    def build_negative_feedback(self):
        answer = f"The answer is false. True answer is {self.qu_answer}"
        return answer

    def __repr__(self):
        return f"{self.qu_text} - {self.qu_answer} ({self.qu_difficulty}/5)"

