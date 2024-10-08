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
	

# ****************** Photo Sending ****************
def send_photo():
    files_photo = {'photo':open('file path','rb')}
    responce_photo= requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id=-4563384288",files=files_photo)
    print(responce_photo)
	
# ****************** Video Sending ****************
def send_video():
    files_video = {'photo':open('file path','rb')}
    responce_photo= requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id=-4563384288",files=files_video)
    print(responce_photo)

# ****************** Video Sending with caption ****************
def send_video_caption():
    files_video = {'video':open('file path','rb')}
    caption = "this is video caption"
    responce_video= requests.post(f"https://api.telegram.org/bot{token}/sendVideo?chat_id=-4563384288&caption={caption}",files=files_video)
    print(responce_video)

# ****************** Photo Sending with caption ****************
def send_image_caption():
    files_image = {'photo':open('file path','rb')}
    caption = "this is image caption"
    responce_video= requests.post(f"https://api.telegram.org/bot{token}/sendVideo?chat_id=-4563384288&caption={caption}",files=files_image)
    print(responce_video)