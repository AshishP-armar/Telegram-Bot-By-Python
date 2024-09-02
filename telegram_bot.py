import requests #pip install requests

token = "api_key"
chat_id = "chat_id" # use the chat id with - this 

# *************** To Send Message **********************
def send_text(message):
	base_url= f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
	requests.get(base_url)
	
