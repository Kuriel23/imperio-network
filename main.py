import discord
from random import *
import requests
import asyncio
from discord.ext.commands import Bot
import time
import datetime
from time import gmtime, strftime
from time import localtime, strftime
import pip
import logging
import youtube_dl
import random
import json
import os

client = discord.Client()
players = {}
blacklist = {438726226279137283}

@client.event
async def on_ready():
   print('BOT ONLINE!Olá amigo!')
   print(client.user.name)
   print("Bot Versão:1.0")
   print('-------Koala-------')
   while True:
       await client.change_presence(game=discord.Game(name="?comandos para ajuda! Estou em beta", type=1, url='https://www.twitch.tv/aventuraland14'), status='streaming')
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='Obrigado a todos!', type=1, url='https://www.twitch.tv/aventuraland14'), status='streaming')
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='Apex Legends', type=1))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='Resident Evil 2 Remake', type=1))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='Minecraft', type=1))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='The sims 4', type=1))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='Fortnite', type=1))
       await asyncio.sleep(20)
       await client.change_presence(game=discord.Game(name='Vamos 100 servidores!Meta do ano!', type=1))
       await asyncio.sleep(20)

@client.event
async def on_message(message):
    if message.content.lower().startswith('?sobre'):
        embed1 = discord.Embed(title="Sobre mim e meu desenvolvedor", description="De Império Network", color=0xE81F3F)
        embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/430487645525901323/436566327918854144/images.jpg")
        embed1.add_field(name="Olá, sou o ImpérioNetwork, fui desenvolvido pelo **Koala#6339**.", value="Se você quiser saber minha historia use ?historia", inline=True)
        embed1.add_field(name="Começei a ser programado no dia 24/03/2018", value="Espero que divirta-se comigo.", inline=True)
        embed1.set_footer(text="Copyright 2018 ImpérioNetwork!")
        await client.send_message(message.channel, embed=embed1)

    if message.content.lower().startswith('?comandos') or message.content.startswith('?ajuda') or message.content.startswith('?help'):
        try:
            embed2 = discord.Embed(title="Comandos", description="De Império Network", color=0xb0ff00)
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/430487645525901323/436489364437204992/support_bear_small2x.png")
            embed2.add_field(name="?moeda", value=" Vamos apostar!Coroa ou moeda?Eu digo!.", inline=False)
            embed2.add_field(name="?memes", value=" Você já sabe.Memes mas não é claro.", inline=False)
            embed2.add_field(name="?fome", value=" Os seus melhores amigos mais saborosos na barriga!", inline=False)
            embed2.add_field(name="?servers", value=" Vê em quantos servidores eu estou.", inline=False)
            embed2.add_field(name="?convites", value=" Eu falo convites meus!", inline=False)
            embed2.add_field(name="?news", value=" Eu apresento a última notícia para você da Globo!", inline=False)
            embed2.add_field(name="?fale", value=" Eu falo o que você pediu!", inline=False)
            embed2.add_field(name="?avatar", value=" Eu apresento o avatar de você ou do usuário mencionado!", inline=False)
            embed2.add_field(name="?serverinfo", value=" Eu apresento as informações do servidor!", inline=False)
            embed2.add_field(name="?google", value=" Eu falo um link do google com sua pesquisa!", inline=False)
            embed2.add_field(name="?userinfo (menção)", value="Apresento informações do utilizador!", inline=False)
            embed2.add_field(name="?gif (tag)", value="Apresento um gif aleatoriamente com essa tag!", inline=False)
            embed2.set_footer(text="Copyright 2018 ImpérioNetwork! || Desenvolvido por: Koala#6339 e Kaze#4218")
            await client.send_message(message.channel, "📬 ``Meus comandos foram enviados no seu privado!``")
            await client.send_message(message.author, embed=embed2)
        except:
            await client.send_message(message.channel,"🤔 O Usuário tem o DM desativado ou você me bloqueou. 🤔")

    if message.author.id == "314867933077569539":
            await client.add_reaction(message, '😀')

    if message.content.lower().startswith('?reload') and message.author.id == "354233941550694400":
            await client.send_message(message.channel, "{} Reload successfully! iPaddysz_ you will have to warn me to give reload again!".format(message.author.mention))
            os.system("python main.py reload")

    if message.content.lower().startswith('?emojiid'):
        emoji = message.content[9:]
        await client.send_message(message.channel, "ID DO EMOJI: \\" +emoji)

    if message.content.lower().startswith('?fome'):
        embedfome = discord.Embed(title="Comando ?fome", description="Os seus melhores amigos da sua barriga!", color=0xffab7f)
        embedfome.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/436238069033861132/thx.png?size=2048")
        embedfome.set_footer(text="Copyright 2018 ImpérioNetwork!")
        await client.send_message(message.channel, embed=embedfome)

    if message.content.lower().startswith('?virus'):
        mention = message.mentions[0]
        message = await client.send_message(message.channel, "|░----| Aguarde...")
        await asyncio.sleep(4)
        await client.edit_message(message, "|░░---| Extraindo Discord.exe...")
        await asyncio.sleep(4)
        await client.edit_message(message, "|░░░--| Removendo DiscordFake.rar...")
        await asyncio.sleep(3)
        await client.edit_message(message, "|░░░░-| Forçando Encerramento da internet...")
        await asyncio.sleep(3)
        await client.edit_message(message, "|░░░░░| Executando Discord.exe")
        await asyncio.sleep(3)
        await client.edit_message(message, "|░░░░░| Operação concluida, infectado {}".format(mention))

    if message.content.lower().startswith('?serverinfo'):
        serverinfo_embed = discord.Embed(title="", description="", color=000000)
        serverinfo_embed.set_thumbnail(url=f"{message.server.icon_url}")
        serverinfo_embed.set_author(name=f"{message.server.name}", icon_url=f"{message.server.icon_url}")
        serverinfo_embed.add_field(name="👑 Criador:", value=f"@{message.server.owner}")
        serverinfo_embed.add_field(name="💻 ID:", value=f"{message.server.id}")
        serverinfo_embed.add_field(name="🌎 Região:", value=f"{message.server.region}".strip().replace('brazil', 'Brasil'))
        serverinfo_embed.add_field(name="📅 Data de criação:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        serverinfo_embed.add_field(name="👥 Membros:", value=f"{message.server.member_count}")
        await client.send_message(message.channel, embed=serverinfo_embed)

    if message.content.lower().startswith('?moeda'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        if choice == 2:
            await client.add_reaction(message, '👑')

    if message.author.id == "none":
            await client.delete_message(message)

    if message.content.lower().startswith('?matar'):
        try:
            morte = random.randint(1, 3)
            if morte == 1:
                emb = discord.Embed(title='\n', description='{} matou o(a) {}!'.format(message.author.name, message.mentions[0].name),color=0x00000)
                emb.set_image(url="https://media1.tenor.com/images/07b1b6d9f75d0dd1aa0090224c3a5070/tenor.gif?itemid=7356862"),
                await client.send_message(message.channel, embed=emb)

            if morte == 2:
                emb = discord.Embed(title='\n', description='{} matou o(a) {}!'.format(message.author.name, message.mentions[0].name),color=0x00000)
                emb.set_image(url="https://media1.tenor.com/images/27f82ef4f27ebad9c51259365cacd62e/tenor.gif?itemid=5472977"),
                await client.send_message(message.channel, embed=emb)

            if morte == 3:
                emb = discord.Embed(title='\n', description='{} matou o(a) {}!'.format(message.author.name, message.mentions[0].name),color=0x00000)
                emb.set_image(url="https://media1.tenor.com/images/45ec8ee66e87cf7603a43d5105f883c3/tenor.gif?itemid=5459055"),
                await client.send_message(message.channel, embed=emb)
        except:
            await client.send_message(message.channel, 'Você precisa mencionar um usuário para matar!')

    if message.content.lower().startswith('?abraçar'):
        try:
            hug = random.randint(1, 3)
            if hug == 1:
                emb = discord.Embed(title='\n', description='{} ganhou um abraço do(a) {}!'.format(message.mentions[0].name, message.author.name), color=0x00000)
                emb.set_image(url="https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705"),
                await client.send_message(message.channel, embed=emb)

            if hug == 2:
                emb = discord.Embed(title='\n', description='{} ganhou um abraço do(a) {}!'.format(message.mentions[0].name, message.author.name), color=0x00000)
                emb.set_image(url="https://media1.tenor.com/images/949d3eb3f689fea42258a88fa171d4fc/tenor.gif?itemid=4900166"),
                await client.send_message(message.channel, embed=emb)

            if hug == 3:
                emb = discord.Embed(title='\n', description='{} ganhou um abraço do(a) {}!'.format(message.mentions[0].name, message.author.name), color=0x00000)
                emb.set_image(url="https://media1.tenor.com/images/11889c4c994c0634cfcedc8adba9dd6c/tenor.gif?itemid=5634578"),
                await client.send_message(message.channel, embed=emb)
        except:
            await client.send_message(message.channel, 'Você precisa mencionar um usuário para abraçar!')

    if message.content.lower().startswith('?ppt'):
        choice = random.randint(1, 3)
        if choice == 1:
            await client.add_reaction(message, '✂')
        if choice == 2:
            await client.add_reaction(message, '📝')
        if choice == 3:
            await client.add_reaction(message, "🌕")

    if message.content.lower().startswith('?memes'):
        choice = random.randint(1, 6)
        if choice == 1:
            embedmeme1 = discord.Embed(title="Hora do Meme!", description="", color=0xff9b4f)
            embedmeme1.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/430502115765518337/homens-na-cozinha.jpg")
            await client.send_message(message.channel, embed=embedmeme1)
        if choice == 2:
            embedmeme2 = discord.Embed(title="Hora do Meme!", description="", color=0xff9b4f)
            embedmeme2.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/430503968331005962/demon.gif")
            await client.send_message(message.channel, embed=embedmeme2)
        if choice == 3:
            embedmeme3 = discord.Embed(title="Hora do Meme!", description="", color=0xff9b4f)
            embedmeme3.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/430503570865913866/e55afca5b870224b445dc6396cf3893c.jpg")
            await client.send_message(message.channel, embed=embedmeme3)
        if choice == 4:
            embedmeme4 = discord.Embed(title="Hora do Meme!", description="", color=0xff9b4f)
            embedmeme4.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/430487982546485269/meme-calor-chapolin.jpg")
            await client.send_message(message.channel, embed=embedmeme4)
        if choice == 5:
            embedmeme5 = discord.Embed(title="Hora do Meme!", description="", color=0xff9b4f)
            embedmeme5.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/430490834199117834/Engra4.jpg")
            await client.send_message(message.channel, embed=embedmeme5)
        if choice == 6:
            embedmeme6 = discord.Embed(title="Hora do Meme!", description="", color=0xff9b4f)
            embedmeme6.set_image(url="https://cdn.discordapp.com/attachments/430487645525901323/430492065244250112/ISv2N.jpg")
            await client.send_message(message.channel, embed=embedmeme6)

    if message.content.lower().startswith('?servers'):
        servidores = str(len(client.servers))
        allservers = '\n'.join([str(server) for server in client.servers])
        await client.send_message(message.channel,"{}, Até agora estou em {} servidores, tais quais: {}.".format(message.author.mention,servidores, allservers))

    if message.content.lower().startswith('?membros'):
        jogadores = str(len(set(client.get_all_members())))
        await client.send_message(message.channel,"{}, Até agora estou interagindo com {} membros".format(message.author.mention,jogadores))

    if message.content.lower().startswith('?emojis'):
        emojis =  discord.utils.get(client.get_all_emojis(), name="PepeBebendoCafe")
        await client.send_message(message.channel,"Comando em experimentos. {}".format(emojis))

    if message.content.lower().startswith('?py'):
        codigo_py = message.content[4:]
        await client.delete_message(message)
        await client.send_message(message.channel, f"Código de {message.author.mention}")
        await client.send_message(message.channel, f"```py\n{codigo_py}```")

    elif message.content.lower().startswith('?avatar'):
        try:
            membro = message.mentions[0]
            avatarembed = discord.Embed(title="", color=0xFF8000, description="**[Clique aqui](" + membro.avatar_url + ") para acessar o link do avatar apresentado!**")
            avatarembed.set_author(name=membro.name)
            avatarembed.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)
        except:
            avatarembed2 = discord.Embed(title="", color=0xFF8000, description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar apresentado!**")
            avatarembed2.set_author(name=message.author.name)
            avatarembed2.set_image(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=avatarembed2)

    if message.content.lower().startswith('?emojiinfo'):
        emojisearch = message.content[11:]
        allemojis = client.get_all_emojis()
        emoji = discord.utils.get(allemojis, name=emojisearch)
        emojiinfo = discord.Embed(title="\n", description="\n", color=0x000000)
        emojiinfo.add_field(name="Nome:", value="{}".format(emoji))

    if message.content.lower().startswith('?convite'):
        embedconvite = discord.Embed(title="Convites!!!", description="Aqui estão alguns dos meus convites!", color=0xff9b4f)
        embedconvite.set_thumbnail(url="https://cdn.discordapp.com/attachments/430487645525901323/438017350206357505/fleck.jpg")
        embedconvite.add_field(name="Convite para meu servidor!Tou á espera de você", value="[Clique Aqui](https://discord.gg/zubMYv4)", inline=False)
        embedconvite.add_field(name="Convite para eu entrar no seu servidor.", value="[Clique Aqui](https://discordapp.com/oauth2/authorize?client_id=427093936251863040&scope=bot&permissions=8)")
        embedconvite.add_field(name="Convite para meu site.", value="[Clique Aqui](https://imperionetwork.glitch.me)")
        embedconvite.set_footer(text="Copyright 2018 ImpérioNetwork")
        await client.send_message(message.channel, embed=embedconvite)

    if message.content.lower().startswith('?fale'):
        mensagem_falada = message.content[5:]
        await client.delete_message(message)
        embedfalar = discord.Embed(title=f"{message.author.name} pediu para eu falar:", color=0xFF8000, description=f"{mensagem_falada}")
        await client.send_message(message.channel, embed=embedfalar)
        
    if message.content.lower().startswith('?news'):
        reqnews = requests.get('https://newsapi.org/v2/top-headlines?sources=globo&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    elif message.content.lower().startswith("?eval"):
        if not message.author.id == '354233941550694400':
            return await client.send_message(message.channel, '<:drake_no:472442602520707102> **Permissão insuficiente**')
        try:
            embedeval1 = discord.Embed(title='\n', description='\n')
            embedeval1.add_field(name='**:inbox_tray: Entrada**', value='`' + message.content[6:] + '`')
            embedeval1.add_field(name='**:outbox_tray: Saída**', value='`' + str(eval(message.content[6:])) + '`')
            embedeval1.set_thumbnail(url="https://cdn.discordapp.com/attachments/430487645525901323/474652350922096652/1357e8b2e27ce31.png")
            await client.send_message(message.channel, embed=embedeval1)
            await client.add_reaction(message, '🙉')
        except Exception as e:
            embedeval = discord.Embed(title='\n', description='\n')
            embedeval.add_field(name='**:inbox_tray: Entrada**', value='`' + message.content[6:] + '`')
            embedeval.add_field(name='**:outbox_tray: Saída**', value='`' + repr(e) + '`')
            embedeval.set_thumbnail(url="https://cdn.discordapp.com/attachments/430487645525901323/474652579738025984/wrong-295503_960_720.png")
            await client.send_message(message.channel, embed=embedeval)
            await client.add_reaction(message, '🙊')

    if message.content.lower().startswith("?google"):
        google_txt = 'https://www.google.com/search?q=' + message.content[7:].strip().replace(' ', '+')
        google_embed = discord.Embed(title="Resultado Da pesquisa:", color=0xFF8000, description=f"{google_txt}")
        google_embed.set_thumbnail(url="http://diylogodesigns.com/blog/wp-content/uploads/2016/04/google-logo-icon-PNG-Transparent-Background.png")
        await client.send_message(message.channel, embed=google_embed)

    if message.channel == client.get_channel('430009192515108864'):
        await client.add_reaction(message, '👎')
        await client.add_reaction(message, '👍')
        await client.add_reaction(message, '💖')

    if message.content.lower().startswith('<@427093936251863040>'):
        helping = discord.Embed(title=f"Oi?", color=0xff0000, description=f"Eu sou o ImpérioNetwork!")
        helping.add_field(name='Use ?ajuda no servidor.', value="Para ver os meus comandos.")
        helping.set_image(url="https://cdn.discordapp.com/attachments/425866379921719297/450797281676099584/iktp8z6po7y20uxz6xeq_400x400.jpeg")
        marca = await client.send_message(message.channel, embed=helping)
        await client.add_reaction(marca, '❓')
        await client.add_reaction(marca, '🇦')
        await client.add_reaction(marca, '🇯')
        await client.add_reaction(marca, '🇺')
        await client.add_reaction(marca, '🇩')
        await client.add_reaction(marca, '🅰')

    if message.content.lower().startswith('?bug'):
        bug_feito = message.content[4:]
        bug_embed = discord.Embed(title=f"Bug Reportado de {message.author.name}", color=0xFF8000, description=bug_feito)
        bug_embed.set_footer(text=f"ID do usuário: {message.author.id}")
        await client.delete_message(message)
        bug_msg = await client.send_message(message.channel, embed=bug_embed)
        await client.add_reaction(bug_msg, '✅')
        await client.add_reaction(bug_msg, '❎')
        await client.send_message(message.author, f"{message.author.mention}, obrigado por enviar seu bug em {message.server.name}!")

    if message.content.lower().startswith('?buscaremoji'):
        try:
           msg = message.content[13:]
           requisitar = requests.get('https://discordemoji.com/api')
           resposta = json.loads(requisitar.text)
           for resp in resposta:
               if resp['title'] == msg:
                  embed = discord.Embed(title='Informações do emoji: {}'.format(resp['title']), description='[Clique aqui]({}) para baixar o emoji.'.format(resp['image']), color=0x00FFF)
                  embed.set_thumbnail(url=resp['image'])
                  return await client.send_message(message.channel, embed=embed)
               else:
                   pass
        except:
            await client.send_message(message.channel, "Desculpe, não encontrei nenhum emoji com esse nome.")

    if message.content.startswith('?gif'):
        try:
            tag = message.content[6:]
            resultado = giphy_api(tag)
            embed_gif = discord.Embed(title="\n", description='\n', color=0x751975)
            embed_gif.set_image(url=resultado)
            embed_gif.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed_gif)
        except:
            await client.send_message(message.channel, 'Não encontrei nenhuma gif para essa tag!Espere alguém que posta um gif com essa tag!')

    if message.content.lower().startswith('?pm'):
        try:
            await client.delete_message(message)
            embed = discord.Embed(title='Mensagem de um misterioso :3',  description='Olá {}, eu sou o {}, vim atraves daqui te dizer: {}'.format(message.mentions[0], client.user.name, message.content[3:]),)
            await client.send_message(message.mentions[0], embed=embed)
        except:
            await client.send_message(message.channel, 'Puts não consegui mandar uma msg, acho que ele me bloqueou :(!')

    if message.content.lower().startswith('?botavisar'):
        await client.delete_message(message)
        avisarimperio = client.get_channel("368090912573882369")
        avisarfala = message.content[11:]
        botavisar = discord.Embed(title="\n", color=0xFF8000, description=avisarfala)
        botavisar.set_image(url="https://images-ext-1.discordapp.net/external/Tz2TE2BfBvB2eM-XABGxspW0ucHRvMwnBTtU_edEA-E/https/cdn.discordapp.com/icons/368089935548514312/a1504f2671c4f9f079a99c4036a2bb05.jpg")
        botavisar.set_author(name=f"{message.author.name} avisou uma novidade no dia: " +datetime.datetime.now().strftime("%d/%m/%y ás: %H:%M") ,icon_url=f"{message.author.avatar_url}")
        botavisar.set_footer(text="Você quer receber novidades? Use ?notificar - Copyright 2018 ImpérioNetwork")
        await client.send_message(avisarimperio, "<@&463722127359737857> Aí vem uma novidade!!!")
        await client.send_message(avisarimperio, embed=botavisar)

    if message.content.lower().startswith('?userinfo'):
        try:
            userinfo_mention = message.mentions[0]
            userinfo_mention_embed = discord.Embed(title="", color=0xFF8000, description="")
            userinfo_mention_embed.set_thumbnail(url=f"{userinfo_mention.avatar_url}")
            userinfo_mention_embed.set_author(name=f"{userinfo_mention.name} - Jogando {userinfo_mention.game}".strip().replace('None', 'Nada'), icon_url=f"{userinfo_mention.avatar_url}")
            userinfo_mention_embed.add_field(name="💻 ID do usuário:", value=f"{userinfo_mention.id}")
            userinfo_mention_embed.add_field(name="📅 Conta criada em:", value=userinfo_mention.created_at.strftime("%d %b %Y %H:%M"))
            userinfo_mention_embed.add_field(name="⏰ Entrou pela primeira vez em:", value=userinfo_mention.joined_at.strftime("%d %b %Y %H:%M"))
            userinfo_mention_embed.add_field(name="💼 Cargos:", value=([role.name for role in userinfo_mention.roles if role.name != "@everyone"]))
            userinfo_mention_embed.add_field(name="💼 Cargo mais alto:", value=f"{userinfo_mention.top_role}")
            await client.send_message(message.channel, f"{message.author.mention}", embed=userinfo_mention_embed)
        except:
            userinfo_embed = discord.Embed(title="", color=0xFF8000, description="")
            userinfo_embed.set_thumbnail(url=f"{message.author.avatar_url}")
            userinfo_embed.set_author(name=f"{message.author.name} - Jogando {message.author.game}".strip().replace('None', 'Nada'), icon_url=f"{message.author.avatar_url}")
            userinfo_embed.add_field(name="💻 ID do usuário:", value=f"{message.author.id}")
            userinfo_embed.add_field(name="📅 Conta criada em:", value=message.author.created_at.strftime("%d %b %Y %H:%M"))
            userinfo_embed.add_field(name="⏰ Entrou pela primeira vez em:", value=message.author.joined_at.strftime("%d %b %Y %H:%M"))
            userinfo_embed.add_field(name="💼 Cargos:", value=([role.name for role in message.author.roles if role.name != "@everyone"]))
            userinfo_embed.add_field(name="💼 Cargo mais alto:", value=f"{message.author.top_role}")
            await client.send_message(message.channel, f"{message.author.mention}", embed=userinfo_embed)

    if message.content.lower().startswith('?ban'):
        try:
            if not message.author.server_permissions.ban_members:
                return await client.send_message(message.channel, '⚠️Permissões insuficientes')
            author = message.author.mention
            user = message.mentions[0]
            await client.ban(user)
            await client.send_message(message.channel,"Usuário: {} banido do servidor pelo Administrador: {}".format(user.mention,author))
        except discord.errors.Forbidden:
            return await client.send_message(message.channel,'⚠️ Não posso banir o usuário: {}'.format(user.mention))
        except:
            await client.send_message(message.channel, "Erro: Você não mencionou ninguém.")

    if message.content.lower().startswith('?mutar'):
        try:
            if not message.author.server_permissions.manage_roles:
                return await client.send_message(message.channel, '⚠️Permissões insuficientes')
            author = message.author.mention
            user = message.mentions[0]
            motivo = message.content[29:]
            cargo = discord.utils.get(message.author.server.roles, name='Muted')
            await client.add_roles(user, cargo)
            await client.send_message(message.channel,'O Usuário: {} foi mutado pelo Administrador: {} pelo motivo: {}.'.format(user.mention, author, motivo))
        except:
            await client.send_message(message.channel, "Deu erro.")

    if message.content.lower().startswith('?notificar'):
        if message.server.id == "368089935548514312":
             cargo = discord.utils.get(message.author.server.roles, name='Notificar')
             author = message.author
             await client.add_roles(author, cargo)
             await client.send_message(message.channel,'Pronto.Agora você tem o cargo Notificar.')
        else:
             await client.send_message(message.channel, "Este comando não é permitido neste servidor.")

    if message.content.lower().startswith('?desnotificar'):
        if message.server.id == "368089935548514312":
             cargo = discord.utils.get(message.author.server.roles, name='Notificar')
             author = message.author
             await client.remove_roles(author, cargo)
             await client.send_message(message.channel,'Pronto.Agora você não tem o cargo Notificar.')
        else:
             await client.send_message(message.channel, "Este comando não é permitido neste servidor.")

    if message.content.lower().startswith('?giveawaysnotificar'):
        if message.server.id == "368089935548514312":
             cargo = discord.utils.get(message.author.server.roles, name='Notificar Giveaways')
             author = message.author
             await client.add_roles(author, cargo)
             await client.send_message(message.channel,'Pronto.Agora você tem o cargo Notificar Giveaways.')
        else:
             await client.send_message(message.channel, "Este comando não é permitido neste servidor.")

    if message.content.lower().startswith('?giveawaysdesnotificar'):
        if message.server.id == "368089935548514312":
             cargo = discord.utils.get(message.author.server.roles, name='Notificar Giveaways')
             author = message.author
             await client.remove_roles(author, cargo)
             await client.send_message(message.channel,'Pronto.Agora você não tem o cargo Notificar Giveaways.')
        else:
             await client.send_message(message.channel, "Este comando não é permitido neste servidor.")

    if message.content.lower().startswith('?report'):
        await client.delete_message(message)
        canalreport = client.get_channel("474238062625292295")
        membro = message.author.mention
        reportado = message.mentions[0]
        motivoreport = message.content[29:]
        embedreport = discord.Embed(title="1 report chegou!Atenda-o!", description="Reaja com as seguintes reações se o report foi aceitado/negado.\n Aceitado - ✅ Negado - ❎.", color=0xfb0000)
        embedreport.add_field(name="👥Membro:", value="{}".format(membro), inline=False)
        embedreport.add_field(name="😡Reportado:", value="{}".format(reportado), inline=False)
        embedreport.add_field(name="🖨Motivo:", value="{}".format(motivoreport), inline=False)
        await client.send_message(canalreport, "@here acabou de receberem 1 report!")
        report = await client.send_message(canalreport, embed=embedreport)
        await client.add_reaction(report, '✅')
        await client.add_reaction(report, '❎')

    if message.content.lower().startswith('?desmutar'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️Permissões insuficientes')
        author = message.author.mention
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Muted')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel,'O usuário: {} foi Desmutado pelo Administrador: {}'.format(user.mention, author))

    if message.content.lower().startswith('?ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0x000000, description='Meu tempo de resposta é `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)

def giphy_api(tag):
    url = 'http://api.giphy.com/v1/gifs/search?q={}&api_key=VtcqzPrTaq8ocQ95snNhnZtrCREJMkwD&limit=16'.format(tag)
    resposta = requests.get(url)
    resposta_json = json.loads(resposta.text)
    gif = resposta_json['data'][randrange(0,15)]['id']
    return 'https://media.giphy.com/media/{}/giphy.gif'.format(gif)

client.run('NDI3MDkzOTM2MjUxODYzMDQw.DZfh5g.Mq0LRmIv8qU3CQLGB7Jaog3dXnc')                                                          