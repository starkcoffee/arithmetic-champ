

def prompt(challenge):
  return f"What is {challenge} ?\n"

# returns (challenge_str, true_value, tolerance_percent)
def generate_challenge():
  return "100/14", 100/14, 0

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
  challenge_str, true_value, tolerance_percent = generate_challenge()
  while True:
    answer = float(input(prompt(challenge_str)))
    close_enough = is_close_enough(answer, true_value, tolerance_percent)
    print(compose_response(close_enough, true_value))

if __name__ == '__main__':
  main()
