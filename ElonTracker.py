import requests
from twilio.rest import Client

# Your FlightAware API key
api_key = "YOUR_API_KEY"

# The FlightAware identifier for Elon Musk's plane
ident = "N628TS", "N272BG", "N502SX"

# Your Twilio account SID and auth token
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

# Your Twilio phone number
from_number = "+1234567890"

# The phone number you want to send the text to
to_number = "+0987654321"

def check_flight_status():
  # Make a request to the FlightAware flightInfo API
  url = f"https://api.flightaware.com/json/FlightXML3/FlightInfo?ident={ident}&howMany=1&offset=0"
  headers = {"Authorization": f"Basic {api_key}"}
  response = requests.get(url, headers=headers)

  # Check the status of the flight
  if response.status_code == 200:
    data = response.json()
    if data["FlightInfoResult"]["flights"][0]["realtime_status"] == "in the air":
      send_text()

def send_text():
  # Create a Twilio client
  client = Client(account_sid, auth_token)

  # Send a text message
  message = client.messages.create(
      body="Elon Musk's plane is in the air!",
      from_=from_number,
      to=to_number
  )

if __name__ == "__main__":
  check_flight_status()
