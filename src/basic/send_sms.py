# Download the twilio-python library from http://twilio.com/docs/libraries
#from twilio.rest import TwilioRestClient
from twilio import rest

# Find these values at https://twilio.com/user/account
account_sid = "AC489b7850d915e0d98a8252ac27a1e2fd"
auth_token = "4baf1a3cf84f3cf560f8a3fb57920deb"
#client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+919952067334", from_="+13126267334",
                                     body="This is a sample sms sent from Python program")
print message.sid
