import fetch
import time
from datetime import datetime, timedelta


# Returns datetime object of current time in UTC
def curTime():
    return datetime.utcnow().replace(microsecond=0) - timedelta(
        seconds=datetime.utcnow()
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .time()
        .second,
        minutes=datetime.utcnow()
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .time()
        .minute,
        hours=datetime.utcnow()
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .time()
        .hour,
    )


# Given a string of format 'day month date hh:mm:ss year', returns a datetime object
def getTimeString(timeString):
    if isinstance(timeString, list):
        dateString = " ".join(timeString)
    dateList = datetime.strptime(dateString, "%a %b %d %H:%M:%S %Y")
    return dateList


# Returns datetime object of tweet time given {tweet} dict
def getTweetTime(tweet):
    tweetTimeString = tweet["time"]
    tweetTime = tweetTimeString.split()
    del tweetTime[4]
    return getTimeString(tweetTime)


# Main script, which fetches and checks for tweets
def fetchTweets(userDict, sleepTime):
    startTime = curTime()
    print("\nChecking for tweets...")
    while True:
        # Tweet Checker
        tweetFound = False
        for username, userID in userDict.items():
            tweetList = fetch.getTweets(userID, 2)
            for tweet in tweetList:
                tweetTime = getTweetTime(tweet)
                if tweetTime > startTime:
                    print(
                        f"New Tweet by {username}.\n> Contents: {tweet['contents']}\n"
                    )
                    tweetFound = True
        if not tweetFound:
            print("No new tweets.")

        timeLeft = sleepTime

        # Countdown Timer
        while timeLeft:
            minutesLeft, secondsLeft = divmod(timeLeft, 60)
            countdownTmer = "Refreshing in: {:02d}:{:02d}".format(
                minutesLeft, secondsLeft
            )
            print(countdownTmer, end="\r")
            timeLeft -= 1
            time.sleep(1)
        print("\n\nChecking for tweets...")
