import discord, requests, random, os
from discord.ext import commands
import sqlite3 as sql
from datetime import datetime as dt
import traceback



class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
	
    def db_util(self,mode,query):
        '''
        <mode>:
            -"insert" for adding rows to db\n
            -"update" for modifying rows of db\n
            -"select" for returning values from db (as a list of rows represented by tuples)\n
            -"delete" for removing rows from db\n
        <query>: SQL query to excecute
        '''
        #TODO: ADD BACKUP SQL METHOD
        conn = sql.connect('submissions.sql')
        c = conn.cursor()

        #print(query)
        to_return = None
        if mode.lower() == 'select':
            c.execute(query)
            to_return = c.fetchall()
            print(to_return)
        else:
            c.execute(query)

        conn.commit()
        conn.close()
        return to_return 
    
    
    
    @commands.command(name='submit', aliases=["s"])
    async def submit(self, ctx, comp_id: str, title: str, description: str):
        '''
		Submit a new entry to a competition via <comp_id>. If you are collabing, only one person has to submit (surround in " "):

		<title>: Submission Title (surround in " ") (CAN BE MULTIPLE WORDS)
		<description>: Give some background info surrounding the track. IF YOU ARE COLLABING, INCLUDE OTHER PEOPLE'S DISCORD TAGS AS WELL (surround in " ")
		<audio>: Upload audio to message. DO NOT TYPE ANYTHING
        '''
        try:
            #Check if competition is closed 
            closed = self.db_util('select',f'SELECT closed FROM competitions where id = "{comp_id.lower()}"')[0][0]
            if closed == 1 or closed == "TRUE":
                await ctx.channel.send("This competition is closed. Please message the moderators to open the competition.")
                return
            
            #Creates Audio Filepath and Save Audio
            user_folder = f'./audio/{comp_id.lower()}/{str(ctx.author)}'
            if not os.path.exists(user_folder):
                os.mkdir(user_folder)
            audio_file = f'{user_folder}/{ctx.message.attachments[0].filename}'
            await ctx.message.attachments[0].save(audio_file)
            
            #Insert Submission into SQL Table
            date = dt.now().strftime('%H:%M:%S on %m/%d/%Y')
            insert_query = f'''INSERT INTO submissions 
                            (comp_id, username, title, description, date, audio_src)
                            VALUES ("{comp_id.lower()}","{str(ctx.author)}","{title}","{description}","{date}","{audio_file}")
                            '''
            self.db_util('insert',insert_query)
            await ctx.channel.send(f"Your submission track \"{title}\" has been processed!")
        except Exception as e:
            print(e)
            await ctx.send('An error has occured. Did you enter all the parameters properly?')
            return
    
    
    
    @commands.command(name='unsubmit', aliases=["us"])
    async def unsubmit(self, ctx, comp_id: str):
        '''
		Unsubmit your music from a certain competition via <comp_id> (surround in  " ")
        '''
        try:
            self.db_util('delete', f'DELETE FROM submissions WHERE comp_id = "{comp_id.lower()}" AND username = "{str(ctx.author)}"')
            
            #Delete User Submission File
            dir = f'./audio/{comp_id.lower()}/{str(ctx.author)}'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            
            comp_name = self.db_util('select', f'SELECT theme FROM competitions WHERE id = "{comp_id.lower()}"')[0][0]
            await ctx.send(f'You have unsubmitted from {comp_name}.')
        except Exception as e:
            print(e)
            await ctx.send("An error has occured. You either haven't submitted yet to that competition or entered an invalid parameter")



async def setup(client):
    await client.add_cog(Member(client))