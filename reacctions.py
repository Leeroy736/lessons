@Bot.event
async def on_raw_reaction_add(payload):
    guild = await Bot.fetch_guild(АйдиСервера)
    if payload.message_id == ВашАйди and payload.emoji.name == "ВашЭмоджи":
        role = discord.utils.get(guild.roles, id = ВашАйди)
        await payload.member.add_roles(role)
