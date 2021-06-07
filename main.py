from bs4 import BeautifulSoup as bs
import requests
import discord
from jikanpy import Jikan
import re


def vrv(vrvlink):
    jikan = Jikan()
    page = requests.get(vrvlink)
    soup = bs(page.content, 'html.parser')
    title = str(soup.find_all('title'))[8:-9]
    mallink = jikan.search('anime', title)['results'][0]['url']
    return mallink


def funimation(funilink):
    jikan = Jikan()
    title = funilink.replace('https://www.funimation.com/shows/', '').replace('-', ' ')[:-1].strip()
    mallink = jikan.search('anime', title)['results'][0]['url']
    return mallink


def crunchyroll(crunchylink):
    jikan = Jikan()
    title = crunchylink.replace('https://www.crunchyroll.com/', '').replace('-', ' ').strip()
    mallink = jikan.search('anime', title)['results'][0]['url']
    return mallink


def netflix(netflixlink):
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
        await message.channel.send(vrv(message.content))
    elif 'funimation' in message.content:
        await message.channel.send(funimation(message.content))
    elif 'crunchyroll' in message.content:
        await message.chanel.send(crunchyroll(message.content))
    elif 'netflix' in message.content:
        await message.channel.send(netflix(message.content))

client.run('TOKEN')
