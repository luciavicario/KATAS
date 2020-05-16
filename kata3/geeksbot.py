from telegram.ext import Updater

def main():
    # Gestiona la comunicacion entre nuestro bot y telegram, 
    # cuando reciva actualizaciones de telegram, reaccionara,
    # o si es algún mensaje mirará como responder.

    # Instanciamos el updater. 
    # Necesita un token que hay que pedirselo al boot father 
    # de Telegram e introducirlo en este comando con comillas.
    # /start -> /newbot
    updater = Updater(token=open('./bot_token').read(), use_context=True)

    # Reparte el trabajo entre los manejadores (componentes que
    # se encargan de reacionar ante los comandos de telegram)
    # Invocará a la función de cada comando recibido.

    # Añadimos un manejador al: ( ... .add_handler(manejador, función))
    # comando /start
    # comando /repite
    # comando /suma

    updater.dispatcher.add_handler(CommandHandler('start',start))
    updater.dispatcher.add_handler(CommandHandler('repite',repite))
    updater.dispatcher.add_handler(CommandHandler('suma',suma))

    # Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    # Capturamos señales de parada
    updater.idle()

# update: El comando
# context: Lista de palabras recibidas como comandos (son Strings)

# Recibir comando y  saludar
def start(update, context):
    update.message.reply_text("Hola, soy un bot")

# Recibir comando y repetir
def repite(update,context):
    update.message.reply_text(update.message.text)

# Recibir comando y sumar
def suma (update,context):
    # args = [2, 2] -> # + #
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es " + str(resultado))

main()