import requests

prod_wp_url = 'http://ec2-3-22-183-132.us-east-2.compute.amazonaws.com:8088'

def test_wp_site():
    r = requests.get(prod_wp_url)
    if r.status_code == 200:
        print("Prod WordPress server is active")
    else:
        print("Wordpress server may need attention")
test_wp_site()