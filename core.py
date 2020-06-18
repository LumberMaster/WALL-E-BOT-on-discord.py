import datetime
from config import *
import json
import discord
from discord.ext import commands
import random
# from discord.ext.commands import Bot


bot = commands.Bot(command_prefix = '!')

#-----------------------------------------------------------
#                    События
#-----------------------------------------------------------
@bot.event
async def on_ready():
    today = datetime.datetime.today()
    print(f'[BOT][{today.strftime("%d.%m.%Y  %H:%M")}] Online')
    LOGS = open('LOGS.txt', 'a', encoding='utf-8')
    raw = str(f'[BOT][{today.strftime("%d.%m.%Y  %H:%M")}] Online \n')
    LOGS.write(raw)
    LOGS.close()

@bot.event
async def on_disconnect():
    today = datetime.datetime.today()
    print(f'[BOT][{today.strftime("%d.%m.%Y  %H:%M")}] Offline')
    LOGS = open('LOGS.txt', 'a', encoding='utf-8')
    raw = str(f'[BOT][{today.strftime("%d.%m.%Y  %H:%M")}] Offline \n')
    LOGS.write(raw)
    LOGS.close()

@bot.event
async def on_message(msg):
    filename = "bank.txt"

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    while i < len(players):
        if str(players[i]['id']) == str(msg.author.id):
            players[i]['money'] = players[i]['money'] + players[i]['salary']
            players[i]['exp'] = players[i]['exp'] + 1
            break
        i += 1

    myfilew = open(filename, mode="w", encoding="utf-8")
    json.dump(players, myfilew)
    myfilew.close()
    await bot.process_commands(msg)

@bot.event
async def on_command_error(ctx,error):
    await ctx.send(ctx.message)
    await ctx.send(error)

# @bot.event
# async def on_connect(user):
#     print(f'[connect] {user.name}')
#

# @bot.event
# async def on_disconnect(user):
#     print(f'[disconnect] {user.name}')


@bot.event
async def on_raw_reaction_add(reaction):
    POSTID = 708320806643564641
    # print(reaction)
    print(discord.Guild.roles)
    if reaction.message_id == POSTID:
        if reaction.emoji.name == '🚹': # 🚹 man
            role = discord.utils.get(discord.Guild.roles, name="Мальчик💙")
            await bot.add_roles(reaction.user_id, role)
        if reaction.emoji.name  == '🚺': # 🚺 woman
            role = discord.utils.get(discord.Guild.roles, name="Девочка♥️")
            await bot.add_roles(reaction.user_id, role)

    # print(reaction.message)
    # print(reaction.emoji)
    # print(user.name)


#-----------------------------------------------------------
#                    Команды в чате
#-----------------------------------------------------------
@bot.command()
async def hello(ctx):
    await ctx.send(f'Здарова мой сладенький {ctx.author} ')


@bot.command()
async def say(ctx,*, msg):
    today = datetime.datetime.today()

    await ctx.message.delete()
    print(f'[BOT][SAY][{today.strftime("%d.%m.%Y  %H:%M")}] | {msg} | author - { ctx.author }   ')
    await ctx.send(f'{msg}')

    LOGS = open('LOGS.txt', 'a', encoding='utf-8')
    raw = str(f'[BOT][SAY][{today.strftime("%d.%m.%Y  %H:%M")}] | {msg} | author - { ctx.author }   \n')
    LOGS.write(raw)
    LOGS.close()

# @bot.command()
# async def help(ctx):
#     pass
@bot.command()
async def shop(ctx):
    await ctx.send(ctx.message)
    await ctx.send(ctx.command)
    await ctx.send(ctx.args)

@bot.command()
async def buy(ctx):
    pass

@bot.command()
async def pay(ctx):
    pass

@bot.command()
async def write(ctx, *,msg):
    arrMSG = []
    msg = msg.lower()
    arrALPH = {
        ' ':' ',
        'a':':regional_indicator_a:',
        'b':':regional_indicator_b:',
        'c':':regional_indicator_c:',
        'd':':regional_indicator_d:',
        'e':':regional_indicator_e:',
        'f':':regional_indicator_f:',
        'g':':regional_indicator_g:',
        'h':':regional_indicator_h:',
        'i':':regional_indicator_i:',
        'j':':regional_indicator_j:',
        'k':':regional_indicator_k:',
        'l':':regional_indicator_l:',
        'm':':regional_indicator_m:',
        'n':':regional_indicator_n:',
        'o':':regional_indicator_o:',
        'p':':regional_indicator_p:',
        'q':':regional_indicator_q:',
        'r':':regional_indicator_r:',
        's':':regional_indicator_s:',
        't':':regional_indicator_t:',
        'u':':regional_indicator_u:',
        'v':':regional_indicator_v:',
        'w':':regional_indicator_w:',
        'x':':regional_indicator_x:',
        'y':':regional_indicator_y:',
        'z':':regional_indicator_z:',
        '0':'0️⃣',
        '1':'1️⃣',
        '2':'2️⃣',
        '3':'3️⃣',
        '4':'4️⃣',
        '5':'5️⃣',
        '6':'6️⃣',
        '7':'7️⃣',
        '8':'8️⃣',
        '9':'9️⃣',
    }

    message = '>>> '

    i = 0
    while i < len(msg):
        arrMSG.append(msg[i])
        i+=1

    i = 0
    while i < len(arrMSG):
        message += arrALPH[arrMSG[i]]
        i+=1

    await ctx.send(message)

@bot.command()
async def commands(ctx):
    message = '>>> !hello - Выводит "Hello (Ваш ник)"\n'
    message += '!commands - Выводит список доступных команд\n'
    message += "!say текст - Бот печатает ваш текст\n"
    message += "!clear - Очищает историю чата(Только для админа)\n"
    message += "!register - Создаёт аккаунт на сервере\n"
    message += "!profile - Информация об аккаунте\n"
    message += "!balance - Баланс на карте\n"
    message += "!lvlup - Увеличить свой лвл(За новый лвл дают больше денег с 1 сообщения)\n"
    message += "!crash 'Число от 1 до 8' 'Кол-во денег' - Игра crash\n"
    message += "!casino 'Кол-во денег' - Игровой автомат 3 в ряд\n"
    await ctx.send(message)

@bot.command()
async def register(ctx):
    filename = "bank.txt"

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    register = True

    while i < len(players):
        # print(str(i) + "      " + str(players[i]['id']) + '       ' + str(ctx.author.id))
        if str(players[i]['id']) == str(ctx.author.id):
            register = False
            await ctx.send('Ваш профиль уже существует')
            break
        i += 1

    if register:
        myfilew = open(filename, mode="w", encoding="utf-8")
        player = {
            'nick' : f'{ctx.author.name}',
            'id' : f'{ctx.author.id}',
            'salary': 0.5,
            'money': 0,
            'exp': 0,
            'lvl': 0,
            'rep': 0
        }
        players.append(player)
        json.dump(players, myfilew)
        myfilew.close()
        await ctx.send('Профиль создан')


@bot.command()
async def profile(ctx):
    filename = "bank.txt"

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    while i < len(players):
        if str(players[i]['id']) == str(ctx.author.id):
            msg = f'>>> Профиль:    {players[i]["nick"]}\n'
            msg += f'Уровень:   {players[i]["lvl"]}    🌍\n'
            msg += f'Опыт:      {players[i]["exp"]}    🔮\n'
            msg += f'Баланс:    {int(players[i]["money"])}  ₽\n'
            await ctx.send(msg)
            break
        i += 1

@bot.command()
async def balance(ctx):
    filename = "bank.txt"

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    while i < len(players):
        if str(players[i]['id']) == str(ctx.author.id):
            money = int(players[i]['money'])
            break
        i += 1

    await ctx.send(f"{money} ₽")

@bot.command()
async def lvlup(ctx):
    filename = "bank.txt"

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    while i < len(players):
        if str(players[i]['id']) == str(ctx.author.id):
            if(players[i]['money'] >= lvlsCONFIG[(players[i]['lvl'] + 1)]['money']) and (players[i]['exp'] >= lvlsCONFIG[(players[i]['lvl'] + 1)]['exp']):
                players[i]['money'] = players[i]['money'] - lvlsCONFIG[(players[i]['lvl'] + 1)]['money']
                players[i]['exp'] = players[i]['exp'] - lvlsCONFIG[(players[i]['lvl'] + 1)]['exp']
                players[i]['lvl'] = players[i]['lvl'] + 1
                players[i]['salary'] = lvlsCONFIG[players[i]['lvl']]['salary']
                await ctx.send(f'Уровень повышен до {players[i]["lvl"]}')
            else:
                if (players[i]['money'] < lvlsCONFIG[(players[i]['lvl'] + 1)]['money']):
                    money = lvlsCONFIG[(players[i]['lvl'] + 1)]['money'] - players[i]['money']
                    await ctx.send(f'Вам не хватает {int(money)} ₽')
                    break
                if (players[i]['exp'] < lvlsCONFIG[(players[i]['lvl'] + 1)]['exp']):
                    exp = lvlsCONFIG[(players[i]['lvl'] + 1)]['exp'] - players[i]['exp']
                    await ctx.send(f'Вам не хватает {exp} Опыта')
                    break

                await ctx.send(f'Вам не хватает {int(money)} ₽ и {exp} Опыта')
            break
        i += 1

    myfilew = open(filename, mode="w", encoding="utf-8")
    json.dump(players, myfilew)
    myfilew.close()

@bot.command()
async def crash(ctx,number,cash):
    filename = "bank.txt"
    number = int(number)
    cash = int(cash)

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    go = False
    while i < len(players):
        if str(players[i]['id']) == str(ctx.author.id):
            if cash <= int(players[i]['money']):
                go = True
            else:
                await ctx.send('У вас на счету нет столько денег')
            break
        i += 1
    if go:
        message = f'>>> Число: {number}\n'
        message += f'Ставка: {cash}\n'
        imgs = "1️⃣2️⃣3️⃣\n8️⃣"

        players[i]['money'] = players[i]['money'] - cash

        randomNUMBER = random.randint(0,8)
        if (number < 1) or (number > 8):
            await ctx.send('Число должно быть от 1 до 8!')
        else:
            if number > randomNUMBER:
                cash = 0
            if number == randomNUMBER:
                cash = cash * 2
            if number < randomNUMBER:
                cash = cash * ( 1 + (0.1 * number))

        players[i]['money'] = players[i]['money'] + cash
        if randomNUMBER == 1:
            imgs += '↖️'
        elif randomNUMBER == 2:
            imgs += '⬆️'
        elif randomNUMBER == 3:
            imgs += '↗️'
        elif randomNUMBER == 4:
            imgs += '➡️'
        elif randomNUMBER == 5:
            imgs += '↘️'
        elif randomNUMBER == 6:
            imgs += '⬇️'
        elif randomNUMBER == 7:
            imgs += '↙️'
        elif randomNUMBER == 8:
            imgs += '⬅️'

        imgs += '4️⃣\n7️⃣6️⃣5️⃣\n'

        if randomNUMBER == 0:
            imgs = '💢0️⃣💢'

        message += f'Выйгрыш: {int(cash)}\n'
        message += imgs

        await ctx.send(message)

        myfilew = open(filename, mode="w", encoding="utf-8")
        json.dump(players, myfilew)
        myfilew.close()

@bot.command()
async def casino(ctx,cash):
    filename = "bank.txt"
    cash = int(cash)

    myfiler = open(filename, mode="r", encoding="utf-8")
    players = json.load(myfiler)
    myfiler.close()

    i = 0
    go = False
    while i < len(players):
        if str(players[i]['id']) == str(ctx.author.id):
            if cash <= int(players[i]['money']):
                go = True
            else:
                await ctx.send('У вас на счету нет столько денег')
            break
        i += 1

    if go:
        message = f'>>> Ставка: {cash}\n'

        players[i]['money'] = players[i]['money'] - cash

        numbers = []
        imgs = '⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️'

        for j in range(0,3):
            randomNUMBER = random.randint(0,4)
            numbers.append(randomNUMBER)
            if randomNUMBER == 0:
                imgs += '🔔'
            elif randomNUMBER == 1:
                imgs += '🍒'
            elif randomNUMBER == 2:
                imgs += '🎲'
            elif randomNUMBER == 3:
                imgs += '🍓'
            elif randomNUMBER == 4:
                imgs += '7️⃣'
            imgs += '⬜️'

        if (numbers[0] == numbers[1]) and (numbers[0] == numbers[2]) and (numbers[1] == numbers[2]):
            if numbers[0] == 0:
                cash = cash * 25
            if numbers[0] == 1:
                cash = cash * 50
            if numbers[0] == 2:
                cash = cash * 100
            if numbers[0] == 3:
                cash = cash * 500
            if numbers[0] == 4:
                cash = cash * 1000
        else:
            cash = 0


        imgs+= '\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n'
        message += imgs
        message += f'Выйгрыш: {int(cash)}\n'

        await ctx.send(message)

        players[i]['money'] = players[i]['money'] + cash

        myfilew = open(filename, mode="w", encoding="utf-8")
        json.dump(players, myfilew)
        myfilew.close()

@bot.command()
async def clear(ctx):
    if(ctx.author.id in OWNERS):
        async for message in ctx.channel.history():
            await message.delete()
        message = '>>> \n\n'
        message += '   :broom:  :revolving_hearts: Кира провела уборку :revolving_hearts:  :broom:    \n'
        message += '\n\n'
        message += '!hello - Выводит "Hello (Ваш ник)"\n'
        message += '!commands - Выводит список доступных команд\n'
        message += "!say текст - Бот печатает ваш текст\n"
        message += "!clear - Очищает историю чата(Только для админа)\n"
        message += "!register - Создаёт аккаунт на сервере\n"
        message += "!profile - Информация об аккаунте\n"
        message += "!balance - Баланс на карте\n"
        message += "!lvlup - Увеличить свой лвл(За новый лвл дают больше денег с 1 сообщения)\n"
        message += "!crash 'Число от 1 до 8' 'Кол-во денег' - Игра crash\n"
        message += "!casino 'Кол-во денег' - Игровой автомат 3 в ряд\n"
        await ctx.send(message)

        today = datetime.datetime.today()

        print(f'[WARNING][{today.strftime("%d.%m.%Y  %H:%M")}] Игроком {ctx.author} была проведенна очистка чата  \n')

        LOGS = open('LOGS.txt', 'a', encoding='utf-8')
        raw = str(f'[WARNING][{today.strftime("%d.%m.%Y  %H:%M")}] Игроком {ctx.author} была проведенна очистка чата  \n')
        LOGS.write(raw)
        LOGS.close()

    else:

        today = datetime.datetime.today()

        print(f'[WARNING][{today.strftime("%d.%m.%Y  %H:%M")}] {ctx.author} пытается очистить историю Чата! \n')

        LOGS = open('LOGS.txt', 'a', encoding='utf-8')
        raw = str(f'[WARNING][{today.strftime("%d.%m.%Y  %H:%M")}] {ctx.author} пытается очистить историю Чата! \n')
        LOGS.write(raw)
        LOGS.close()

        await ctx.message.delete()
        await ctx.send(f'🚨🚨 Виу виу 🚨🚨, ⚠⚠ ПОПЫТКА ОБОЙТИ СИСТЕМУ БЕЗОПАСНОСТИ ⚠⚠  🚨🚨 🚓🚓🚓 🚨🚨    нарушитель  -  {ctx.author}')


bot.run(TOKEN)
