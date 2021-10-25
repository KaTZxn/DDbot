import discord
from discord.ext import commands
from core.classes import Cog_Extension



class Vt(Cog_Extension):

    # thumbnail_endpoint_1 = "https://i.ytimg.com/vi/"
    # thumbnail_endpoint_2 = "/maxresdefault.jpg"
    # stream_endpoint = "https://www.youtube.com/watch?v=" #Youtube video page
    # dischannel = CHANNELID(int) #Discord's channel id
    # members = json.load(open("./cmds/members.json", mode = 'r', encoding = "utf-8")) #load hololive members dic
    # xml_endpoint = "https://www.youtube.com/feeds/videos.xml?channel_id=" #Youtube video feed xml
    
    @commands.command()
    async def listlive(self, ctx):
        templist = Holo.apilistlive() #requesting live list to Holoapi
        tempnum = len(templist) #getting range of the list
        embed_tosend = discord.Embed(title = f"{tempnum}streams on live!")

        #sending process
        for i in range(tempnum):
            embed_tosend.add_field(name = f"{templist[i][1]}'s stream", value = f"[{templist[i][0]}]({stream_endpoint}{templist[i][2]})")
        await ctx.send(embed = embed_tosend)


class holoapi(object):
    holoapi_endpoint = "https://api.holotools.app/v1/"

    #def apilivenum(self): #get the number of nowlive
    #    ...

    def apilistlive(self): #make a list of nowlive
        lookup_url = f"{self.holoapi_endpoint}live"
        result = requests.get(lookup_url)
        live_dic = result.json()["live"]

        livelist = []
        for i in range(len(live_dic)):
            #get each stream information except desc. and some stats.
            temp = [live_dic[i]["title"], live_dic[i]["channel"]["name"], live_dic[i]["yt_video_key"]]
            livelist.append(temp)

        return livelist

def setup(bot):
    bot.add_cog(Vt(bot))
