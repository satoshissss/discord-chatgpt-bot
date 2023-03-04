"""
参考
"""

import os

import discord

TOKEN = os.environ["DISCODE_HORO_API_KEY"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event  # 起動時に動作する処理
async def on_ready():
    print("ログインしました")  # 起動したらターミナルにログイン通知が表示される


@client.event  # メッセージ受信時に動作する処理
async def on_message(message):
    if message.author.bot:  # メッセージ送信者がBotだった場合は無視する
        return
    if message.content == "/neko":  # 「/neko」と発言したら「にゃーん」が返る処理
        await message.channel.send("にゃーん")


client.run(TOKEN)  # Botの起動とDiscordサーバーへの接続
