# BitCanna-balance_node
Basic script in python3 with Botogram to query info from a BitCanna masternode or fullnode on Linux via Telegram.
* We are amateur developers who love to create useful tools... if you want to help us with new ideas feel free to contribute.
* You can find us on Telegram at: [@BitcannaGlobal](https://t.me/BitcannaGlobal)

**Commands:**

* /getbalance - Show the balance of your wallet
* /getblockcount - Check this to know if your fullnode-masternode is synced
* /getlist - This will show the last Transactions in your wallet
* /getmasternode - This will show the online MASTERNODES
* /getpeers - This will show the online NODES (both)
* /getunspent - This will show amount to transfer in command-line to another address
* /getstakeinfo - Soon
* /subscribe - Subscribe your Telegram user to alerts
* /help - Show this help message.

**You need for running this script:**
* To have a Bot created in Telegram with @BotFather and a valid API KEY
* Linux system with a fullnode/masternode running and synced
* Python3 and pip3 installed 
* Botogram
* Set your config in the script (Token and route to binaries)

# Step-by-step guide:

**1) Create your own Bot in Telegram**

You can find the official Telegram instructions right here:
https://core.telegram.org/bots#6-botfather

**2) The linux masternode/fullnode side**

Download the script balance_node.py

When you run the script balance_node.py the first time it indicates that you need the Botogram library

bitcanna@mymasternode:~$ python3 balance_node.py
Traceback (most recent call last):
  File "balance_bot.py", line 4, in <module>
    import botogram
ImportError: No module named 'botogram'

The easy way is:

* $ sudo apt-get install python3-pip
* $ sudo pip3 install botogram2

If the last command fails, you can check this info:

* You can install botogram following this instructions:
https://github.com/python-botogram/botogram

* You can easily install it with pip (if needed) following this instructions:
https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3

Obtain balance_node:
git clone https://github.com/BitCannaCommunity/balance_node.git


Change your own setting, edit with nano or vi:  nano config.py
* You must change the path to the binaries
* Must also replace your API Telegram Bot Token 


Execute it!!!

```bitcanna@mymasternode:~$ python3 balance_node.py

12:49.27 -   INFO    - Your bot is now running!
12:49.27 -   INFO    - Press Ctrl+C to exit.
``` 
**3) Search the bot in Telegram (use the @alias) and /start it**
