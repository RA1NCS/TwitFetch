import requests

# Common HTTP Parameters defines to avoid reusage
global HTTP_PARAMETERS
HTTP_PARAMETERS = {
    "X-RapidAPI-Key": "73d82610b7msheaba598fed24841p1e0f71jsn6bfe6217691f",
    "X-RapidAPI-Host": "twitter135.p.rapidapi.com",
}


# Returns JSON response of webpage given URL adn Query
def getJSON(HTTP_URL, HTTP_QUERY):
    return requests.get(HTTP_URL, headers=HTTP_PARAMETERS, params=HTTP_QUERY).json()


# Returns Twitter UserID of a user given their username
def getUserID(userName):
    HTTP_URL = "https://twitter135.p.rapidapi.com/UserByScreenName/"
    HTTP_QUERY = {"username": userName}

    HTTP_JSON = getJSON(HTTP_URL, HTTP_QUERY)

    return HTTP_JSON["data"]["user"]["result"]["rest_id"]


# Returns a list containing past tweets (number of tweets to get is a parameter)
def getTweets(userID, tweetsToGet):
    HTTP_URL = "https://twitter135.p.rapidapi.com/UserTweets/"
    HTTP_QUERY = {"id": userID, "count": tweetsToGet}

    HTTP_JSON = getJSON(HTTP_URL, HTTP_QUERY)
    tweetInstructions = HTTP_JSON["data"]["user"]["result"]["timeline"]["timeline"][
        "instructions"
    ]

    tweetList = []
    # Filtering Dictionary
    for instruction in tweetInstructions:
        if instruction["type"] == "TimelineAddEntries":
            for entry in instruction["entries"]:
                content = entry["content"]
                if content["entryType"] == "TimelineTimelineItem":
                    itemContent = content["itemContent"]
                    if itemContent["itemType"] == "TimelineTweet":
                        tweetObject = itemContent["tweet_results"]["result"]
                        tweetData = tweetObject["legacy"]
                        tweetContents = tweetData["full_text"]

                        # Data Extraction
                        if not tweetContents.startswith("RT @"):
                            tweetTime = tweetData["created_at"]
                            likeCount = tweetData["favorite_count"]
                            retweetCount = tweetData["retweet_count"]
                            commentCount = tweetData["reply_count"]

                            currentTweet = {
                                "time": tweetTime,
                                "contents": tweetContents,
                                "likes": likeCount,
                                "retweets": retweetCount,
                                "comments": commentCount,
                            }

                            tweetList.append(currentTweet)

    return tweetList
