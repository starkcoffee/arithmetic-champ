import pytest
import re
from trainer import *

def test_prompt():
  assert prompt("100/14") == "What is 100/14 ?\n"
  assert prompt("3000/24") == "What is 3000/24 ?\n"

def test_generate_challenge():
  challenge_str, true_value, tolerance_percent = generate_challenge()
  assert eval(challenge_str) == true_value
  assert tolerance_percent >= 0 
  assert tolerance_percent < 20

def test_is_close_enough():
  assert is_close_enough(42, 42, 0)
  assert is_close_enough(41, 42, 2)
  assert not is_close_enough(42, 24, 3)

def test_compose_response_for_good_enough_answer():
  response = compose_response(True, 42) 
  assert re.search('Yeh good job', response)
  assert re.search('42', response)

def test_compose_response_for_not_good_enough_answer():
  response = compose_response(False, 42) 
  assert re.search('Nah', response)
  assert re.search('42', response)
