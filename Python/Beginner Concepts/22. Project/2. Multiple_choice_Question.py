question_prompts = [
    "What color are the leafs?\n(a) red/green\n(b) Yellow\n(c) Black\n\n",
    "What color is the sky?\n(a) Black\n(b) Green\n(c) Blue\n\n",
    "What color are watermelons ?\n(a) Green\n(b) Yellow\n(c) Black\n\n",
]


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question_instances = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]


def prompt(questions):
    score = 0
    for qst in questions:
        answer = input(qst.question)
        if answer is qst.answer:
            score += 1
    print("You got {}/{} correct".format(score, len(questions)))


prompt(question_instances)
