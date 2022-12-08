import requests
import os
import json
import base64
import datetime

"""
This is a file used for working on functions
"""


#format needed 2022-12-07T16:37:53

wp_user = "nfi_wordpress" #stored in an env
wp_pass = "nfi_wordpass" #stored in an env 
wp_url = 'http://ec2-3-22-183-132.us-east-2.compute.amazonaws.com:8088'

# wordpress_user = "nfi_shane"
# wordpress_password = "O3N!sp0nsha89b!Y5HvX3EFp"
blog_timestamp = datetime.datetime.now().isoformat(timespec = 'seconds')
print(blog_timestamp)


def create_wordpress_post():
    post_url = wp_url + '/wp-json/wp/v2/posts' 
    data = {
        'title':"blog_title", 
        'status':'publish', 
        'content': "blog_content", 
        'date': blog_timestamp
    }
    response = requests.post(url = post_url ,auth=(wp_user, wp_pass), data = data)
    print(response)
print(create_wordpress_post())


# def blog_read():
#     url = wp_url + "/wp-json/wp/v2/posts?per_page=1"
#     r = requests.get(url)
#     print(r)

#     pyblog_gather_data = r.json()

#     link = pyblog_gather_data[0]['link']
#     title = pyblog_gather_data[0]['title']['rendered']
#     body = pyblog_gather_data[0]['content']['rendered']
#     body = body.strip('"\n"')
#     body = body.replace('<p>', '').replace('</p>', '') 
#     return f'Title:\n{title}\n\nBody:\n{body}'

# print(blog_read())


















# currenttime = datetime.now()
# currenttime = currenttime.isoformat()




# wordpress_credentials = wp_user + ":" + wp_pass
# token = base64.b64encode(wordpress_credentials.encode())
# header = {'Authorization': 'Basic ' + token.decode('utf-8')}
# post = {
#  'title' : 'Example wordpress post',
#  'status': 'publish',
#  'content': 'This is the content of the post',
#  }
# responce = requests.post(wp_url, headers=header, json=post)
# print(responce)



# # # def blog_posts():
# # #     response = requests.get(wp_url + "/wp-json/wp/v2/posts/?_fields=id,title,excerpt")
# # #     response = response.json()
# # #     num_of_posts = len(response)
# # #     count = 0
# # #     while count < num_of_posts:
# # #         id = response[count]['id']
# # #         title = response[count]['title']['rendered']
# # #         excerpt = response[count]['excerpt']['rendered']
# # #         excerpt = excerpt.replace('<p>', '').replace('</p>', '') 
# # #         count += 1
# # #         print(f'Post {count}: \n ID: {id} \n Title: "{title}" \n Preview: "{excerpt}"')

# # # # def delete_blog_post():
# # # #     blog_posts()
# # # #     post_id = input("Which blog ID would you like to delete: " )
# # # #     post_id = int(post_id)
# # # #     url = f'{wp_url}/wp/v2/posts/{post_id}?force=true'
# # # #     requests.delete(url,auth=basic)
# # # # delete_blog_post()


# # ### Create a blog post from file or input;

# # # def blog_post():
# # #     api_url = wp_url + '/wp-json/wp/v2/posts'
# # #     data = {
# # #     'title' : 'Example wordpress post',
# # #     'status': 'published',
# # #     'content': 'This is the content of the post'
# # #     }
# # #     response = requests.post(api_url,headers=Headers, json=data)
# # #     print(response)
# # # blog_post()