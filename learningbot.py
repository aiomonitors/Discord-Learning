import discord
from discord.ext import commands
'''
@navrxo, @perceptionio, @navrx0 - http://navr.me
What do I want in return? Nothing but knowing
that you truly are learning! Feel free to shout me out on twitter
@navrx0
'''

#CONFIGURE YOUR BOT PREFIX
bot_prefix = '!'

#CONFIGURE YOUR TOKEN
TOKEN = ''

#Create an instance of the bot class. Your bot in this code will be 'bot'
bot = commands.Bot(command_prefix = bot_prefix)

#There are events, and there are commands. An event is when something happens, either in discord, or with the vot
#Commands are when a user tells the bot to do something

@bot.event
#Defines what happens when the bot is 'ready' - You can set this to anything you want. 
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # Prints the name of your bot

#------------FUNCTIONS------------------------
# I am predefining functions so my code is less sloppy.
def paypal(number):
    fees = 1 - .029
    number = (number * fees - .3)
    #rounds number two digits
    numberrounded = round(number, 2)
    return(numberrounded)

def stock_x1(number):
    return(number * .875)

def stock_x2(number):
    return(number * .88)

def stock_x3(number):
    return(number * .885)
    
def stock_x4(number):
    return(number * .89)

#--------BOT COMMANDS-----------------
@bot.command(pass_context = True)
#making a command is like this 'async def <yourcommandname>(ctx): 
#Note yourcommandname should be one word
async def ping(ctx):
    #TO reference parts of the command. everything is now an object of the ctx class
    #EX: to refer to author name:ctx.message.author 
    #TO get author id for example, it would be 
    #ctx.message.author.id

   # The way to make the bot say something, you use await bot.say("YOURTEXTHERE")
    await bot.say("Ping " + ctx.message.author.name)

@bot.command(pass_context=True)
async def embedstructure(ctx):
    author = ctx.message.author

    #create and reference and embed projectsw
    embed = discord.Embed(
        title = "This is a title",
        description = "This is a description",
        color = 0x9400D3
    )
    embed.set_author(name = "THIS IS AN AUTHOR")
    embed.add_field(name = "Name of field", value = "This is the value", inline = True)
    embed.add_field(name = "Inline", value = "These two are inline fields", inline = True)
    embed.add_field(name = "Inline", value = "This field and the one below are inline=false", inline=False)
    embed.add_field(name = "Inline", value = "This field and the one above are inline=false", inline = False)
    embed.set_footer(text = "This is a footer")

    #how and embed should be sent
    await bot.say(embed=embed)

@bot.command(pass_context=True)
#Here i will be taking input, so now i pass in ctx and a regular argument as the function argument
async def fees(ctx, price):
    #Now i will call each function on the price, and store in a variable
    #"price" is currently a string. i will convert it to an integer like so.
    price = int(price)
    #Now i store all fees
    #I enclose each with "str()" because otherwise the embed will not take it. It must be a string
    paypalfees = str(paypal(price))
    stockx1 = str(stock_x1(price))
    stockx2 = str(stock_x2(price))
    stockx3 = str(stock_x3(price))
    stockx4 = str(stock_x4(price))

    #configure the embed again
    embed = discord.Embed(
        title = "Fees Calculator",
        color = 0x9400D3
    )
    embed.add_field(name = "Paypal", value = paypalfees, inline = False)
    embed.add_field(name = "StockX Seller LVL 1", value = stockx1, inline = False)
    embed.add_field(name = "StockX Seller LVL 2", value = stockx2, inline = False)
    embed.add_field(name = "StockX Seller LVL 3", value = stockx3, inline = False)
    embed.add_field(name = "StockX Seller LVL 4", value = stockx4, inline = False)
    embed.set_footer(text = "@navrxo, @PerceptionIO, @navrx0 || http://navr.me")

    await bot.say(embed=embed)

#TO RUN THE BOT, YOU DO
bot.run(TOKEN)

