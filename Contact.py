class Contact(object):

    def __init__(self,**attributes):
        self.attrs = attributes


    def getAttr(self,attr):
        """We can use this to sort the contacts by attribute """
        if attr in self.attrs:
            return self.attrs[attr]
        return ''

    def setName(self,name):
        self.name = name
        self.attrs['name'] = name

    def setPhone(self,phone):
        self.phone = phone
        self.attrs['phone'] = phone

    def setZip(self,zipcode):
        self.zipcode = zipcode
        self.attrs['zipcode'] = zipcode

    def setAddress(self,address):
        self.address = address
        self.attrs['address']=address

    def setAddress2(self,address2):
        self.address2 = address2
        self.attrs['address2'] = address2

    def setCity(self,city):
        self.city = city
        self.attrs['city']=city

    def setState(self,state):
        self.state = state
        self.attrs['state'] = state

    def getLabel(self):
        pass