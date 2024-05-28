___
[Curriculum Page](https://curriculum.sigmalabs.co.uk/Software-Fundamentals/Networking/Week%201/Workshops/get_requests)


- There is no `type` JSON. They're just strings.
- We saw an an unsuccessful request return 200, showing that APIs can be badly setup.
- We looked at using the modules `requests` and `JSON`:
```python
import requests
import JSON

base_url = https://api.github.com/
username = 'airbnb'
ORG = airbnb

def get_user_data(base_url, username):
	try:
		response = requests.get(f"{base_url}/users/{username}", timeout=60)
		response.raise_for_status() # Will crash your programme with an error
		data = response.json()
		print(data)
		
	except requests.exceptions.Timeout:
		print("Timeout")

	except requests.exceptions.RequestsException as e:
		print(f"An error has occured: {e}")

if __name__ == "__main__":
	base_url = https://api.github.com/
	username = 'airbnb'
	ORG = airbnb

	profile_data = get_user_data(base_url, username)
	print(profile_data)

```

- We also note that we MUST make __mock tests__ and NOT use real data. Real data might change or the API might block you.
- TDD therefore relies on such mocks!

```python

import pytest
from get_data import get_user_data

def get_user_data(requests_mock)
	requests_mock.get("https://api.github.com/users/test", json={})
	response = get_user_data(base_url="https://api.github.com", username="test") 

	assert requests_mock.called
	assert requests_mock.call_count == 1
	assert requests_mock.last_requests.method == 'GET'
```