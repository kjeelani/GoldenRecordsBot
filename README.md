# GoldenRecordsBot (GRBot)

A Discord Bot for the UC Berkeley Golden Records Discord (a group of music producers trying to explore new genres via bi-weekly beat battles). This application manages these "competitions" and their respective submissions.


# Installation

1) To test out this application, you first need to create your own Discord Bot. To do this, go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.

2) Add your Discord bot to a test Discord server, then get your Bot token key and paste it in *bot.py* where it asks for you to place the token.

3) Ensure that you have the Pandas and Discord.py libraries downloaded via `pip3 install discord, pandas`.

3) To check if the SQL database has the correct tables, call the print_database() function in start_sql.py. Then run bot.py to startup the Bot


# Commands
Below is a table of commands. ALL parameters that are strings need to be surrounded by quotes.
| Command Name/Aliases       | Permissions | Parameters                                | Description                                                                                                                                                                         |
|----------------------------|-------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| !clear_messages            | Admin       | `<num_messages>`                          | Clears *num_messages* amount of messages from the channel this command was executed                                                                                                 |
| !create_comp (!crc)        | Admin       | `<id> <name> <description>`               | Creates a new competition in the database. <br><br> <br>*id*: Tag used for further commands<br>  *name*: Title of competition<br>*description*: Details of competition |
| !post_comp (!pc)           | Admin       | `<id> <channel>`                          | Posts competition details associated with *id* in *channel*                                                                                                                         |
| !close_comp (!cc)          | Admin       | `<id>`                                    | Locks competition associated with *id*                                                                                                                                              |
| !reopen_comp (!rc)         | Admin       | `<id>`                                    | Unlocks competition associated with *id*                                                                                                                                            |
| !release_submissions (!rs) | Everyone    | `<id> <channel>`                          | Formats and sends all submissions of competition associated with *id* in *channel*.<br><br>You can vote for submissions by reacting to each submission.                             |
| !submit (!s)               | Everyone    | `<id> <title> <description> <audio_file>` | Submits *audio_file* (as an audio attatchment) with *title* and *description* to the submissions database and associates it with a competition via *id*                             |
| !unsubmit (!us)            | Everyone    | `<id>`                                    | Removes all the user's submissions from the competition associated with *id*                                                                                                        |


# Future Changes

1) Making a help command for anyone using GRBot on Discord. 

2) Create a voting system (keeping track of votes via another SQL table, keeping track of past winners, etc.)

3) Edge Case Testing (making sure the database CANNOT break via any command)
