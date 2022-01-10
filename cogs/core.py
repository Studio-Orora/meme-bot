import config
import discord
import datetime
import asyncio
from discord.ext import commands
from discord.commands import slash_command, Option, permissions
from utils.embed import *
from utils.database import *

class core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self):
        if await BLACKLIST.search_blacklist(self.author.id):
            embed = Embed.ban_info(await BLACKLIST.search_blacklist(self.author.id))
            await self.respond(embed=embed, ephemeral=True)
            return False
        else:
            return True

    @commands.slash_command(name="정보", description="'짤방러' 봇의 자세한 정보를 알아볼 수 있어요.", guild_ids=[852766855583891486], checks=[cog_check])
    async def 정보(self, ctx):
        # 짤 로드할 때 필요할듯 - await ctx.interaction.response.defer()
        embed = discord.Embed(
            title=f"<:jbllogo:929615468233363457> {self.bot.user.name} 정보",
            description=f"``Discord API LATENCY`` : {round(self.bot.latency * 1000)}ms",
        )
        embed.set_thumbnail(url=self.bot.user.avatar)
        await ctx.respond("https://discord.gg/FP6JwVDRDc", embed=embed)

def setup(bot):
    bot.add_cog(core(bot))