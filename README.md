# TwitFetch

TwitFetch is a Python script that fetches tweets from a list of Twitter usernames and prints them out if they were created after the script was started.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.

## Installation

1. Clone this repository or download the code as a ZIP file.
2. Extract the files to a folder of your choice.
3. Open the fetch.py file with a text editor and replace "YOUR RAPID API KEY HERE" with your own RapidAPI key.
4. Save the changes and close the text editor.

## Usage

1. Create a usernames.txt file in the same directory as the script files, and list the Twitter usernames you want to monitor, one per line.
2. Run twitFetch.py and enter the refresh interval (in seconds) when prompted. The script will then start monitoring the tweets from the specified usernames.

## Dependencies

-    requests library: To install it, run pip install requests.

## Files

-    twitFetch.py: The main script that fetches and displays tweets from the specified Twitter usernames.
-    fetch.py: A helper script that contains functions to fetch Twitter user IDs and tweets using the RapidAPI service.
-    tweet.py: A helper script that contains functions to parse tweet data and display the output.
