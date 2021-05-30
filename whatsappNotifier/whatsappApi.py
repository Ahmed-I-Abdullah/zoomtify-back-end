from twilio.rest import Client
import environ

def send_message(receiver_number, date_time):
    env = environ.Env()
    environ.Env.read_env()

    account_sid = env("TWILIO_ACCOUNT_SID")
    auth_token = env("TWILIO_AUTH_TOKEN")
    business_number = env("TWILIO_BUSINESS_NUMBER")
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
                                from_= f'whatsapp:{business_number}',  
                                body = f'Hello, I have a meeting at {date_time}',      
                                to = f'whatsapp:{receiver_number}' 
                            ) 
    
    print("Message sid is: ", message.sid)
