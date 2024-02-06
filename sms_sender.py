from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_ID"
auth_token = "YOUR_AUTH_TOKEN"

# Initialize client.
client = Client(account_sid, auth_token)

# Send message.
message = client.messages.create(
    from_="+10123456789", body="Yo soy Pablo Escobar", to="+10123456789"
)

# Print message ID.
print(message.sid)
