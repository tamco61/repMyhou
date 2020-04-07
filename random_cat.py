import discord
import requests
TOKEN = input('Введите токен бота: ')


class YLBotClient(discord.Client):

    async def on_ready(self):
        print(f'{self.user} подключился и готов показать случайного котика (или пёсика!)')

    async def on_message(self, message):
        cat = 'https://api.thecatapi.com/v1/images/search'
        dog = 'https://dog.ceo/api/breeds/image/random'
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            data = response.json()
            await message.channel.send(data[0]['url'])
        elif "пес" or "пёс" or "соба" in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            data = response.json()
            await message.channel.send(data['message'])


client = YLBotClient()
client.run(TOKEN)
