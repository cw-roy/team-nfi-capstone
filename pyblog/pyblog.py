import requests
import datetime
import argparse
import json
import sys
import os
import pprint
# from requests.auth import HTTPBasicAuth

currenttime = datetime.datetime.now()
blog_timestamp = datetime.datetime.now().strftime("%c")

# setup auth from env

### THIS IS AN UPDATE TO THE PYBLOG.PY FILE - USED TO TEST THE MANUAL PIPELINE FOR BAMBOO

wp_user = "nfi_wordpress" #stored in an env
wp_pass = "nfi_wordpass" #stored in an env 
wp_url = 'http://ec2-3-22-183-132.us-east-2.compute.amazonaws.com:8088'


# API auth goes here

#header = (wp_user,wp_pass)

def online_test():
    pass

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
        return format_blog(file)
        # api call here

    else:
        file = open(cli_input)
        format_blog(file)
        # api call here
    # no error handling

def blog_read():
    url = wp_url + "/wp-json/wp/v2/posts?per_page=1"
    r = requests.get(url)

    pyblog_gather_data = r.json()

    link = pyblog_gather_data[0]['link']
    title = pyblog_gather_data[0]['title']['rendered']
    body = pyblog_gather_data[0]['content']['rendered']
    body = body.strip('"\n"')
    body = body.replace('<p>', '').replace('</p>', '') 
    return f'Title:\n{title}\n\nBody:\n{body}'

def blog_delete():
    method = "post"
    url = wp_url + "/wp-json/wp/v2/posts?per_page=1_?_method=DELETE"
    r = requests.post(url)
    



if args.command == "upload":
    blog_upload()
if args.command == "read":
    print(blog_read())
if args.command == "delete":
    blog_delete()