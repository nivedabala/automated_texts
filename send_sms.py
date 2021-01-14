from twilio.rest import Client
import schedule, time
import random

GOOD_MORNING_QUOTES = [
    "Good morning love!", 
    "I don't cook, I don't clean!"
]

def send_message(quotes_list=GOOD_MORNING_QUOTES):
    # Your Account SID from twilio.com/console
    account_sid = ""
    # Your Auth Token from twilio.com/console
    auth_token  = ""

    client = Client(account_sid, auth_token)

    quote = quotes_list[random.randint(0, len(GOOD_MORNING_QUOTES)-1)]

    client.messages.create(
        to="+16476282884", 
        from_="+17868286986",
        body=quote)

schedule.every().day.at("23:39").do(send_message, GOOD_MORNING_QUOTES)


while True:
    schedule.run_pending()
    time.sleep(1)
