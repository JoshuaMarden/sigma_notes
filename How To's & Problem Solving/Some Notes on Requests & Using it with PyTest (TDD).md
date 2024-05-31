___
So in one Office hours, Chris gave us another overview of using requests and then testing. Below the code is presented.

First though I think this is useful:

### URL's - Uniform Resource Indicators
___

A URL (Uniform Resource Locator) is more than just a __path__.

It is made of multiple componenets.

1. **Scheme**: Protocol used (e.g., `http`, `https`).  

2. **Host**: Domain name or IP address (e.g., `(http://example.com/)`).  

3. **Port**: Network port (usually omitted if using default ports).  

4. **Path**: Specific location/resource within the host (e.g., `/api/users`).  

5. **Query**: Parameters after the `?` used for filtering or search criteria (e.g., `?search=python`).  

6. **Fragment**: Optional part after `#` used to identify a subsection of a resource.So, a full URL might look like this:

    `https://example.com:80/api/users?search=python#section2`

In the above URL:  
- **Scheme**: `https`  
- **Host**: `[example.com](http://example.com/)`  
- **Port**: `80` (default port for HTTP)  
- **Path**: `/api/users`  
- **Query**: `search=python`  
- **Fragment**: `section2`


### API URLs / Requests
____

- API requests feature a '`?`'
- This separates the URL from the query parameters.
- The parameters being Key:Value (dict-like) pairs that tell the server what you want.

#### Example 

_Full URL:_
	`https://api.example.com/data?userId=123&sort=asc`

_BaseURL:_
     `https://api.example.com/data`
_Query Parameters:_
     `?userId=123&sort=asc`
_Key Value Pairs:_
     `userId=123` and `sort=asc`


### Example of Request & PyTest
___

**Main Script:**

```python
import requests

def get_movie_info(title: str, year: int) -> dict:
	response = requests.get(
                            f"https://www.omdbapi.com/?apikey=9091375e"\
                            f"&s={title}&y={year}"
                            )

	if response.status_code == 200:
		# Take a moment here to observe that 
		body = response.json()
	
		if body["Response"] == 'False':
			raise Exception("Movie not found")
			return body["Search"][0]
	
	else:
		raise Exception(f"Something went wrong: {response.status_code}")

def get_woah() -> dict:
	response = requests.get("https://whoa.onrender.com/whoas/random")

	if response.status_code == 200:
		body = response.json()
		
		if len(body) >= 1:
			return body[0]
			
		else:
			raise Exception(f"No random woah found")
			
	else:
		raise Exception(f"Something went wrong: {response.status_code}")

def print_results(woah: dict, movie: dict) -> None:
	
	print(f"Movie: {movie["Title"]}")
	print(f"Year: {movie["Year"]}")
	print(f"Full Line: {woah["full_line"]}")
	print(f"Audio: {woah["audio"]}")


if __name__ == "__main__":

	try:
		woah = get_woah()
		movie = get_movie_info(woah["movie"], woah["year"])
		print_results(woah, movie)
	
	except:
		print("Woah and Movie could not be loaded")

```

**Testing With PyTest**

```python
import pytest
from woah import print_results, get_movie_info, get_woah

def test_print_results(capsys):
	fake_movie = {"Title": "Test Film", "Year": 2000}
	fake_woah = {"full_line": "WOAH", "audio": "www.audio.com"}

	print_results(fake_woah, fake_movie)

	printed_lines = capsys.readouterr().out.split("\n")

	assert printed_lines[0] == "Movie: Test Film"

def test_raise_exception_when_no_movie(requests_mock):
	
	movie = "Test"
	year = 999	
	requests_mock.get(
					 f"https://www.omdbapi.com/?apikey=9091375e&"\
					 f"s={movie}&y={year}",\
					 json={"Response": False}
					 )

	with pytest.raises(Exception):
		get_movie_info(movie, year)

def test_raise_exception_when_no_woah(requests_mock):

	requests_mock.get(
		f"https://whoa.onrender.com/whoas/random", json=[])
	with pytest.raises(Exception):
		get_woah()

example_response = {'Search': [{'Title': 'Knock Knock', 'Year': '2015', 'imdbID': 'tt3605418', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYTQ3MzhlZjQtNWMxOS00NTEzLTgzOWYtNTI3MjhmZGU0ZDM2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'}, {'Title': "Knock Knock, It's Tig Notaro", 'Year': '2015', 'imdbID': 'tt4497142', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BZmU2N2JjZjItODM2Yy00OWFmLWIxNmQtNzg1MjQ4ZDgwZDkwXkEyXkFqcGdeQXVyMTk3NDAwMzI@._V1_SX300.jpg'}, {'Title': 'Knock Knock Live', 'Year': '2015', 'imdbID': 'tt4713054', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNWI4NDQ5NTctOWZkOC00MWNiLTg0MGItZWExMzU0MzFhNDllXkEyXkFqcGdeQXVyNDc0NDgwMjk@._V1_SX300.jpg'}, ], 'totalResults': '36', 'Response': 'True'}

def test_returns_correct_positional_movie(requests_mock):

	movie = "Test"
	year = 999
	requests_mock.get(
	                 f"https://www.omdbapi.com/?apikey=9091375e&"\
	                 f"s={movie}&y={year}",\
	                 json=example_response
	                 )
	                 
	response = get_movie_info(movie, year)
	
	assert response["Title"] == 'Knock Knock'
```
