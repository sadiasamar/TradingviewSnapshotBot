#!/usr/bin/python

import logging
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # take time,level,name
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def snapshot(mesg):
    cmd = [x if i == 0 else x.upper() for i, x in enumerate(mesg)] if len(
        mesg) >= 4 and len(mesg) <= 5 and (mesg[0] == '-' or (len(mesg[0]) == 8 and not mesg[0].islower() and not mesg[0].isupper())) else ['-', 'BINANCE', 'BTCUSDT', '1D'] if len(mesg) == 0 else '❌ Wrong Command ! Try  like this "/snap - nse nifty 1d light" or "/snap - nse nifty 1d dark".\n\nPlease Try Again with a correct one ❗️, You may wanna check /help❓for details.\n\nThank You 👍.'
    if isinstance(cmd, str):
        return cmd
    else:
        ChartID = f'chart/{cmd[0]}/' if len(cmd[0]
                                            ) == 8 and not cmd[0].islower() and not cmd[0].isupper() else 'chart/'
        theme = 'light' if len(cmd) == 4 else 'dark' if len(
            cmd) == 5 and cmd[4].lower() == 'dark' else 'light'
        requesturl =  f'http://localhost:3000/run?base={ChartID}&exchange={cmd[1]}&ticker={cmd[2]}&interval={cmd[3]}&theme={theme}'
        return f'https://www.tradingview.com/x/{requests.get(requesturl).text}'

def snapshotlist(mesg):
    snapshotsurl = []
    cmd = [x if i == 0 else x.upper() for i, x in enumerate(mesg)] if len(
        mesg) >= 6 and (mesg[-1] == 'light' or mesg[-1] =='dark') and (mesg[0] == '-' or (len(mesg[0]) == 8 and not mesg[0].islower() and not mesg[0].isupper())) else ['-', 'BINANCE', 'BTCUSDT', '1W'] if len(mesg) == 0 else '❌ Wrong Command ! Try  like this "/snap - nse nifty 1d light" or "/snap - nse nifty 1d dark".\n\nPlease Try Again with a correct one ❗️, You may wanna check /help❓for details.\n\nThank You 👍.'
    if isinstance(cmd, str):
        return cmd
    else:
        ChartID = f'chart/{cmd[0]}/' if len(cmd[0]
                                            ) == 8 and not cmd[0].islower() and not cmd[0].isupper() else 'chart/'
        tickers = cmd[2:-2]
        for symbol in tickers:
            requesturl =  f'http://localhost:3000/run?base={ChartID}&exchange={cmd[1]}&ticker={symbol}&interval={cmd[-2]}&theme={cmd[-1].lower()}'
            snapshotsurl.append(f'https://www.tradingview.com/x/{requests.get(requesturl).text}')
        return snapshotsurl


def start(update, context):
    name = update.message.from_user.first_name  # first name of the user messaging
    reply = "Hi!! {}".format(name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'{reply} \n\nI\'m a TVSnapShot Bot 🤖, I can generate Tradingview Chart Snapshot 📊 of your choice.\n\nPlease type /help❓to know request commands. \n\nThank You. 👍')

def help(update, context):
    reply = """❗️⚠️ Please type /snap or /snaplist first to initate command reception.

You can send the following parameters with a space in between to generate the snapshot URL. 🚀

1️⃣ ChartID = The 8 character long chart id of your saved chart layout or a simple '-'. (Also make sure your chart layout sharing is ON)
(Note: To find your ChartID, you may wanna look at your url https://www.tradingview.com/chart/chartid/)

2️⃣ Exchange Name = Type The Exchange Name Such as 'NSE', 'BSE', 'NASDAQ', 'BINANCE' Etc.

3️⃣ Ticker / Symbol Name = Type the trading ticker name such as 'NIFTY', 'BANKNIFTY', 'BTCUSDT', 'ETHUSDT' Etc.

4️⃣ Interval / Timeframe = Type the chart Timeframe / Interval such as '1D' for 1 Day, '1W' for 1 Week Etc...

- Interval Cheat Codes = Accepted Intervals are [1, 3, 5, 15, 30, 45, 1H, 2H, 3H, 4H, 1D, 1W, 1M]
- (Note: NUmber without letters are in minutes, for example '1' means 1 Minute Timeframe / Interval)

5️⃣ Theme = light / dark (Note: if left empty then light theme will be used by default)

Example-1: 👉 To generate a snapshot of SBIN trading at NSE with 1 minute time frame, the command shall be

- With Default chart layout: /snap - nse sbin 1 light
- With your chart layout: /snap aSdfzXcV nse sbin 1 light

Example-2: 👉 To generate a snapshot of all Tickers/Symbols trading at BINANCE with 1 day time frame, the command shall be

- With Default chart layout: /snaplist - binance ethusdt btcusdt dogeusdt xrpusdt yfiiusdt bnbusdt 1d dark
- With your chart layout: /snaplist aSdfzXcV binance ethusdt btcusdt dogeusdt xrpusdt yfiiusdt bnbusdt 1d light"""

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=reply)


def snap(update, context):
    reply = snapshot(context.args)
    if 'tradingview.com/x/' in reply:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'🥳 Hooray 🥳 - The Requested SnapShot Is Generated: ✔️ 👇 : {reply}')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

def snaplist(update, context):
    reply = snapshotlist(context.args)
    if isinstance(reply, list):
        for snapurl in reply:
            if 'tradingview.com/x/' in snapurl:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f'🥳 Hooray 🥳 - The Requested SnapShots Are Generated: ✔️ 👇 : {snapurl}')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


def echo_text(update, context):
    reply = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


def sticker(update, context):
    reply = update.message.sticker.file_id
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=reply)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="❌ Sorry, I didn't understand that command. \n\nPlease type /help ❓ for more details. \n\nThank You. ✅")

def error(update, context):
    logger.error("Shit!! Update {} caused error {}".format(
        update, update.error))


def main():
    startbrowser = requests.get('http://localhost:3000/start-browser')
    response = startbrowser.text
    print(response)
    
    updater = Updater(token=TOKEN, use_context=True)  # take the updates
    dp = updater.dispatcher  # handle the updates

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("snap", snap))
    dp.add_handler(CommandHandler("snaplist", snaplist))
    # if the user sends text
    dp.add_handler(MessageHandler(
        Filters.text & (~Filters.command), echo_text))
    # if the user sends sticker
    dp.add_handler(MessageHandler(
        Filters.sticker & (~Filters.command), sticker))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    dp.add_error_handler(error)

    updater.start_polling()
    logger.info("Started...")
    updater.idle()


if __name__ == "__main__":
    main()
