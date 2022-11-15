

import keys
from twilio.rest import Client
client = Client(keys.accountSID, keys.authToken)


TwilioNumber = "+16802198519"



myCellPhone = "+19037055343"

textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "John is smelly")

print(textmsg.status)

