from dotenv import load_dotenv
import os
import telebot
import requests
load_dotenv()
key=os.getenv('BOT_KEY')

bot=telebot.TeleBot(key,parse_mode=None)

def random_dog():
  dog_url='https://dog.ceo/api/breeds/image/random'
  response=requests.get(dog_url)
  data_json=response.json()
  pic=data_json['message']
  return pic 

def random_cat():
   cat_url='https://cataas.com/cat?json=True'
   response=requests.get(cat_url)
   json_data=response.json()
   pic=json_data['url']
   return pic 
   

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,' Hey there welcome to Animal.\n You can choose an option from list')

@bot.message_handler(commands=['random_dog'])
def get_random_dog(message):
    bot.send_photo(message.chat.id,random_dog())

@bot.message_handler(commands=['random_cat'])
def get_random_cat(message):
    bot.send_photo(message.chat.id,random_cat())
   
bot.infinity_polling()