import requests
from pprint import pprint as pp
import json

wp_user = "nfi_wordpress" #stored in an env
wp_pass = "nfi_wordpass" #stored in an env 
wp_url = 'http://ec2-3-22-183-132.us-east-2.compute.amazonaws.com:8088'

response = requests.get(wp_url + "/wp-json/wp/v2/posts/?_fields=id,title,excerpt")
response = response.json()

num_of_posts = len(response)

def blog_posts():
    count = 0
    while count < num_of_posts:
        id = response[count]['id']
        title = response[count]['title']['rendered']
        excerpt = response[count]['excerpt']['rendered']
        excerpt.strip('"<p>","</p>"')
        count += 1
        print(f'Post {count}: \n ID: {id} \n Title: "{title}" \n Preview: {excerpt}')
blog_posts()