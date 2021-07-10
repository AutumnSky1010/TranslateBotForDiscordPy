import discord
from discord.ext import commands
import discommands
import events
import os
class Core:
    def bot_run(self):
        token = os.environ['TRANSLATE_BOT_TOKEN']
        intents = discord.Intents().all()
        bot = commands.Bot(
            command_prefix = ',',
            intents = intents,
            help_command = None,
            activity = discord.activity.Game('「,help」でコマンド一覧')
        )
        bot.add_cog(discommands.TranslateCmds())
        bot.add_cog(discommands.CoreCmds())
        bot.add_cog(events.TranslateEvents())
        bot.add_cog(events.CoreEvents())
        bot.run(token)
if __name__ == '__main__':
    Core().bot_run()
