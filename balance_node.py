#python3
import datetime
import os
import botogram
import json

from config import token, path_to_bin

bot = botogram.create(token)
bot.about = "Balance BOT for your own fullnode-masternode. \nIf you found any bugs or have suggestions for new functionalities...\nPlease contact us!"
bot.owner = "@MrSteelBCNA and/or @Raul_BitCannaES"
#==========================================================================
@bot.command("getbalance")
def getbalance_command(chat, message, args):
    """Show the balance of your wallet"""
    get_balance = os.popen(path_to_bin + "/bitcanna-cli getbalance").read()
    print("Result:", get_balance)
    balance = str(get_balance)
    chat.send("The current balance is "+balance+" BCNA")
#==========================================================================
@bot.command("getblockcount")
def getblockcount_command(chat, message, args):
    """Check this to know if your fullnode-masternode is synced"""
    get_block = os.popen(path_to_bin + "/bitcanna-cli getblockcount").read()
    print("Result:", get_block)
    block = str(get_block)
    chat.send("The current Block is "+block)
#==========================================================================
@bot.command("getlist")
def getlist_command(chat, message, args):
    """This will show the last Transactions in your wallet"""
    msg = ""
    get_last = os.popen(path_to_bin + "/bitcanna-cli listtransactions").read()
    loaded_json = json.loads(get_last)
    for tx in loaded_json:
        date_time =  datetime.datetime.fromtimestamp(tx['blocktime']).strftime('%c')
        msg = msg + tx['category'] + " BCNA: " + str(tx['amount']) + " at " + date_time + "\n"
    print (msg)
    chat.send(msg)
#==========================================================================
@bot.command("getmasternode")
def getmasternode_command(chat, message, args):
    """This will show the online MASTERNODES"""
    get_masternodes = os.popen(path_to_bin + "/bitcanna-cli masternode list").read()
    loaded_json = json.loads(get_masternodes)
    msg = ""
    count = 0
    chat.send ("List of online MASTERNODES") 
    print ("List of online MASTERNODES")
    print ("==========================")
    for tx in loaded_json:
        msg = msg + "IP: " +  tx + "\n"
        count = count + 1
    print (msg + "\nTotal: " + str(count))
    chat.send(msg + "\nTotal: " + str(count))
#==========================================================================
@bot.command("getpeers")
def getpeers_command(chat, message, args):
    """This will show the online NODES (both)"""
    get_nodes = os.popen(path_to_bin + "/bitcanna-cli getpeerinfo").read()
    loaded_json = json.loads(get_nodes)
    msg = ""
    count = 0
    file_peers = os.path.join(path_to_bin + '/peers.txt') 
    chat.send ("Building a list...") 
    print ("List of online NODES")
    print ("==========================")
    for tx in loaded_json:
        msg = msg + "IP: " +  tx["addr"] + ", version: " + tx["subver"] + "\n"
        count = count + 1 
    print (msg + "\nTotal: " + str(count))
    with open(file_peers, 'w') as f:
        f.write(msg+ "\nTotal: " + str(count))
    chat.send_file(path=file_peers, caption='This file contains all peers connected to your masternode/fullnode')
#==========================================================================
@bot.command("getunspent")
def getunspent_command(chat, message, args):
    """This will show amount to transfer in command-line to another address"""

    total = 0
    msg = ""
    get_last = os.popen(path_to_bin + "/bitcanna-cli listunspent").read()
    loaded_json = json.loads(get_last)
    chat.send ("Unspent inputs to transfer\n======================")
    for tx in loaded_json:
        if  tx['amount'] == 3.30000000: # > 2.6 for fullnode
            msg = msg + "Mint: " + str(tx['spendable']) + " BCNA: " + str(tx['amount']) + "\n"
            total = total + tx['amount']
        else:
            msg =  msg + 'Other: '  + str(tx['spendable']) + " BCNA: " + str(tx['amount']) + "\n"
    print(msg) #Is printed in console , could be saved in a file and sent by telegram
    #chat.send (msg) #if there are a lot of inputs Telegram can't handle in a message
    chat.send ("Make your transfer with " + (str(total)) + " BCNA")
#==============================================================================
@bot.prepare_memory
def init(shared):
    shared["subs"] = []

@bot.command("subscribe")
def subscribe_command(shared, chat, message, args):
    """Subscribe to the hourly daemon checking"""
    subs = shared["subs"]
    subs.append(chat.id)
    shared["subs"] = subs

@bot.timer(3600) #every hour
def checker(bot, shared):
    get_info = os.popen(path_to_bin + "/bitcanna-cli getinfo").read()
    if get_info.find('error:') == '': #-1 is running
         for chat in shared["subs"]:
            bot.chat(chat).send("Hey! your BitCanna daemon is down!")
         starting = os.popen(path_to_bin + "/bitcannad -daemon").read()
    else:
        print('Daemon is running')
        #bot.chat(chat.id).send(starting)
#==============================================================================


# This runs the bot, until ctrl+c is pressed
if __name__ == "__main__":
    bot.run()
