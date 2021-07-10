import discord
from discord.ext import commands
import lang
import translate
import events
class TranslateCmds(commands.Cog):
    @commands.command()
    async def langs(self,ctx):
        result_embed = discord.Embed()
        lang_code = ''
        lang_name = ''
        for name,code in lang.LangData.langs.items():
            lang_name += f'{name}\n'
            lang_code += f'{code}\n'
        result_embed.color = discord.Colour.green()
        result_embed.title = '言語名、言語コード一覧'
        result_embed.description = '翻訳するコマンドで言語を指定するときに使える言語です。'
        result_embed.add_field(name = '言語名',value=lang_name)
        result_embed.add_field(name = '言語コード',value=lang_code)
        await ctx.send(embed = result_embed)
    @commands.command()
    async def tr(self,ctx:commands.Context,*args):
        tr = translate.Translate()
        language = lang.Language()
        arglist = list(args)
        result = ''
        #引数の言語が日本語指定か調べる
        for i,arg in enumerate(arglist):
            if i == 0:continue
            if not str(arg).isascii():
                #言語コード表記に変える
                arglist[i] = language.to_lang_code(arg)
        if len(args) == 3:
            result = tr.get_result(arglist[0],arglist[1],arglist[2])
        elif len(args) == 2:
            result = tr.get_result(arglist[0],arglist[1],'')
        else:
            await ctx.send('引数が不適切です。\n半角スペースが含まれる文は"  "で囲って下さい。')
            return
        await ctx.send(f'【翻訳前】**__{arglist[0]}__**\n          ⇓\n【翻訳後】__**{result}**__')
    @commands.command()
    async def start(self,ctx,*args:str):
        langdic = lang.LangData().langs
        langs = lang.Language()
        if len(args) != 1:
            await ctx.send('引数の数が不適切です。')
            return
        #言語コードで指定された場合
        if args[0].isascii():
            if not(args[0] in langdic.values()):
                await ctx.send('この言語には対応していません。')
                return
            events.TranslateEvents.name_and_lang[ctx.message.author.id] = args[0]
        else:#言語名で指定された場合
            if not(args[0] in langdic.keys()):
                await ctx.send('この言語には対応していません。')
                return
            events.TranslateEvents.name_and_lang[ctx.message.author.id] = langs.to_lang_code(args[0])
        langname = langs.to_lang_name(args[0])
        await ctx.reply(f'{ctx.message.author.display_name}さんのメッセージは自動で{langname}に翻訳されます。')
    @commands.command()
    async def end(self,ctx):
        #スタート済みか判定
        if not(ctx.message.author.id in events.TranslateEvents.name_and_lang.keys()):
            ctx.send('まだ自動翻訳機能をonにしていないため、終了することができませんでした。')
            return
        events.TranslateEvents.name_and_lang.pop(ctx.message.author.id)
        await ctx.reply(f'{ctx.message.author.display_name}さんの自動翻訳が解除されました。')
class CoreCmds(commands.Cog):
    @commands.command()
    async def help(self,ctx):
        result = ''
        commands_dic = {
            '```,tr [翻訳したい文章] [翻訳後の言語] [翻訳前の言語]\n'+
            ',tr [翻訳したい文章] [翻訳後の言語]```\n':
            '翻訳したい文章を翻訳後の言語に翻訳します。\n'+
            '半角スペースがある文章は`" "`で囲ってください。\n'+
            '例) ```,tr "this is a pen." ja```\n',

            '\n```,start [翻訳後の言語]```\n':'自動翻訳機能をスタートします。\n',
            '\n```,end```\n':'自動翻訳機能を終了します。\n',
            '\n```,langs```\n':'翻訳可能な言語の一覧を送信します。\n'
        }
        for command in commands_dic:
            result += command + commands_dic[command]
        #埋め込みを作成する
        embed = discord.Embed()
        embed.title = 'コマンド一覧'
        embed.color = discord.Colour.from_rgb(245, 229, 107)
        embed.description = result
        await ctx.send(embed=embed)

