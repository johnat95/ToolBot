# ToolBot# ToolBot

This program starts a discord bot, and loads files contationing cog classes. Each cog class containes methods that can be called by sending 
a direct message to the bot on discord.

Further development of CS and CIS tools is planned; the next planned cog will contain methods to aid in subnet masking.

Requirments:
python 3.11
discord.py version 2.1.0
python-dotenv 0.21.0

Installation for Python 3:

https://www.python.org/downloads/

In the project folder, create a virtual enviroment:

    python -m venv <enviroment name>

  Activate virual enviroment:

    -Windows-

    In cmd.exe
    venv\Scripts\activate.bat

    In PowerShell
    venv\Scripts\Activate.ps1

    -Linux and Mac-
    source myvenv/bin/activate

After activating enviroment, command line should show <enviroment name> at the start of the command line.

Enter:

    pip install discord.py==2.1.0 python-dotenv==0.21.0

For development testing:

Add an app through the discord development portal:

https://discord.com/login?redirect_to=%2Fdevelopers

Add a bot to the application, then create a file named bot.env to the project, add the generated token:
    
    TOKEN="<token>"

To Run:

  While the enviroment is activated, type python bot.py to start and ctrl + c to stop
  
  Send '$help' in a direct message to get a list of available commands.
  
  

