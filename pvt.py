import praw, time, urllib.request, json, datetime
reddit = praw.Reddit(client_id="nope",
                     client_secret="not gonna tell you",
                     username="pvt-bot",
                     password="super_secret_password",
                     user_agent="some text idk")

subreddit = reddit.subreddit("pewdiepiesubmissions+pewdiepie")
keyphrase = "!pvt"
num = 0
def run():
    for comment in subreddit.stream.comments():
         if keyphrase in comment.body.lower():
            listf = open("comments.txt", "r")
            list = listf.readlines()
            if str(str(comment)+"\n") not in list:
                global num
                try:
                    num +=1
                    print("Attemting to leave reply to "+str(comment)+"  |  "+str(datetime.datetime.now())+"  |  "+str(num))
                    listf.close()
                    token = "not gonna tell you"
                    raw = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+token).read()
                    pewds = int(json.loads(raw)["items"][0]["statistics"]["subscriberCount"])
                    raw = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+token).read()
                    tgay = int(json.loads(raw)["items"][0]["statistics"]["subscriberCount"])
                    raw = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC-9-kyTW8ZkZNDHQJ6FgpwQ&key="+token).read()
                    music = int(json.loads(raw)["items"][0]["statistics"]["subscriberCount"])
                    diff = abs(pewds - tgay)
                    musicd = abs(pewds - music)
                    if pewds > tgay:
                        leading = ("Pewdiepie")
                    else:
                        leading = ("T-series")
                    pewdsr = "{:,d}".format(pewds)
                    tgayr = "{:,d}".format(tgay)
                    diffr = "{:,d}".format(diff)
                    musicr = "{:,d}".format(musicd)
                    reply = ("[Pewdiepie](https://youtube.com/user/pewdiepie): "+pewdsr+"\n\n"+"[T-Series](https://youtube.com/user/tseries): "+tgayr+"\n\n"+"Difference: "+diffr+"\n\n"+"Leading: "+leading+"\n\n"+"Difference between Youtube Music and Pewdiepie: "+musicr+"\n\n"+"^(You can find discussion about the bot) [^(here)](https://www.reddit.com/user/ado1928/comments/b8jz09/pvt_bot_discussion/)")
                    comment.reply(reply)
                    print("Success")
                except:
                    print("Failed, retrying in 5 seconds")
                    time.sleep(5)
                    run()
                else:
                    listf = open("comments.txt", "a")
                    print(str(comment)+"\n", file=listf)
                    listf.close()
run()




