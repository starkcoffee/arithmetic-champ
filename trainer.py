from sys import argv
from time import time 
from random import randint
from statistics import mean
from contextlib import contextmanager
from datetime import date
import random

TOLERANCE = 0.05
CELEBRATE_EMOJIS = ['🥳','🐝','🌟'] 

class Results:
  def __init__(self):
    self.results = []
  def append(self, time_s, success):
    self.results.append((time_s, success))
  def mean_completion_time_s(self):
    return round(mean([ t[0] for t in self.results ]), 2)
  def success_rate(self): 
    return round([ t[1] for t in self.results].count(True) / len(self.results) * 100)
  def count(self):
    return len(self.results)

def main():
  
  results = Results()

  for i in range(int(argv[1])):

    challenge_str, true_value, tolerance = generate_challenge()

    task = lambda: float(input(prompt(challenge_str))) 
    time, answer = time_task_in_seconds(task)
    close_enough = is_close_enough(answer, true_value, tolerance)
    results.append(time, close_enough)

    print(compose_response(close_enough, true_value))

  print(f"Avg completion time: {results.mean_completion_time_s()}s")
  print(f"Success rate: was {results.success_rate()}%")

  with open('arithemtic-training-results.csv', 'a') as report_file:
    isodate = date.today().isoformat()
    report_file.write(f"{isodate},{results.count()},{results.mean_completion_time_s()},{results.success_rate()}\n")

# returns (challenge_str, true_value, tolerance)
def generate_challenge():
  numerator = generate_numerator()
  denominator = randint(6, 100)
  return f"{numerator}/{denominator}", numerator/denominator, TOLERANCE

def generate_numerator():
  return (randint(100,10000)//100)*100

def prompt(challenge):
  return f"What is {challenge} ?\n"

# returns (completion_time_seconds, task_return_val)
def time_task_in_seconds(task):
  start = time()
  task_return_val = task()
  stop = time()
  return round(stop - start), task_return_val

def is_close_enough(answer, true_value, tolerance):
  return abs(answer - true_value) <= tolerance * true_value

def compose_response(was_close_enough, true_value):
  response = "\n"

  if was_close_enough:
    emoji = random.choice(CELEBRATE_EMOJIS)
    response += f"Yeh good job!{emoji}\n"
  else:
    response += "Nah\n"
  response += f'Answer is {true_value}\n'

  return response

if __name__ == '__main__':
  main()
