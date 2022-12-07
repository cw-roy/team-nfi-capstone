import requests

## Build testing for API /// If available,

# test if online?
wp_user = "nfi_wordpress" #stored in an env
wp_pass = "nfi_wordpass" #stored in an env 
wp_url = 'http://ec2-3-22-183-132.us-east-2.compute.amazonaws.com'
port = ':8088' 

r = requests.get(wp_url + port)
print(r)

def test_wp_site():
    r = requests.get(wp_url + port)
    if r.status_code == "200":
        print("The WP Server is online")
    else:
        print("There may be an issue here.")
        return r.status_code


# Healthcheck ??

#200 = OK Indicates that the request has succeeded.
# Possible to write an if statement and ping the WP site? If it returns online send status code of..? 
# 2xx = positive 
# 200 = OK Indicates that the request has succeeded.
# 4xx Status Codes (Client Error)
# 400 =