import telebot
from gtts import gTTS
# need to use ( pip install gtts )
# Replace 'YOUR_TOKEN' with your actual bot token
bot_token = ''YOUR_TOKEN''
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Text-to-Voice Bot! Send me a message and I will convert it to voice.")

@bot.message_handler(func=lambda message: True)
def convert_text_to_voice(message):
    text = message.text
    voice = gTTS(text=text, lang='en')
    voice.save('voice.mp3')
    voice_file = open('voice.mp3', 'rb')
    bot.send_voice(message.chat.id, voice_file)

bot.polling()
