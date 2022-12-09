import requests
import os


prod_wp_url = os.environ.get('WP_HOST') #stored in an env
stage_wp_url = os.environ.get('WP_STAGE') #stored in an env

def prod_wp_site():
    r = requests.get(prod_wp_url)
    if r.status_code == 200:
        print("Prod WordPress server is active")
    else:
        print("Wordpress server may need attention")
prod_wp_site()


def stage_wp_site():
    r = requests.get(prod_wp_url)
    if r.status_code == 200:
        print("Staging WordPress server is active")
    else:
        print("The Staging Wordpress server may need attention")
stage_wp_site()