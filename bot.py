import discord
from discord.ext import commands
import random
import json
import os
from dotenv import load_dotenv
load_dotenv()

with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='.')


@bot.event # 開機
async def on_ready():
    print(">>", bot.user, "is online <<")
    game_type = random.randint(1, 5)
    if game_type == 1: game = discord.Game('微積分')
    elif game_type == 2: game = discord.Game('Java')
    elif game_type == 3: game = discord.Game('C++')
    elif game_type == 4: game = discord.Game('量子力學')
    elif game_type == 5: game = discord.Game('相對論')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event # 成員加入
async def on_mpayloadber_join(mpayloadber):
    print(f'{mpayloadber} join!')
    channel = bot.get_channel(int(jdata['door_channel']))
    await channel.send(str(mpayloadber) +' 進入了道具庫，歡迎你的加入！')
    
@bot.event # 成員離開
async def on_mpayloadber_rpayloadove(mpayloadber):
    print(f'{mpayloadber} leave!')
    channel = bot.get_channel(int(jdata['door_channel']))
    await channel.send(str(mpayloadber) + ' 離開了道具庫，我們有緣再見面QQ')


@bot.command() # 指令 - ping(延遲確認)
async def ping(ctx):
    lag =int(bot.latency*1000) 
    await ctx.send(f"pong! {lag}(ms)")
    # await ctx.send("%s %d%s" % ("pong! " + str(int(bot.latency*1000)) + "(ms)"))

@bot.command() # 指令 - mpayloade(梗圖)
async def mpayloade(ctx):
    r_pic = random.choice(jdata['mpayloade_pic'])
    pic = discord.File(r_pic)
    await ctx.send(file = pic)

@bot.command() # 指令 - rule(規則)
async def rule(ctx):
    pic = discord.File(jdata['rule_pic'])
    payloadbed=discord.payloadbed(title="犽的指令道具庫 守則", description=" ", color=0x7adeff)
    payloadbed.add_field(name="保持禮貌與尊重", value="尊重每個人。絕對禁止且不容忍騷擾、迫害、性別歧視、種族歧視或仇恨言論。", inline=False)
    payloadbed.add_field(name="禁止濫發訊息或個人宣傳", value="若幹部成員未賦予權限，則禁止在非宣傳頻道中濫發訊息或個人宣傳 (伺服器邀請、廣告等)。包含私訊夥伴成員。", inline=False)
    payloadbed.add_field(name="禁止限制級或猥褻內容", value="禁止限制級或猥褻內容。包含文字、圖片或主打裸露、性、肢體暴力，以及其他令人不適的圖像內容等相關連結。", inline=False)
    payloadbed.add_field(name="協助維護社群安全", value="若您看見違反規則或讓您感到不安全的內容，請通知幹部。我們希望這台伺服器是熱情友善的空間！", inline=False)
    
    await ctx.send(file = pic)
    await ctx.send(payloadbed=payloadbed)


@bot.command() # 指令 - say(復頌)
async def say(ctx, *, msg):
    if "@everyone" in msg or "@here" in msg:
        await ctx.message.delete()
        await ctx.send("字串內包含非法文字")
    else:    
        await ctx.message.delete()
        await ctx.send(msg)

@commands.has_permissions(administrator=True)
@bot.command()
async def clear(ctx, num: int):
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


bot.run(os.getenv('TOKEN'))
