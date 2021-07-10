import discord
from discord import mentions
from discord.ext import commands
from translate import Translate
class TranslateEvents(commands.Cog):
    name_and_lang = {}
    @commands.Cog.listener(name='on_message')
    async def auto_translate(self,message):
        if message.author.bot:return
        if not(message.author.id in TranslateEvents.name_and_lang):return
        if not(message.content == ',end' or ',start'  in message.content):
            result = Translate().get_result(
                message.content,
                TranslateEvents.name_and_lang[message.author.id],'')
            await message.reply(f'{message.author.display_name}:{result}')
class CoreEvents(commands.Cog):
    @commands.Cog.listener(name = 'on_message')
    async def print_log(self,message):
        guild_name = message.guild.name
        channel_name = message.channel.name
        author_name = message.author.display_name
        print(f'【<{guild_name}>{channel_name}】\n<{author_name}>{message.content}')
    @commands.Cog.listener(name = 'on_ready')
    async def ready(self):
        print('準備完了！！')
    

                