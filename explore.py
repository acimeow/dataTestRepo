from twilio.rest import Client

client = Client("AC02dac7cf1eadbefd39a617e877e2d464", "9c8aef55c254b6d2901c701bdb5dee4c")

for msg in client.messages.list():
    print(f"Deleting: {msg.body}")
    msg.delete()

# msg = client.messages.create(
#     to="+19174967168",
#     from_="+18179935898",
#     body="Hello from Python",
# )

# print(f"Created a new message: {msg.sid}")
