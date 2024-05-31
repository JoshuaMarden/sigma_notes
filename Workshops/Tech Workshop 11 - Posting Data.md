___

### Quick Note
___

- Rather than building long URLs you can simply build a dictionary with the API parameters in it.

```python
parameters = {
	't' : "Fight Club"
	'i' : "321564"
	'api_key' : "97640f06"
}
```
Then you can pass the dictionary along with the URL:
```python
response = request.get(base_url, params=parameters, timeout=10)
```

- If you declare an empty dict you can fill it out each time you want to send a query.

### Workshop Work
___

Basic API [here](### Quick Note)

Here is an example of 
```python
"""Experimenting with sigma test API"""

import pprint
import json
import requests
  
base_url = "https://sigma-micro-blogging.herokuapp.com/"


def get_micro_blogging_site(base_url: str) -> json:
	response = requests.get(base_url)
	return response.json()



def submit_to_microblog(base_url: str, msg: str, username: str) -> bool:
# API set to accept a dict with 'message'
	data = {"message": msg, "from": username}
	msg_sent = requests.post(f"{base_url}{username}", json=data)

  

if 200 <= msg_sent.status_code < 300:
	return True
else:
	return False

  

if __name__ == "__main__":
	base_url = "https://sigma-micro-blogging.herokuapp.com/"
	pprint.pprint(get_micro_blogging_site(base_url))

  

	msg = "fish are all body no head"
	username = "sigmastudent99"
	pprint.pprint(submit_to_microblog(base_url, msg, username))
```


