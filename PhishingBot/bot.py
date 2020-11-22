from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

import matplotlib.pyplot as plt
import pickle
import os

from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

from skyline import Skyline



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
        "\n/report allows to check link thread.",
        parse_mode=ParseMode.MARKDOWN
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
        user_id = update.effective_chat.id
        if not context.args:
            raise Exception("id no indicat")
        id = context.args[0]
        if id not in context.user_data:
            raise Exception("Variable '" + id + "' no definida")

        directory = "./database/" + str(user_id)
        if not os.path.isdir(directory):
            os.makedirs(directory)

        filename = directory + '/' + str(id) + '.sky'
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
        user_id = update.effective_chat.id
        if not context.args:
            raise Exception("id no indicat")
        id = context.args[0]

        directory = "./database/" + str(user_id)
        filename = directory + '/' + str(id) + '.sky'
        if not os.path.isfile(filename):
            raise Exception("No es troba cap Skyline amb id = '" +
                            id + "'. Prova a guardar primer amb /save id")

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


def skyComp(update, context):
    try:
        msg = update.message.text
        lexer = SkylineLexer(InputStream(msg))
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()

        numError = parser.getNumberOfSyntaxErrors()
        if numError > 0:
            raise Exception('Error de sintaxis!')

        visitor = EvalVisitor(context.user_data)
        a = visitor.visit(tree)

        if isinstance(a, Skyline):
            user_id = update.effective_chat.id
            fitxer = str(user_id) + "_tmp.png"
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
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(MessageHandler(Filters.text, skyComp))


updater.start_polling()
