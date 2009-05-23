import configobj, re
conf = configobj.ConfigObj("mpyw.ini")
if conf.as_bool("speech_allowed"):
	import comtypes.client
	sapi = comtypes.client.CreateObject("SAPI.SPvoice")

def speak(text):
	try:
		sapi.speak(text)
	except NameError:
		pass
def find(what, where, case):
	if  not case:
		where = where.lower()
		what = what.lower()
	try:
		return where.index(what)
	except ValueError:
		return -1
def find_by_regex(regex, text, case):
	try:
		if case:
			reg = re.compile(regex)
		else:
			reg = re.compile(regex, re.i)
	except re.error:
			return -2
	res = reg.search(text)
	return res.start()