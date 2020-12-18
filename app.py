from flask import Flask, request, jsonify
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/v1/sanitized/input/', methods = ["POST"])
def payload():
    # return the json sent with the post request and save it in the output variable
    output = request.json['payload']
    # convert the output into a string that can be parsed to check for invalid parameters (this was useful for testing but probably isnt necessary)
    outputString = str(f"""{output}""")
    # check for any possible SQL injection attacks
    sanitation = verifySanitization(outputString)
    data = {'payload_status': sanitation}
    # output the data
    return jsonify(data)

def verifySanitization(data):
    ''' this function returns a boolean that determines if the input text is malicious sql code '''

    # read the txt file for the invalid input parameters
    with open("SQL-Injection-codes.txt", 'r') as file:
        lines = file.readlines()
        lines = [line.strip("\n") for line in lines]
    # compare the input data to the invalid input parameters

    # print(lines[:10])
    # if the data is invalid input return 'Unsanitized'
    if data in lines:
        # locate where in the file the SQL code was found
        pos = lines.index(data)
        print(f'The data was found on line: {pos} with the value of {lines[pos]}')
        return 'Unsanitized'

    # if the data is valid input return sanitized
    else:
        print(f"{data} is valid input")
        return 'Sanitized'


    
    


if __name__ == "__main__":
    app.run(debug=True)
