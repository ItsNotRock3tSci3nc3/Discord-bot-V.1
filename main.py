from discord.ext import commands

bot = commands.Bot(command_prefix='r/')

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def test(ctx):
    pass

# or:

@commands.command()
async def test(ctx):
    pass

@bot.command(name='list')
async def _list(ctx, arg):
    pass


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


bot.add_command(test)
