import discord
from discord.ext import commands
from discord.ui import Button
import random
import json
import os
import time
import random
from dotenv import load_dotenv
load_dotenv()

with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='.')
MAX_GUESS = 10
flag = True
ans_list = []
guess_list = []


@bot.event  # 開機
async def on_ready():
    print(">>", bot.user, "is online <<")
    game_type = random.randint(1, 5)
    if game_type == 1:
        game = discord.Game('微積分')
    elif game_type == 2:
        game = discord.Game('Java')
    elif game_type == 3:
        game = discord.Game('C++')
    elif game_type == 4:
        game = discord.Game('量子力學')
    elif game_type == 5:
        game = discord.Game('相對論')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event  # 成員加入
async def on_mpayloadber_join(mpayloadber):
    print(f'{mpayloadber} join!')
    channel = bot.get_channel(int(jdata['door_channel']))
    await channel.send(str(mpayloadber) + ' 進入了道具庫，歡迎你的加入！')


@bot.event  # 成員離開
async def on_mpayloadber_rpayloadove(mpayloadber):
    print(f'{mpayloadber} leave!')
    channel = bot.get_channel(int(jdata['door_channel']))
    await channel.send(str(mpayloadber) + ' 離開了道具庫，我們有緣再見面QQ')


@bot.command()  # 指令 - ping(延遲確認)
async def ping(ctx):
    """
    輸入這個指令可以讓您確認機器人是否在線！
    也可以知道您與機器人的延遲。
    """
    lag = int(bot.latency*1000)
    await ctx.send(f"pong! {lag}(ms)")
    # await ctx.send("%s %d%s" % ("pong! " + str(int(bot.latency*1000)) + "(ms)"))


@bot.command()  # 指令 - meme(梗圖)
async def meme(ctx):
    """
    可以看看梗圖...然後就沒了:)
    """
    r_pic = random.choice(jdata['meme_pic'])
    pic = discord.File(r_pic)
    await ctx.send(file=pic)


@bot.command()  # 指令 - rule(規則)
@commands.has_permissions(administrator=True)
async def rule(ctx):
    """
    [管理員專用]
    顯示規則文字
    """
    pic = discord.File(jdata['rule_pic'])
    payloadbed = discord.payloadbed(
        title="犽的指令道具庫 守則", description=" ", color=0x7adeff)
    payloadbed.add_field(
        name="保持禮貌與尊重", value="尊重每個人。絕對禁止且不容忍騷擾、迫害、性別歧視、種族歧視或仇恨言論。", inline=False)
    payloadbed.add_field(
        name="禁止濫發訊息或個人宣傳", value="若幹部成員未賦予權限，則禁止在非宣傳頻道中濫發訊息或個人宣傳 (伺服器邀請、廣告等)。包含私訊夥伴成員。", inline=False)
    payloadbed.add_field(
        name="禁止限制級或猥褻內容", value="禁止限制級或猥褻內容。包含文字、圖片或主打裸露、性、肢體暴力，以及其他令人不適的圖像內容等相關連結。", inline=False)
    payloadbed.add_field(
        name="協助維護社群安全", value="若您看見違反規則或讓您感到不安全的內容，請通知幹部。我們希望這台伺服器是熱情友善的空間！", inline=False)

    await ctx.send(file=pic)
    await ctx.send(payloadbed=payloadbed)


@bot.command()  # 指令 - say(複誦)
async def say(ctx, *, msg):
    """
    機器人會代替你說話
    """
    if "@everyone" in msg or "@here" in msg:
        await ctx.message.delete()
        await ctx.send("字串內包含非法文字")
    else:
        await ctx.message.delete()
        await ctx.send(msg)


@commands.has_permissions(administrator=True)
@bot.command()
async def clear(ctx, num: int):
    """
    [管理員專用]
    可以批量刪除訊息
    """
    await ctx.channel.purge(limit=num + 1)


@bot.event
async def on_raw_reaction_add(payload):
    # print(payload.mpayloadber, payload.payloadoji)
    # print(payload.channel_id)
    if str(payload.emoji) == '<:check:1036979544126656572>' and payload.channel_id == 1036064012791726140:
        # if 1 == 1:
        print('1')
        guild = bot.get_guild(payload.guild_id)
        role = guild.get_role(1036960296239116368)
        await payload.member.add_roles(role)


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.green, emoji="✅")
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello world!")


@bot.command()
@commands.has_permissions(administrator=True)
async def test_button(ctx):
    """
    [管理員專用]
    召喚測試用的按鈕（此指令為之後製作按鈕的範例）
    """
    view = Menu()
    await ctx.reply(view=view)
bot.run(os.getenv('TOKEN'))
# hi
