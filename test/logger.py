def log(author, authorid, discri, guild, channel, message):
    from datetime import datetime
    import pytz
    
    pst = pytz.timezone('America/Los_Angeles')
    datetimela = datetime.now(pst)
    datetimela = datetimela.strftime("%B %d, %Y		%H:%M:%S")

    if message == ".optout":
        returnme = "Are you sure you want to opt out? This option is irreversable. \nIf you are sure, use the command `.optout y`"
        return returnme
    elif message == ".optout y":
        returnme = "You have opted out of the message logger"
        optf = open("optedout.txt", "a")
        optf.write(f'{datetimela}		{author}#{discri} has opted out.		id={authorid}')
        optf.close()
    else:
        logf = open("log.txt", "a")
        optf = open("optedout.txt", "r")
        people = optf.read()
        if author == "I run on Heroku" or str(authorid) in people:
            pass
        else:
    	    logf.write(f"Time: {datetimela}\nAuthor: {author}#{discri}\nGuild: {guild}\nChannel: {channel}\nMessage: {message}\n\n\n")
        logf.close()
        optf.close()
