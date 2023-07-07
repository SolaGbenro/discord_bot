from app.discord_bot.discord_api import client, discord_token
# running two python files simultaneously requires additional __init__.py files

if __name__ == '__main__':
    client.run(discord_token)
