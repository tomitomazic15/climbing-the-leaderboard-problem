import math
import time
import os
import random
import re
import sys

first_question = int(input("Amount of numbers for total score:  "))
second_question = int(input("Amount of numbers for Alica score: "))

score_list = []
alica_list = []

for x in range(first_question):
    number = int(input("Enter Total Score: "))
    score_list.append(number)

for x in range(second_question):
    number2 = int(input("Enter Alica score: "))
    alica_list.append(number2)


def my_function(scores, alica):
    scores_unique = []

    for score in scores:
        if score not in scores_unique:
            scores_unique.append(score)

    empty_alica = []

    for alica_score in alica:

        found_in_leaderboard = False
        i = 0

        while i < len(scores_unique) and not found_in_leaderboard:
            if scores_unique[i] < alica_score:
                print(i + 1)
                empty_alica.append(i + 1)
                found_in_leaderboard = True

            elif scores_unique[i] == alica_score:
                print(i + 1)
                empty_alica.append(i + 1)
                found_in_leaderboard = True

            i += 1

        if not found_in_leaderboard:
            print(i + 1)
            empty_alica.append(i + 1)

    return empty_alica


my_function(score_list, alica_list)

time.sleep(1000)
