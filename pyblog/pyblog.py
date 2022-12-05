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



### THIS IS AN UPDATE TO THE PYBLOG.PY FILE - USED TO TEST THE MANUAL PIPELINE FOR BAMBOO

wp_user = "nfi_wordpress" #stone in an env
wp_pass = "nfi_wordpass" #store in an env 
wp_site = "wp site address here"

#  
# API auth goes here
# r = request.get(wp_site)
#

#Build ArgPrase

cli_parser = argparse.ArgumentParser(
    prog = 'WordPress CLI',
    description= "Interact with the Wordpress API",
    epilog= 'Thank you for coming to my Ted Talk!')

cli_parser.add_argument('command', type=str)
cli_parser.add_argument(
    '-f',
    '--file',
    help="Intentionally left blank."
    )
cli_parser.add_argument(
    'text_input',
    nargs='?',
    type=str,
    default="-",
    help="Intentionally left blank."
    )

args = cli_parser.parse_args()

def format_blog(file):
    contents = file.read()
    contents = contents.splitlines()
    title = contents[0]
    body = "\n".join(contents[1:])
    print(title)
    print(body)
    file.close()


# read from stdin - i

def blog_upload():
    cli_input = args.file or args.text_input
    if cli_input == "-":
        file = sys.stdin
        format_blog(file)

    else:
        file = open(cli_input)
        format_blog(file)

def blog_read():
    print("this is where we will pull from the API and read the lastest blog")
    #need to define api calls here
    #need to pull in post and print it likly with pprint or json


if args.command == "upload":
    print("Looking to upload a file")
    blog_upload()
if args.command == "read":
    blog_read()
