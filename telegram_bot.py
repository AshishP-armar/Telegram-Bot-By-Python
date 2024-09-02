import requests #pip install requests

token = "api_key"
chat_id = "chat_id" # use the chat id with - this 

# *************** To Send Message **********************
def send_text(message):
	base_url= f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
	requests.get(base_url)
	
	
# **************To send Message Link ******************
def send_link(link):
	link_message = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={link}"
	requests.get(link_message)
	
