import re

class Human(object):
	'class co so cho tat ca nguoi'
	__name = ""
	__age = 0
	__phone = ""

	def __init__(self, name, age, phone):
		try:
			int(phone)
			int(age)
		except ValueError:
			print "Wrong parameter"
			return
		self.__name = name
		self.__age = age
		self.__phone = phone

	def __del__(self):
		print "Delete obj"

	def getName(self):
		return self.__name

	def getPhone(self):
		return self.__phone

	def printInfo(self):
		print "%s %s" % (name, phone)

class Parent(Human):
	__isMerry = False

	def __init__(self, isMerry, name, phone, age):
		super(Parent, self).__init__(name, age, phone)
		self.__isMerry = isMerry

