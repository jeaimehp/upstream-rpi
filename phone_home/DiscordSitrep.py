#need to check all pip installs on rpi
import datetime as dt
from datetime import datetime
import socket
import ctypes
import psutil
import time
import os
from os import statvfs
import subprocess
import discord
from discord.ext import commands


from dotenv import load_dotenv
# Imports enviromental variables
load_dotenv()

#######################################
# Discord  API setup                    #
#######################################
# !!!NOTE BEFORE UPLOADING TO REPOSITORY!!!
# Be sure to censor the access and secret keys from the "Discord  API Setup" Section if written in clear text!
# This example uses python-dotenv for this purpose with the TOKEN set in an .env file
# in the same directory as this python file with the format:
#
# TOKEN = "token_from_Discord"
#
# If using git/github ensure the .gitignore has ".env" so as to not include it in uploads
#
######################################

# These can be changed to clear text but it is not recommended
TOKEN = os.getenv("TOKEN")


description= 'situation report'
bot=commands.Bot(command_prefix='?penguin', description=description)

@bot.event
async def on_ready():
    channel = bot.get_channel(946864785969012827)
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    printedname = socket.gethostname()
    await channel.send(printedname + " is online!")
    await sitrep(channel)
    print('---------')

@bot.command()
async def rightnow(ctx):
    """gives time"""
    current = datetime.now()
    dt = current.strftime("%m/%d/%Y, %H:%M:%S")
    await ctx.send("Date, Time: " + dt)
    
@bot.command() 
async def hostinfo(ctx):    
    """gives hostname and IP address""" 
    domainname = socket.getfqdn()
    hostname = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    await ctx.send("Hostname: " + hostname)
    await ctx.send("IP Address: " + s.getsockname()[0])
    
@bot.command()
async def uptime(ctx):
    """length that pi has been connected to network"""
    seconds_elapsed = time.time() - psutil.boot_time()
    hours = seconds_elapsed//3600
    seconds = seconds_elapsed%3600
    minutes = seconds//60
    seconds = seconds%60

    await ctx.send("Uptime: " + str(format(int(hours),"02d")) + ":" + str(format(int(minutes),"02d")) + ":" + str(format(int(seconds),"02d")))
    

@bot.command()
async def diskspace(ctx):
    """gives disk space info"""
    obj_Disk = psutil.disk_usage('/')

    await ctx.send("Total (in GB): " + str(obj_Disk.total / (1024.0 ** 3)))
    await ctx.send("Used (in GB): " + str(obj_Disk.used / (1024.0 ** 3)))
    await ctx.send("Free (in GB): " + str(obj_Disk.free / (1024.0 ** 3)))
    await ctx.send("Percent used: " + str(obj_Disk.percent) + "%")

@bot.command()
async def signalStrength(ctx):
    strength = subprocess.run(["iwconfig wlan0 | grep Link"], capture_output = True, text = True).stdout
    await ctx.send(strength)

@bot.command()
async def storedWav(ctx):
    storedWav = subprocess.run(["find upstream-rpi/sound/ -iname '*.wav' | wc -l "], captureoutput= True, text = True).stdout
    await ctx.send("Number of audio files in memory: " + storedWav)
@bot.command()
async def sitrep(ctx):
    """full situation report of rpi"""
    current = datetime.now()
    dt = current.strftime("%m/%d/%Y, %H:%M:%S")
    await ctx.send("Date, Time: " + dt)
    
    domainname = socket.getfqdn()
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    await ctx.send("Hostname: " + hostname)
    await ctx.send("IP Address: " + s.getsockname()[0])

    seconds_elapsed = time.time() - psutil.boot_time()
    hours = seconds_elapsed//3600
    seconds = seconds_elapsed%3600
    minutes = seconds//60
    seconds = seconds%60
    await ctx.send("Uptime: " + str(format(int(hours),"02d")) + ":" + str(format(int(minutes),"02d")) + ":" + str(format(int(seconds),"02d")))

    obj_Disk = psutil.disk_usage('/')
    await ctx.send("Total: " + str(obj_Disk.total / (1024.0 ** 3)))
    await ctx.send("Used: " + str(obj_Disk.used / (1024.0 ** 3)))
    await ctx.send("Free: " + str(obj_Disk.free / (1024.0 ** 3)))
    await ctx.send("Percent used: " + str(obj_Disk.percent) + "%")
    """ 
    strength = subprocess.run(["iwconfig wlan0 | grep Link"], capture_output = True, text = True).stdout
    await ctx.send(strength)

    storedWav = subprocess.run(["find upstream-rpi/sound/ -iname '*.wav' | wc -l "], captureoutput= True, text = True).stdout
    await ctx.send("Number of audio files in memory: " + storedWav)
    """
bot.run(TOKEN)

