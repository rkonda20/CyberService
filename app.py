"""Main application file"""
from flask import Flask
from flask import Response


app = Flask(__name__)

'''***
@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    str = "".join(reversed(random_string))
    response_text = '{ "message":' + str +  '}'
    print("******* Response - " + response_text)
    response = Response(response_text, 200, mimetype='application/json')
    print("******* Response obj - " + response)
    return response
#   return "".join(reversed(random_string))
'''

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '{ "msg": "Hello World" }'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)