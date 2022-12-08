import requests
import datetime
import argparse
import json
import sys
import os
import pprint
from dotenv import load_dotenv

load_dotenv()

currenttime = datetime.datetime.now()
blog_timestamp = datetime.datetime.now().strftime("%c")

wp_user = os.environ.get('WP_USER') #stored in an env
wp_pass = os.environ.get('WP_PASS') #stored in an env
wp_url = os.environ.get('WP_HOST') #stored in an env

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
    blog_title = contents[0]
    blog_body = "\n".join(contents[1:])
    return blog_post(blog_title,blog_body)
    file.close()

def blog_post(blog_title, blog_body):
    post_url = wp_url + '/wp-json/wp/v2/posts' 
    auth = wp_user + ":" + wp_pass
    data = {
        'title': blog_title, 
        'status':'publish', 
        'content': blog_body, 

    }
    response = requests.post(url = post_url ,auth=(wp_user,wp_pass), data = data)
    return response

def blog_upload():
    cli_input = args.file or args.text_input
    if cli_input == "-":
        file = sys.stdin
        return format_blog(file)

    else:
        file = open(cli_input)
        return format_blog(file)
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

def blog_posts():
    response = requests.get(wp_url + "/wp-json/wp/v2/posts/?_fields=id,title,excerpt")
    response = response.json()
    num_of_posts = len(response)
    count = 0
    while count < num_of_posts:
        id = response[count]['id']
        title = response[count]['title']['rendered']
        excerpt = response[count]['excerpt']['rendered']
        excerpt = excerpt.replace('<p>', '').replace('</p>', '') 
        count += 1
        print(f'Post {count}: \n ID: {id} \n Title: "{title}" \n Preview: "{excerpt}"')

if args.command == "upload":
    print(blog_upload())
if args.command == "read":
    print(blog_read())
if args.command == "posts":
    blog_posts()