from logging import error
from flask import Flask, render_template, redirect, request, json

app = Flask(__name__)

protected = []
admins = ['9519874704']

@app.route('/')
def index():
    return '<h1>Index Page</h1>'
    # return render_template('index.html')

@app.route('/bomb')
def bomb():
    mobile_number, messages = request.args.get('mobile_number'), request.args.get('messages')

    if mobile_number == None or messages == None:
        res = "Please Provide all Parameters."
    
    else:
        if int(messages) >= 500:
            res = "You cannot Bomb more than 500 messages at a Time."
        
        elif str(mobile_number) in protected:
            res = "You can't Bomb on Protected Numbers."

        elif str(mobile_number) in admins:
            res = "You can't Bomb on Admin's Number."

        elif len(str(mobile_number)) > 10 or len(str(mobile_number)) < 10:
            res = "Please Enter Mobile Number Correctly"

        elif len(str(mobile_number)) == 10:
            try:
                int(str(mobile_number))
            
            except:
                res = "Please Enter Mobile Number not ABCD."

        else:
            res = "Bombing is Being Started."

    data = {"mobile_number" : mobile_number, "messages" : messages, "Response" : res}
    response = app.response_class(response=json.dumps(data), mimetype='application/json')
    return response

if __name__=="__main__":
    app.run(port=80, debug=True)