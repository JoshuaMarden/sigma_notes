___

TODO: Get notes when pushed to git.


```python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)  # Flask("Whatever")

with open("companies.json", 'r') as f:
    companies_data = json.load(f)

country = [c["country"] for c in companies_data]

@app.route("/", methods=["GET"])
def hello():
    return "<h1>Hello World<h1>"

@app.route("/companies", methods=["GET"])
def companies_list():
    parameters = request.args.to_dict()
    print(parameters)
    if parameters["country"] in country:
        return jsonify([c for c in companies_data if c["country"] == parameters["country"]])
    else:
        return "Error, invalid query", 404

@app.route("/companies/<int:id>", methods=["GET"])
def company_id(id):
    return [c for c in companies_data if c["id"] == id]

if __name__ == "__main__":
    app.run(port=5000, debug=True)
```