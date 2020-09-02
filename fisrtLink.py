import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("5nvpPoNoDwnMZMyyLTMxBiWUG", 
    "pr0tcQXz8brKndmheqpwbSuLOSoHQHLVlRpO15eCJemwTop5FS")
auth.set_access_token("1255513158011228163-LSTYrgqjkDcgchHQIDQJenqq06egMG", 
    "L426blPjvQLDGLKghGM9Nbfg6tEonooxjoS6Ho0HAiSyR")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
sports_list = ["football", "soccer", "golf", "wrestling", "basketball", "wheelchair basketball", "swimming", "bowling", "track", "baseball"]
message_list = ["GO Blue Devils!", "T-Town Beatdown!", "Go big blue!", "#TOGETHERWE"]
x = 0
while True:

    AD_Timeline = api.user_timeline("mike_yamo")
    
    for tweet in AD_Timeline:
        text = tweet.text
        text.lower()
        f = open("idList.txt", "r")
        previous_ids = f.readline()
        
        isUnique = True
        if previous_ids.find(str(tweet.id)) > -1:
            isUnique = False
            print("previous Id")
        
        if (text.find("congrat") > -1 or text.find("win") > -1 or text.find("shout out") > -1 or text.find("won") > -1 or text.find("shoutout") > -1 or text.find("beat") > -1) and isUnique:
            f = open("idList.txt", "a")
            f.write(str(tweet.id))
            f.write(" ")
            sport_name = ""
            for sport in sports_list:
                if text.find(sport) > -1:
                    sport_name = " " + sport
            gender = ""
            if text.find("girl") > -1:
                gender = " girls"
            elif text.find("boy") > -1:
                gender = " boys"
            i = 6
            grade = ""
            while i <= 12 and grade == "":
                if text.find(" " + str(i)) > -1:
                    grade = " " + str(i) + "th grade"
                i += 1
            if len(sport_name) + len(gender) + len(grade) > 0:
                new_post = ""
                
                new_post = "Congrats to our" + grade + gender + sport_name + " team. " + message_list[x % 4]            
                print(text)
                print(new_post)
                api.update_status(new_post)
                x += 1
    time.sleep(86400)
    
