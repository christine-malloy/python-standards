import sys
sys.path.append('src')

from webserver import get_repo_url, get_random_number

def test_get_repo_url():
  assert get_repo_url() == "https://github.com/christine-malloy/python-standards"

def test_get_random_number():
  assert isinstance(get_random_number(), (int, float))