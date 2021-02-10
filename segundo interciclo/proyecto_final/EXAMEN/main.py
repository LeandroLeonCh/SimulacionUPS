from bot.bot_facebook import bot_facebook
from bot.excel_bot import excel_bot
from bot.flyer_canvas import flyer_bot
from bot.outlook_bot import outlook_bot
from bot.comentarios_likes import  comentarios_likes
import json



if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)

    driver_path = 'chromedriver'
    url = config['url']
    url_outlook = config['url_outlook']
    url_canva = config['url_canva']
    username = config['username']
    password = config['password']
    username_correo = config['username_correo']
    pass_correo = config['password_correo']
    url_publicacion = config['url_publicacion']
    url_drive=config['url_drive']

    #flyer_bot(driver_path,url_canva)
    #bot_facebook(driver_path,url,username,password)
    #outlook_bot(driver_path,url_outlook,username_correo,pass_correo)
    #comentarios_likes(driver_path,url,username,password,url_publicacion)
    excel_bot(driver_path, url_drive)

