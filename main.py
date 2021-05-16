from bs4 import BeautifulSoup as bs
import requests
import discord
from jikanpy import Jikan
import re


def vrvmalurl(vrvlink):
    jikan = Jikan()
    page = requests.get(vrvlink)
    soup = bs(page.content, 'html.parser')
    title = str(soup.find_all('title'))[8:-9]
    mallink = jikan.search('anime', title)['results'][0]['url']
    return mallink


def funimalurl(funilink):
    jikan = Jikan()
    title = funilink.replace('https://www.funimation.com/shows/', '').replace('-', ' ')[:-1].strip()
    mallink = jikan.search('anime', title)['results'][0]['url']
    return mallink


def netflixmalurl(netflixlink):
    url = re.findall('https:.*$', netflixlink)
    jikan = Jikan()
    page = requests.get(url[0])
    soup = bs(page.content, 'html.parser')
    title = str(soup.find_all('title'))[8:-19]
    mallink = jikan.search('anime', title)['results'][0]['url']
    return mallink


client = discord.Client()


@client.event
async def on_ready():
    pass


@client.event
async def on_message(message):
    if 'vrv' in message.content:
        await message.channel.send(vrvmalurl(message.content))
    elif 'funimation' in message.content:
        await message.channel.send(funimalurl(message.content))
    elif 'netflix' in message.content:
        await message.channel.send(netflixmalurl(message.content))


client.run('TOKEN')

