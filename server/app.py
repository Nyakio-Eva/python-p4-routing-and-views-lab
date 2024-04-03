#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(0,(parameter)))
    print(numbers)
    return f'{numbers}\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation, num2):
   if operation == "+":
       result = num1 + num2

   elif operation == "-":
       result = num1 - num2

   elif operation == "*":
       result = num1 * num2

   elif operation == "div":
       if num2 != 0: #check to avoid division by zero error
           result = num1 / num2

   elif operation == '%':
       if num2 != 0:
           result = num1 % num2

   if result is not None:
       return f'{result}'

   else:
       return 'Invalid operation'               




if __name__ == '__main__':
    app.run(port=5555, debug=True)
