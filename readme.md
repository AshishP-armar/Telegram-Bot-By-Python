1. Create a Telegram bot
2. Send a message to a channel

1. Create a Telegram bot
    To use the Telegram API, you will need to create a Telegram bot and obtain its API key. You can do this by talking to the BotFather in Telegram. To do this:

    1. Open the Telegram app on your smartphone or desktop.
    2. Search for the “BotFather” username in the search bar.
    3. Click on the “Start” button to start a conversation with the BotFather.
    4. Type “/newbot” and follow the prompts to create a new bot. The BotFather will give you an API      key that you will use in the next step.

2. After creating a new bot :
    1. Make A Telegram group and add this bot init using bot username

3. In next step We fetching the chat_id :
    1. Send message in telegram group - /my_id bot_username
    2. To fetch chat_id go to the :- https://api.telegram.org/api_key/getUpdates
    3. it will show like this (   {"ok":true,"result":[{"update_id":12345648,
"message":{"message_id":76,"from":{"id":123456789,"is_bot":false,"first_name":"A","last_name":"TP"},********"chat":{"id":-123456789,***********"title":"group_name","type":"group","all_members_are_administrators":true},"date":1725288439,"text":"/id","entities":[{"offset":0,"length":3,"type":"bot_command"}]}},{"update_id":893875403,
"message":{"message_id":77,"from":{"id":123456789,"is_bot":false,"first_name":"A","last_name":"TP"},"chat":{"id":-123456789,"title":"group_name","type":"group","all_members_are_administrators":true},"date":1725288457,"text":"/my_id @atp4455bot","entities":[{"offset":0,"length":6,"type":"bot_command"},{"offset":7,"length":11,"type":"mention"}]}}]}  )
    4. In The stars it will be the your chat_id