import random
from  questions import Question
from data import questions_data
def main():

    question = []
    for question_data in questions_data:
        new_question = question.append(Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        ))

    random.shuffle(question)

    for questions in question:
        print(questions.build_question())
        user_ans = input()
        questions.player_ans = user_ans
        if questions.is_correct():
            print(questions.build_positive_feedback())
        else:
            print(questions.build_negative_feedback())
    couter = 0
    points = 0
    for questions in question:
        if questions.is_correct():
            couter += 1
            points += questions.get_poitns()
    print()
    print("The end!")
    print(f"Correct {couter} answers from 5 answers")
    print(f"Your score is {points}")


main()

