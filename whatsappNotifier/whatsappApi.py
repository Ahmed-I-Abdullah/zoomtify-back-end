from twilio.rest import Client
import environ

def send_message(sender_number, receiver_number, date_time):
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()

    account_sid = env("TWILIO_ACCOUNT_SID")
    auth_token = env("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
                                from_= f'whatsapp:{sender_number}',  
                                body = f'Hello, I have a meeting at {date_time}',      
                                to = f'whatsapp:{receiver_number}' 
                            ) 
    
    print(message.sid)
