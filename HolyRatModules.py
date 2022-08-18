import asyncio
import logging
import datetime
from .. import loader, utils
from asyncio import sleep

logger = logging.getLogger(__name__)


@loader.tds
class HolyRatMod(loader.Module):
    
    strings = {"name": "HolyRat", "cfg_doc": "smth"}
    tmsgIs = False
    
    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m)) 
        
    async def gfycmd(self, message):
        """.gfy {текст}"""
        url = "https://google.com/search?q="
        await asyncio.sleep(0.2)
        text = utils.get_args_raw(message)
        text1 = text.split(" ")
        reqtext = text1[0:]
        reqtext1 = " ".join(reqtext)
        urltext = "https://google.com/search?q=" + "+".join(text1)
        await utils.answer(message, "Ссылка готова: <a href=" 
        + urltext+ ">" + " ".join(text1) + "</a>")

    async def pingcmd(self, message):
        """Вернёт время задержки работы user-бота в миллисекундах."""
        time1 = datetime.datetime.now()
        await utils.answer(message, "Проверяю пинг...")
        time2 = datetime.datetime.now()
        time_diff = time2 - time1
        tping = time_diff.microseconds / 1000
        tping = str(tping)
        await utils.answer(message, "Пинг: <code>" + tping + "ms</code>.")

    async def tmsgcmd(self, message):
        """Зациклить сообщение:\n.tmsg {число} {s, m, h} {текст}""" 
        def calc(ttype_fun, tnum_fun):
            if ttype_fun == "s" or ttype_fun == "с":
        		     	tnun_fun = tnum_fun * 1
            elif ttype_fun == "m" or ttype_fun == "м":
            		 tnum_fun = tnum_fun * 60
            elif ttype_fun == "h" or ttype_fun == "ч":
                tnum_fun = tnum_fun * 60 * 60
            else:
                tnum_fun = 0
            return tnum_fun
        timetype = "none"
        timenum = 0 
        args = utils.get_args_raw(message)
        args_spl = args.split(" ")
        try:
            timenum = int(args_spl[0])
            timetype = str(args_spl[1])
            timetext = args_spl[2:]
            timetext = " ".join(timetext)
        except Exception as e:
            logger.exception(e)
            
        timer = calc(timetype, timenum)
        if timer > 0:
            try:
                global tmsgIs
                tmsgIs = True
                await message.delete()
                while tmsgIs:
                    await message.respond(timetext)
                    await sleep(timer)
            except ValueError:
                await message.respond("Ошибка: укажите сообщение, которое нужно отправлять!") 
            except Exception as e:
                e = str(e)
                logger.exception(e)
                await message.respond("Произошла неизвестная ошибка.\n" 
                + "Проверьте правильность ввода команды!")
        else:
            await utils.answer(message, "	<b>Что-то пошло не так. Проверьте правильность ввода команды.</b>") 
            
    async def 	tmsgstopcmd(self, message):
        global tmsgIs
        tmsgIs = False
        if tmsgIs == True:
            tmsgIs = False
            await utils.answer(message, "Цикл остановлен.")
        else: 
            await utils.answer(message, "Вы не запускали циклы!") 
       










