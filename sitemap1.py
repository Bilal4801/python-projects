from domain_validation.whois import WHOIS
import argparse
import sys
import logging
from pysitemap import crawler
import os
import random  

parser = argparse.ArgumentParser()
parser.add_argument('-geturl', type=str, required=True, help='Enter your url')
args = parser.parse_args()

url = args.geturl

project_dir = os.path.abspath(os.path.dirname(__file__))



# url="https://www.prepostseo.com"
domainname=url.split("www.")[-1]
webname=domainname.split(".")[0]


# print(domainname)

whois = WHOIS(domainname)

if whois.registrar() != "Registrar_not_found":
    createdir=project_dir+"/upload/output/"
    randomname = random.randint(1000, 10000)
    try:
        os.makedirs(createdir)    
        print("Directory " , createdir ,  " Created ")
    except FileExistsError:
        print("Directory " , createdir ,  " already exists")
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    # root_url = sys.argv[1]
    root_url = url
    crawler(root_url, out_file=f'{project_dir}/upload/output/{webname}{randomname}sitemap.xml', exclude_urls=[".pdf", ".jpg", ".zip"])
    print('{project_dir}/upload/output/{webname}{randomname}sitemap.xml')
else:
    print("domin not found")