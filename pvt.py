import praw, time, urllib.request, json, datetime											#Imports packages
reddit = praw.Reddit(client_id="nope",																#Login information
                     client_secret="its a secret",
                     username="pvt-bot",
                     password="super_secret_password",
                     user_agent="some text idk")

subreddit = reddit.subreddit("pewdiepiesubmissions+pewdiepie")				#Subreddits and keyphrase
keyphrase = "!pvt"

num = 0
def run():
    for comment in subreddit.stream.comments():												#Checks each comment
         if keyphrase in comment.body.lower():												#Checks if "!pvt" is in the comment body
            listf = open("comments.txt", "r")
            list = listf.readlines()
            if str(str(comment)+"\n") not in list:										#Checks if the comment is in comments that have already been replied to
                global num
                try:																									#Attempts to leave reply
                    num += 1
                    print("Attemting to leave reply to "+str(comment)+"  |  "+str(datetime.datetime.now())+"  |  "+str(num))
                    listf.close()
                    token = "still not gonna tell you"
                    raw = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+token).read()			#Gets the current sub count of Pewdiepie
                    pewds = int(json.loads(raw)["items"][0]["statistics"]["subscriberCount"])
                    raw = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+token).read()				#Gets the current sub count of T-Gay
                    tgay = int(json.loads(raw)["items"][0]["statistics"]["subscriberCount"])
                    diff = abs(pewds - tgay)													#Calculates the difference
                    ("Difference: "+"{:,d}".format(diff))	
                    if pewds > tgay:																	#Who is leading
                        leading = ("Pewdiepie")
                    else:
                        leading = ("T-series")
                    pewdsr = "{:,d}".format(pewds)										#Formats the number (example: 1234567890 becomes 1,234,567,890)
                    tgayr = "{:,d}".format(tgay)
                    diffr = "{:,d}".format(diff)
                    reply = ("[Pewdiepie](https://youtube.com/user/pewdiepie): "+pewdsr+"\n\n"+"[T-Series](https://youtube.com/user/tseries): "+tgayr+"\n\n"+"Difference: "+diffr+"\n\n"+"Leading: "+leading+"\n\n"+"^(Bot developed by) [^(u/ado1928)](https://reddit.com/user/ado1928)^(. If you have any questions, PM me)")			#Leaves the reply
                    comment.reply(reply)
                    print("Success")
                except:																								#If the operation fails
                    print("Failed, retrying in 1 minute")
                    time.sleep(60)
                    run()
                else:																									#If the operation is completed sucressfully
                    listf = open("comments.txt", "a")
                    print(str(comment)+"\n", file=listf)							#Adds the comment to the comment list
                    listf.close()	
run()



