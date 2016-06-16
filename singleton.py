class MySingleton(object):
	_intance = None 
	def __new__(self):
		if not self._intance:
			self._intance = super(MySingleton, self).__new__(self)
			self.y = 10
		return self._intance

def singleton(myClass):
	intances = {}
	def getIntance(*args, **kwargs):
		if myClass not in intances:
			intances[myClass] = myClass(*args, **kwargs)
		return intances[myClass]
	return getIntance

@singleton
class TestClass(object):
	pass

x = TestClass()