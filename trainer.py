from sys import argv
from time import time 
from random import randint
from statistics import mean
from contextlib import contextmanager

TOLERANCE = 0.05

def main():
  
  completion_times_in_seconds = []

  for i in range(int(argv[1])):

    challenge_str, true_value, tolerance = generate_challenge()

    task = lambda: float(input(prompt(challenge_str))) 
    time, answer = time_task_in_seconds(task)
    completion_times_in_seconds.append(time)

    close_enough = is_close_enough(answer, true_value, tolerance)
    print(compose_response(close_enough, true_value))

  mean_completion_time_s = round(mean(completion_times_in_seconds),2)
  print(f"Avg completion time was {mean_completion_time_s}")

# returns (completion_time_seconds, task_return_val)
def time_task_in_seconds(task):
  start = time()
  task_return_val = task()
  stop = time()
  return round(stop - start), task_return_val

def prompt(challenge):
  return f"What is {challenge} ?\n"

def generate_numerator():
  return (randint(100,10000)//100)*100

# returns (challenge_str, true_value, tolerance)
def generate_challenge():
  numerator = generate_numerator()
  denominator = randint(6, 100)
  return f"{numerator}/{denominator}", numerator/denominator, TOLERANCE

def is_close_enough(answer, true_value, tolerance):
  return abs(answer - true_value) <= tolerance * true_value

def compose_response(was_close_enough, true_value):
  response = "\n"

  if was_close_enough:
    response += "Yeh good job!🥳\n"
  else:
    response += "Nah\n"
  response += f'Answer is {true_value}\n'

  return response

if __name__ == '__main__':
  main()
