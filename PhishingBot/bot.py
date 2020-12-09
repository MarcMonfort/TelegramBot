from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

import matplotlib.pyplot as plt
import pickle
import os
import random




def start(update, context):
    name = update.effective_chat.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="PhishingPredictorBot!\nWelcome %s!"
        "\nUse /help to see the available commands." % name)


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Available commands:"
        "\n/status shows yours current alert level."
        "\n/threats shows your most recent threats."
        "\n/report allows to report a possible phishing link",
        parse_mode=ParseMode.MARKDOWN
    )


def status(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Number of threats: "+str(random.randint(0,10))
    )

def threats(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Number of threats: "+str(random.randint(0,10))
    )

def report(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Usage:"+'\n/report www.example.com'
    )

def login(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Username:"
    )







TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('report', report))
dispatcher.add_handler(CommandHandler('login', login))
dispatcher.add_handler(CommandHandler('status', status))
dispatcher.add_handler(CommandHandler('threats', threats))
# dispatcher.add_handler(MessageHandler(Filters.text, skyComp))


updater.start_polling()
