from random import randint

def prompt(challenge):
  return f"What is {challenge} ?\n"

def generate_numerator():
  return (randint(100,10000)//100)*100

# returns (challenge_str, true_value, tolerance_percent)
def generate_challenge():
  numerator = generate_numerator()
  denominator = randint(6, 100)
  return f"{numerator}/{denominator}", numerator/denominator, 0

def is_close_enough(answer, true_value, tolerance_percent):
  return abs(answer - true_value) <= tolerance_percent

def compose_response(was_close_enough, true_value):
  response = "\n"

  if was_close_enough:
    response += "Yeh good job!🥳\n"
  else:
    response += "Nah\n"
  response += f'Answer is {true_value}\n'

  return response

def main():
  while True:
    challenge_str, true_value, tolerance_percent = generate_challenge()
    answer = float(input(prompt(challenge_str)))
    close_enough = is_close_enough(answer, true_value, tolerance_percent)
    print(compose_response(close_enough, true_value))

if __name__ == '__main__':
  main()
