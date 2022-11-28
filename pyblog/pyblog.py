"""
Python client for Wordpress
Utilizing the RESTful API provided by Wordpress (docs), write a python CLI tool to read and write blog posts. 
a) Read configuration from the following ENV variables
	WORDPRESS_USERNAME
	WORDPRESS_PASSWORD
	WORDPRESS_URL
	b) Unit tests
⦁	Ensure you unit test as many code paths as you can.
⦁	Include error handling for if the Wordpress API is unavailable or incorrect credentials are provided.
	c) Containerized
⦁	Your CLI tool should be able to run on any machine running docker via a docker container. 
⦁	NOTE, a docker container cannot access files on the host machine, so "upload -f <filename>" may need to be tweaked.  See “CLI Detailed Requirements” below.

Required Functions
⦁	Show latest blog post
⦁	Upload a blog post
Example Usage
python3 pyblog.py <command> [options]

python3 pyblog.py read
	- Outputs the contents of the latest blog post to stdout

python3 pyblog.py upload -f <filename or - >
	- Uploads the contents of the specified file as a new blog post
	- Uses the current time for the post
	- Format of the post file is as follows	
	- NOTE: The literal character '-' as the filename signifies reading file contents from stdin instead of opening a file
"""



