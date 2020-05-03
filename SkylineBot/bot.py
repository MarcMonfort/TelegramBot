from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
""" import matplotlib
import matplotlib.pyplot as plt """

import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser

from cl.EvalVisitor import EvalVisitor
from cl.TreeVisitor import TreeVisitor

import matplotlib.pyplot as plt  # grafica

from skyline import Skyline

import random
import os

import pickle


def start(update, context):
    name = update.effective_chat.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="SkyLineBot!\nBenvingut %s!"
        "\nUsa /help per veure les comandes disponibles." % name)


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Comandes disponibles:"
        "\n/help llistat de les comandes disponibles."
        "\n/start inicia la conversa amb el Bot"
        "\n/author mostra el nom i el correu de l'autor del projecte"
        "\n/lst mostra els identificadors definits i la seva àrea"
        "\n/clean esborra tots els identificadors definits."
        "\n/save id : Guarda un skyline definit amb el nom id.sky"
        "\n/load id : Carrega el skyline de l'arxiu id.sky."
    )


def author(update, context):
    name = "Marc Monfort Grau"
    email = "marc.monfort@est.fib.upc.edu"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=name+'\n'+email
    )


def lst(update, context):
    try:
        sky = []
        for x in context.user_data:
            if isinstance(context.user_data[x], Skyline):
                sky.append(str(x) + " - " +
                           str(context.user_data[x].getArea()))
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ID  Area\n" + '\n'.join(sky)
        )
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣' + " *" + str(e) + "*",
            parse_mode=ParseMode.MARKDOWN)


def clean(update, context):
    context.user_data.clear()


def save(update, context):
    try:
        name = update.effective_chat.first_name
        user_id = update.effective_chat.id
        if not context.args:
            raise Exception("id no indicat (/save id)")
        id = context.args[0]

        if id not in context.user_data:
            raise Exception("Variable '" + id + "' no definida")

        filename = 'database/' + str(user_id) + '.' + str(id) + '.sky'
        outfile = open(filename, 'wb')

        pickle.dump(context.user_data[str(id)], outfile)
        outfile.close()
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣' + " *" + str(e) + "*",
            parse_mode=ParseMode.MARKDOWN)


def load(update, context):
    try:
        name = update.effective_chat.first_name
        user_id = update.effective_chat.id
        if not context.args:
            raise Exception("id no indicat (/load id)")
        id = context.args[0]
        
        #mirar antes si existe el archivo!!!
        filename = 'database/' + str(user_id) + '.' + str(id) + '.sky'
        infile = open(filename, 'rb')
        sky = pickle.load(infile)
        infile.close()

        context.user_data[id] = sky
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣' + " *" + str(e) + "*",
            parse_mode=ParseMode.MARKDOWN)


def counter(update, context):
    if 'counter' not in context.user_data:
        context.user_data['counter'] = 0
    context.user_data['counter'] += 1
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(context.user_data['counter']))


def tata(update, context):
    try:
        msg = update.message.text
        lexer = SkylineLexer(InputStream(msg))
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()

        numError = parser.getNumberOfSyntaxErrors()

        if numError > 0:
            raise Exception('Error de sintaxis!')

        visitor2 = EvalVisitor(context.user_data)
        a = visitor2.visit(tree)

        if isinstance(a, Skyline):
            fitxer = "%d.png" % random.randint(1000000, 9999999)
            area, top = a.plot()
            plt.savefig(fitxer, bbox_inches='tight')
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(fitxer, 'rb'))
            os.remove(fitxer)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='area: %d\nalçada: %d' % (area, top))
        else:
            raise Exception('Cap Skyline detectat!')

    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣' + " *" + str(e) + "*",
            parse_mode=ParseMode.MARKDOWN)


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('counter', counter))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(MessageHandler(Filters.text, tata))


updater.start_polling()
