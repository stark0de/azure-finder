import dns.resolver
from colorama import Fore, init
from termcolor import colored
import sys

init()

if len(sys.argv) != 2:
    print(Fore.RED+"Usage: python3 azure-finder.py listwithdomains")
    sys.exit()

urls=open(sys.argv[1],"r").readlines()
#print(urls)

strings=['.accesscontrol.windows.net', '.graph.windows.net','.onmicrosoft.com', '.azure-api.net', '.biztalk.windows.net', '.blob.core.windows.net', '.cloudapp.net', '.cloudapp.azure.com', '.azurecr.io', '.azurecontainer.io', '.vo.msecnd.net', '.file.core.windows.net', '.azurefd.net', '.management.core.windows.net', '.origin.mediaservices.windows.net', '.azure-mobile.net', '.queue.core.windows.net', '.servicebus.windows.net', '.database.windows.net', '.azureedge.net', '.table.core.windows.net', '.trafficmanager.net', '.azurewebsites.net', '.visualstudio.com']
resolver = dns.resolver.Resolver()
for j in urls:
    #print(j.strip)
    try:
       answers = resolver.query(j.strip(), 'CNAME')
       for rdata in answers:
           for i in strings:
               if i in rdata.to_text():
               #print(rdata.to_text)
                  print(Fore.GREEN+"[+] Azure asset found in "+j.strip()+" !!"+Fore.WHITE)
    except:
        continue
