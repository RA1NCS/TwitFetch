from tweet import fetchTweets
from fetch import getUserID


# Returns dictionary in the format {username:userID} for twitter users
def getIDList():
    idList = {}
    with open("usernames.txt", "r") as usernames:
        for username in usernames.readlines():
            try:
                username = username.strip()
                userID = getUserID(userName=username)
                idList.update({username: userID})
            except KeyError:
                print(f"'{username}' is not a twitter account, skipping.")
    return idList


# Final Program to run the script
if __name__ == "__main__":
    try:
        sleepTime = int(
            input(
                "Enter the time (in seconds) after which the script should refresh for new tweets:\n> "
            )
        )

    except ValueError:
        print("Invalid input, defaulting to 60 seconds.\n")
        sleepTime = 60

    userDict = getIDList()
    fetchTweets(userDict=userDict, sleepTime=sleepTime)
