import vonage
from flask import jsonify

# client = vonage.Client(application_id='2e237d3f-9f78-4c57-bd69-635844ba9a72', private_key='q')

# ncco = [
#   {
#     'action': 'talk',
#     'voiceName': 'Aditi',
#     'text': 'Hello sir this is a call from your operator bank. We are feeling bad to inform you that your balance of twenty thousand rupees is debited from your bank account in the case of fraudulent activity! Now get your ass and suck my dick. Regards your dad alif'
#   }
# ]

# voice = vonage.Voice(client)
# while True:
# 	response = voice.create_call({
# 	'to': [{
# 	    'type': 'phone',
# 	    'number': '919519874704'
# 	  }],
# 	  'from': {
# 	    'type': 'phone',
# 	    'number': '919519874704'
# 	  },
# 	  'ncco': ncco
# 	})
# 	print(response['uuid']+' Call Bombed')

class CallBomb:
	def __init__(self, times, msg = "हैलो सर हमें आपको यह सूचित करने के लिए खेद है कि आपी माँ चुद छुकी है कृपया अगली बार कंडोम का उपयोग करे"):
		self.times = times
		client = vonage.Client(application_id='2e237d3f-9f78-4c57-bd69-635844ba9a72', private_key='q')
		global ncco 
		ncco = [
				{
					'action': 'talk',
					'voiceName': 'Aditi',
					'text': msg
				}
			]

		global voice 
		voice = vonage.Voice(client)

	def bomb(self):
		for i in range(self.times):
			response = voice.create_call({
				'to': [{
					'type': 'phone',
					'number': '919519874704'
				}],
				'from': {
					'type': 'phone',
					'number': '919519874704'
				},
				'ncco': ncco
				})
			print(response['uuid'], "Call Bombed")
		return jsonify(
					Response = "Bombing is Being Started",
					Country_Code = '91',
					Mobile_Number = 9519874704,
					Tool = "iCallBomber",
					Creator = "MrSp4rX"
				)
