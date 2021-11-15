import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
import time
import json


class Live(Cog_Extension):
    Channel = "906350477720051823"
    #Channel_ID = ["UC5LyYg6cCA4yHEYvtUsir3g"]
    Channel_ID = ["UCrAq8h6Q3xGxzUC-84YD9PQ"]
    YOUTUBE_API_KEY = "AIzaSyDYr49jodshi4ou79kteo1p9xbKM5CnUAE"


    def get_live_videos(channelID):
    
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet,id&channelId={channelID}&key={YOUTUBE_API_KEY}&maxResults=100&order=date&type=video"

        live_videos = []
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for video in data.get("items",[]):
                    if video["snippet"].get("liveBroadcastContent") == "live":
                        live_videos.append({"id":video["id"].get("videoId"),"title":video["snippet"].get("title")})

        return live_videos

    async def checkStreaming():
        await self.bot.wait_until_ready()
        self.channel = self.bot.getchannel(Channel)
        while not self.bot.is_closed():
            json_file = open("./link.json", "r")
            json_obj = json.load(json_file)
            json_file.close()
            for id in Channel_ID:
                videos = get_live_videos(id)
                if len(videos) > 0:
                    for video in videos:
                        if video["id"] in json_obj["link"]:
                            break
                        else:
                            json_obj["link"].append(video["id"])
                            json_file = open("./link.json", "w", encoding="UTF-8")
                            json.dump(json_obj, json_file, ensure_ascii=False)
                            json_file.close()
                            #print("配信中です！→" + video["id"] + video["title"])
                            embed=discord.Embed(title={video["title"]}, url="https://www.youtube.com/watch?v="+{video["id"]}, description="直播中", color=0xff941a)
                            embed.set_author(name="木屌Vbot")
                            embed.set_thumbnail(url="http://img.youtube.com/vi/"+{video["id"]}+"/maxresdefault.jpg")
                            embed.add_field(name="{}", value="{}", inline=False)
                            await ctx.send(embed=embed) 
                else:
                    await ctx.send("ライブ配信がみつかりません")
            await asyncio.sleep(1800)








def setup(bot):
    bot.add_cog(Live(bot))