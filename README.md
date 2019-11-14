# BitCanna-balance_node
Basic script in python3 with Botogram to query info at BitCanna masternode or fullnode on Linux from Telegram

**Commands:**

*/getbalance - Show the balance of your wallet
*/getblockcount - Check this to know if your fullnode-masternode is synced
*/getlist - This will show the last Transactions in your wallet
*/getmasternode - This will show the online MASTERNODES
*/getpeers - This will show the online NODES (both)
*/getunspent - This will show amount to transfer in command-line to another address
*/getstakeinfo - Soon
*/help - Show this help message.

**You need for running this script:**
* To have a Bot created in Telegram with @BotFather and a valid API KEY
* Linux system with a fullnode/masternode running and synced
* Python3 and pip3 installed 
* Botogram
* Set your config in the script (Token and route to binaries)

# Step-by-step guide:

**1) To have a Bot created in Telegram with @BotFather and a valid API KEY. Telegram side.**

You must create a Telegram bot using the @BotFather. 
* Call him, /start and follow this steps:

* /newbot → And put a cool name for your bot. This name could have spaces like “MN MegaBot”
  
    After the name you must put an Alias or ID for your bot, and must end in _bot or bot, as example: MN_Mega_Bot
    When finish, it showed the TOKEN for your bot (like a unique password to work on Telegram )
    If you need to obtain again the TOKEN, edit the Bot, or set advanced params you can typing /mybot

Selecting API Token you will get again the TOKEN key, take note it, needed to end the set-up.
Also you must note it the name of the bot and alias, in my example @myfullnodebot


**2) The linux masternode/fullnode side**

Download the script balance_node.py, choose one of the following ways:

a) Download the script balance_node.py in and unzip it 
  * $ wget https://github.com/RaulBernal/BitCanna-balance_node/archive/master.zip
  * $ unzip master.zip
  * $ cd master

b) or clone with git
  * $ git clone https://github.com/RaulBernal/BitCanna-balance_node.git
  * $ cd BitCanna-balance_node

When you run the script balance_node.py the first time it indicates that you need the Botogram library

bitcanna@mymasternode:~$ python3 balance_node.py
Traceback (most recent call last):
  File "balance_bot.py", line 4, in <module>
    import botogram
ImportError: No module named 'botogram'

The easy way is:

* $ sudo apt-get install python3-pip
* $ sudo pip3 install botogram2

If the last fail you can check this info:

* You can install botogram following this instructions:
https://github.com/python-botogram/botogram

* You can easily install it with pip (if it needed) following this instructions:
https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3


Change your own settings in balance, edit with nano or vi:  nano balance_node.py
* You must change the route to the binaries
* Must replace also your Token 


Execute it!!!

bitcanna@mymasternode:~$ python3 balance_node.py

12:49.27 -   INFO    - Your bot is now running!
12:49.27 -   INFO    - Press Ctrl+C to exit.

**3) Search the bot in Telegram (use the @alias) and /start it**
