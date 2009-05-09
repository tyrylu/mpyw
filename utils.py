import configobj
conf = configobj.ConfigObj("mpyw.ini")
if conf.as_bool("speech_allowed"):
	import comtypes.client
	sapi = comtypes.client.CreateObject("SAPI.SPvoice")

def speak(text):
	try:
		sapi.speak(text)
	except NameError:
		pass
