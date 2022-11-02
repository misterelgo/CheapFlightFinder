from twilio.rest import Client

TWILIO_SID = "AC0178e75d507105c023f6bb184900017f"
TWILIO_AUTH_TOKEN = "c7ca91aaad2a5033690916f3c5de1ebc"
TWILIO_VIRTUAL_NUMBER = "+13023054266"
TWILIO_VERIFIED_NUMBER = "+33646356635"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.\
            create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
        # Prints if successfully sent.
        print(message.sid)