from twilio.rest import Client

account_sid = "AC2122231ba279401df94fbabbe480cab3"
auth_token = "dc5a97cc9b4d489289a517239939b318"
#phone_number = "0757574935"

client = Client(account_sid, auth_token)


# Get the messages
messages = client.messages.list(
    from_='+254757574935', # Your phone number
    limit=20 # Limit the number of messages
)

# Print out the messages
for message in messages:
    print(message.body)