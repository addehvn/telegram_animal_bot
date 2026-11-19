from dotenv import load_dotenv
import os
import telebot
import requests
load_dotenv()
key=os.getenv('BOT_KEY')
bot=telebot.TeleBot(key,parse_mode=None)
markup=telebot.types.ReplyKeyboardMarkup()
random_cat_btn=telebot.types.KeyboardButton('random_cat')
random_dog_btn=telebot.types.KeyboardButton('random_dog')
cat_fact_btn=telebot.types.KeyboardButton('cat_fact')
dog_fact_btn=telebot.types.KeyboardButton('dog_fact')
markup.row(random_cat_btn,random_dog_btn)
markup.row(cat_fact_btn,dog_fact_btn)
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

def cat_fact():
   fact_url='https://catfact.ninja/fact'
   response=requests.get(fact_url)
   json_data=response.json()
   fact=json_data['fact']
   return f'Cats random fact: {fact}'  

def dog_fact():
   fact_url='https://dogapi.dog/api/v2/facts?limit=1'
   response=requests.get(fact_url)
   data_josn=response.json()
   data=data_josn['data']
   attributes=data[0]['attributes']
   fact=attributes['body']
   return fact 

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,' Hey there welcome to Animal.\n You can choose an option from list',reply_markup=markup)

@bot.message_handler(func=lambda message:message.text=='random_dog')
def get_random_dog(message):
    bot.send_photo(message.chat.id,random_dog())

@bot.message_handler(func=lambda message:message.text=='random_cat')
def get_random_cat(message):
    bot.send_photo(message.chat.id,random_cat())

@bot.message_handler(func=lambda message:message.text=='cat_fact')
def get_cat_fact(message):
   bot.send_message(message.chat.id,cat_fact())

@bot.message_handler(func=lambda message:message.text=='dog_fact')
def get_dog_fact(message):
   bot.send_message(message.chat.id,dog_fact())
   
bot.infinity_polling()