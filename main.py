from interactions import *
import asyncio

BOT_TOKEN = ""

bot = Client(
    token=BOT_TOKEN,
    intents=Intents.DEFAULT,
    sync_interactions=True,
    activity="/nuke"
)

@listen()
async def on_ready():
    print("Bot ready!")

@slash_command(
    name="nuke",
    description=f"Deletes a channel and creates a copy of it."
)
@slash_default_member_permission(
    Permissions.MANAGE_CHANNELS
)
@contexts(
    guild=True, 
    bot_dm=False
)
async def nuke_channel(ctx: SlashContext):
    await ctx.send("Nuking the channel in 3 seconds...")

    guild = ctx.guild.id
    username = ctx.user.mention

    channel_name = ctx.channel.name
    channel_type = ctx.channel.type
    channel_topic = ctx.channel.topic if hasattr(ctx.channel, 'topic') else None
    channel_permissions = ctx.channel.permission_overwrites
    channel_position = ctx.channel.position
    channel_nsfw = ctx.channel.nsfw if hasattr(ctx.channel, 'nsfw') else False
    channel_category = ctx.channel.category

    await asyncio.sleep(3)

    await ctx.channel.delete()

    guild = bot.get_guild(guild)

    new_channel = await guild.create_channel(
        name=channel_name,
        channel_type=channel_type,
        topic=channel_topic,
        permission_overwrites=channel_permissions,
        position=channel_position,
        nsfw=channel_nsfw,
        category=channel_category
    )

    await new_channel.send(f"Nuked successfully by {username}!")



if __name__ == "__main__":
    print("Starting...")
    bot.start()
