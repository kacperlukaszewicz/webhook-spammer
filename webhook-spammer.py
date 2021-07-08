from discord_webhook import DiscordWebhook
print("""
╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═                                                                  
""")
print(' ')

webhook = input('Webhook URL: ')
message = input('Message: ')
post = DiscordWebhook(url=webhook,content=message)
count = int(input('How many messages: '))

print('Sending messages....')

looped = 0

for x in range(count):
    response = post.execute()
    looped += 1
    print('Messages sent: ',looped)
