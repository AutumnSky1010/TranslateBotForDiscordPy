import discord
from discord import mentions
from discord.ext import commands
from translate import Translate
class TranslateEvents(commands.Cog):
    name_and_lang = {}
    def __init__(self,bot:commands.Bot):
        self.bot = bot
    @commands.Cog.listener(name='on_message')
    async def auto_translate(self,message):
        if message.author.bot:return
        if not(message.author.id in TranslateEvents.name_and_lang):return
        if not(message.content == ',end' or ',start'  in message.content):
            result = Translate().get_result(
                message.content,
                TranslateEvents.name_and_lang[message.author.id],'')
            await message.reply(f'{message.author.display_name}:{result}')
                