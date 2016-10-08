# Download the twilio-python library from http://twilio.com/docs/libraries
#from twilio.rest import TwilioRestClient
from twilio import rest

def get_number():
    mobno = raw_input("Mobile number to send SMS: (along with country code)")
    print mobno, len(mobno)
    if len(mobno) == 0:
        return mobno
    else:
        if (not mobno.startswith("+")):
            print "Mobile number should start with +, please include the country code"
            mobno = "0"
            print "Try again"
        elif (len(mobno) < 12):
            print "Mobile number length should be atleast 11 digits including + symbol"
            mobno = "0"
            print "Try again"
            
    return mobno

def get_message():
    mobmsg = raw_input("Enter a message to send - Max 150 characters")
    print mobmsg, len(mobmsg)

    if len(mobmsg) == 0:
        return mobmsg
    else:
        if (len(mobmsg) > 150):
            print "Enter a message lesser than 150 characters length"
            mobmsg = ""
            print "Please Try again"
            
    return mobmsg

# Find these values at https://twilio.com/user/account
account_sid = "AC489b7850d915e0d98a8252ac27a1e2fd"
auth_token = "4baf1a3cf84f3cf560f8a3fb57920deb"
#client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

mobnum = "0"
while (mobnum == "0"): 
    mobnum = get_number()
msg = ""
while (msg == ""): 
    msg = get_message()

if (len(mobnum) > 0 and len(msg) > 0):
    message = client.messages.create(to=mobnum, from_="+13126267334", body=msg)
    print message.sid
    print "SMS sent to "+mobnum+", message is ["+msg+"]"
else :
    print "Either number of message is null, hence not sending the sms"

#message = client.messages.create(to="+919952067334", from_="+13126267334",
#                                     body="This is a sample sms sent from Python program")
#print message.sid
