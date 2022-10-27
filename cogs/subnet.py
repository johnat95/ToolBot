#programmer: Nathan Johnston

#purpose: converts numbers to binary, with the option of breaking down the math at each bit

from discord.ext import commands
import psutil


class Subnet(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       await print("Subnet Creator Online")

    

   
    
async def setup(bot):
    await bot.add_cog(Subnet(bot))        
     
