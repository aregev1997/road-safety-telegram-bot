#pip install telepot
#pip3 install python-telegram-bot

import logging
from telegram.ext import *
import Responses
from telegram.ext import Filters, Updater, CommandHandler,InlineQueryHandler, CallbackQueryHandler,MessageHandler
import requests
import re
import telepot
import telegram
#from telegram import bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


API_KEY = '1949881014:AAHEoC0f9ED4TVgvyU4H_47NTDP1XQIc99I'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()
#     image_url = contents['url']
#     return image_url


def warning_lights_command(update,context):
    bot = telegram.Bot(token=API_KEY)
    chat_id=update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=open('C:\ADI_SHIREL_BOT\image.png', 'rb'))


def start_command(update, context):
    update.message.reply_text('What is the problem?')


def help_command(update, context):
    update.message.reply_text('\warning_lights\n'+r'\numbers'+'\n'+'\yedidim\n')

def numbers_command(update, context):
    update.message.reply_text('To Yedidim dial 1230\n'+
                              'Emergency stop on Route 6 dial *6116')

def yedidim_command(update, context):
    bot = telegram.Bot(token=API_KEY)
    chat_id = update.message.chat_id
    update.message.reply_text('Dial 1230')


def Puncture_command(update, context):

    bot = telegram.Bot(token=API_KEY)
    chat_id = update.message.chat_id
    #url='https://www.rac.co.uk/drive/advice/car-maintenance/how-to-change-a-tyre/'
    garage_url='https://waze.com/ul?q=garage'
    #update.message.reply_text(url,garage_url)
    update.message.reply_text(garage_url)


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = Responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':

    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('warning_lights', warning_lights_command))
    dp.add_handler(CommandHandler('numbers', numbers_command))
    dp.add_handler(CommandHandler('yedidim', yedidim_command))
    dp.add_handler(CommandHandler('Puncture',Puncture_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(0)
    updater.idle()




