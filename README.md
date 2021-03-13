# TradingviewSnapshotBot [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
This is an unofficial TradingviewSnapshotBot 🤖, It can generate Tradingview Chart Snapshots 📊 of your choice and send it over telegram.

![TradingView](https://raw.githubusercontent.com/ShabbirHasan1/TradingviewSnapshotBot/main/images/bot.gif)

## Usage
❗️⚠️ Please type /snap or /snaplist first to initate command reception.

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
  - With Default chart layout: /snap - nse sbin 1 dark    or    /snap - nse sbin 1 light
  - With your chart layout: /snap aSdfzXcV nse sbin 1 light     or /snap aSdfzXcV nse sbin 1 dark

  Example-2: 👉 To generate a snapshot of all Tickers/Symbols trading at BINANCE with 1 day time frame, the command shall be
  - With Default chart layout: /snaplist - binance ethusdt btcusdt dogeusdt xrpusdt yfiiusdt bnbusdt 1d dark
  - With your chart layout: /snaplist aSdfzXcV binance ethusdt btcusdt dogeusdt xrpusdt yfiiusdt bnbusdt 1d light

  Example-3: 👉 To generate a snapshot of all Tickers/Symbols trading at NSE-NFO with 1 day time frame, the command shall be
  - With Default chart layout: /snaplist - nse nifty finnifty banknifty aartiind adanient adaniports amarajabat apollotyre acc ashokley asianpaint auropharma ambujacem bajaj-auto bankbaroda balkrisind bataindia bergepaint bel bharatforg bhartiartl biocon bhel boschltd britannia cadilahc canbk cholafin cipla colpal coalindia concor cumminsind dlf dabur divislab drreddy escorts federalbnk glenmark godrejprop havells gmrinfra hdfcamc hdfcbank hindunilvr icicibank igl industower ioc hcltech hdfc itc jindalstel jswsteel hindalco l&tfh ibulhsgfin icicigi lalpathlab icicipruli lichsgfin lt lupin indigo m&m m&mfin manappuram maruti infy mfsl nationalum nestleind nmdc pageind jublfood pel pidilitind pnb mindtree mothersumi pvr sail sbin siemens muthootfin srf naukri srtransfin sunpharma tataconsum tatapower tcs techm ntpc torntpower vedl ongc wipro petronet apollohosp powergrid recltd reliance bajfinance tatasteel bpcl titan torntpharm tvsmotor coforge eichermot exideind gail godrejcp grasim hdfclife heromotoco axisbank hindpetro bajajfinsv idea idfcfirstb kotakbank marico mgl mrf pfc rblbank indusindbk sbilife suntv tatachem tatamotors ultracemco mcdowell-n voltas upl zeel ramcocem shreecem ubl bandhanbnk alkem aplltd aubank cub deepakntr granules gujgasltd irctc lti ltts mphasis nam-india navinfluor pfizer piind trent 1d dark

## Running The App
  After Cloning the repo, You need to update the telegram bot token in tvsnapshotbot.py line-11 ```TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"``` with your bot token obtained from telegram @botfather

  ```
  git clone https://github.com/ShabbirHasan1/TradingviewSnapshotBot.git
  cd TradingviewSnapshotBot
  chmod +x start.sh index.js tvsnapshotbot.py
  ./start.sh
  ```
### Stop The APP
  ``` Press CTRL + C```

## Requirements
 - Python 3.8 or newer.
 - [Requests](https://pypi.org/project/requests/), Included in installation.
 - [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) (```pip install python-telegram-bot```)
 - Node Js v15.11.0 or newer ```sudo apt install nodejs```
 - ExpressJs 4.17.1 or newer ```npm install express --save```
 - puppeteer 8.0.0 or newer ```npm install puppeteer -g```

## Issue
 Found a bug? Want to ask something? Just create an issue and I'll help you.
  
## Warning
 Trading (especially using an automated program) is a dangerous activity. Do not use TradingView's analysis / snapshots to trade automatically without your financial advisor's supervision. I am not responsible for any financial loss.

## Contributing
 You may fork this repository or submit a pull request. Any pull request (documentation, bug fix, features, etc) are welcomed.

## License
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
