import requests
import mmh3
import codecs
import argparse
import sys

if __name__ =="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--domain", help="Domain name (only the domain name ex: google.com)")
	parser.add_argument("-u", "--url", help="Entire URL (make sure the URL returns the ico file as image like png,jpg,etc.)")
	args = parser.parse_args()
	
	if args.domain and args.url:
		sys.exit("Error: can not use both --domain and --url arguments at the same time.")
	
	if not args.domain and not args.url:
		sys.exit("Error: none of the --domain or --url arguments have been used.")
		
	r = ""
	
	if args.domain:
		r = requests.get("https://www.google.com/s2/favicons?domain=" + args.domain)
		# alternative
		# r = requests.get("https://icons.duckduckgo.com/ip3/" + args.domain + ".ico")
		
	if args.url:
		r = requests.get(args.url)
		# If you use the URL option you can search the links for the favicon using or inside the following:
		# www.domain.com/favicon.ico
		# <link rel="shortcut icon" href="/favicon.ico" />
		# <link rel="icon" href="/favicon.png" />
		# <link rel="apple-touch-icon" href="images/touch.png" />
		# <link rel="apple-touch-icon-precomposed" href="images/touch.png" />
	
	# we use response.content because we need the binary format of the image file
	favicon = codecs.encode(r.content, "base64")
	iconhash = mmh3.hash(favicon)
	print(iconhash)
	
