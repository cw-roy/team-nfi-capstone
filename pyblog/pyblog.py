import requests
import datetime
import argparse
import json
import sys
import os
import pprint
from requests.auth import HTTPBasicAuth


currenttime = datetime.datetime.now()
blog_timestamp = datetime.datetime.now().strftime("%c")

# setup auth from env

wp_user = "retrieve from elsewhere"
wp_pass = "retrieve from elsewehre"
wp_site = "{wordpress url goes here}"

# Generate the CLI argmuments

# basic arg parse setup
cli_parse = argparse.ArgumentParser(
    prog = 'WordPress CLI',
    description= "interact with the wp API",
    epilog= 'Thank you for coming to my Ted Talk!')

# -f , --File to identify a file to be uploaded to WP Blog
# "-" the character "-" to read from stdin


cli_parse.add_argument(
    'filename',
    help="Please choose a filepath. ex: c:/users/document.txt")
args = cli_parse.parse_args()

with open(args.filename, "r") as file:
    title = file.readlines()[0]
    
    print(title)