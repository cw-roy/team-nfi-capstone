import requests
import os

prod_wp_url = os.environ.get('WP_HOST') #stored in an env

def test_wp_site():
    r = requests.get(prod_wp_url)
    if r.status_code == 200:
        print("Prod WordPress server is active")
    else:
        print("Wordpress server may need attention")
test_wp_site()