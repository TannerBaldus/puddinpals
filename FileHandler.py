import csv
class FileHandler(object):

	def __init__(self):
		self.uspsFields = ['Last','Delivery','Second','Recipient','Phone']

	def readUSPS(self,row):
		attributes ={}
	
		last = row['Last'].split(' ')
		attributes['name'] = row['Recipient']
		attributes['phone'] = row['Phone']
		attributes['address'] = row['Delivery']
		attributes['address2'] = row['Second']
		attributes['city'] = last[0]
		attributes['state'] = self.stateCode(last[1])
		attributes['zipcode'] = last[2]
		zipcode = last[2]
		return attributes


	def stateCode(self state):
		if len(state) => 2:
			return state[0:1].upper()


	def writeUSPS(self,contact,dictwriter):
		attributes ={}
		attributes['Recipient'] = contact.getAttr('name')
		last = [contact.getAttr('city'),contact.getAttr('state'),contact.getAttr('zipcode')]
		attributes['Last'] = ' '.join(last)
		attributes['Delivery'] = contact.getAttr('address2')
		attributes['Phone'] = contact.getAttr('phone')
		dictwriter.writerow(attributes)

