#!/usr/bin/env python3

import argparse
from random import shuffle

def LoadQuestions(file_name, question_list, answer_list):
    with open(file_name) as f:
        for line in f.readlines():
            parts = line.split('*')
            if len(parts) == 2:
                question_list.append(parts[0].strip())
                answer_list.append(parts[1].strip())

def AskAQuestion(questions, answers, questions_left):
    number_of_remaining_questions = len(questions_left)

    shuffle(questions_left)
    next_question = questions_left[number_of_remaining_questions - 1]

    answer = input('{} {} : '.format(number_of_remaining_questions, questions[next_question]))
    if(answer == answers[next_question]):
        del(questions_left[number_of_remaining_questions - 1])
    else:
        print('Wrong. The correct answer was: {}'.format(answers[next_question]))


def main():
    questions = []
    answers = []

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_name", help="name of the input file", action="store")
    parser.add_argument("-q", "--num-questions", help="number of times a single question is asked", action="store", dest="max_questions", type=int, default=3)
    args = parser.parse_args()

    LoadQuestions(args.input_file_name, questions, answers)

    questions_left = list(range(len(questions))) * args.max_questions

    while questions_left:
        AskAQuestion(questions, answers, questions_left)

main()
