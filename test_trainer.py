import pytest
import re
from trainer import *

def test_results():
  results = Results()
  results.append(1, True)
  results.append(3, False)

  assert results.mean_completion_time_s() == 2
  assert results.success_rate() == 50
  assert results.count() == 2

def test_prompt():
  assert prompt("100/14") == "What is 100/14 ?\n"
  assert prompt("3000/24") == "What is 3000/24 ?\n"

def test_generate_numerator():
  assert generate_numerator() >= 100 
  assert generate_numerator() <= 10000 
  assert generate_numerator() % 100 == 0

def test_generate_challenge():
  challenge_str, true_value, tolerance_percent = generate_challenge()
  assert re.search('\\d/\\d', challenge_str)
  assert eval(challenge_str) == true_value
  assert tolerance_percent == 0.05

def test_generate_challenge_gives_different_challenges():
  challenge_str1, *_ = generate_challenge()
  challenge_str2, *_ = generate_challenge()
  assert challenge_str1 != challenge_str2

def test_get_answer_returns_a_float_from_user_input(mocker):
  mocker.patch('builtins.input', return_value='7.5')
  assert get_answer('prompt') == 7.5

def test_get_answer_keeps_asking_until_it_gets_valid_input(mocker):
  mocker.patch('builtins.input', side_effect=['hi', 'there', 42])
  assert get_answer('prompt') == 42

def test_is_close_enough():
  assert is_close_enough(42, 42, 0)
  assert not is_close_enough(41, 42, 0.01)
  assert is_close_enough(41, 42, 0.03)

def test_compose_response_for_good_enough_answer():
  response = compose_response(True, 42) 
  assert re.search('Yeh good job', response)
  assert re.search('42', response)

def test_compose_response_for_not_good_enough_answer():
  response = compose_response(False, 42) 
  assert re.search('Nah', response)
  assert re.search('42', response)

