import argparse
# pip install whois
import whois
# pip install socket
import socket
# pip install python-nmap
import nmap
# pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
# pip install selenium
from selenium import webdriver
import webbrowser
import re

# This function is to find the links on the site :
def Find_Links(url):
    global links
    links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('http'):
            links.append(href)
    return links
            
# # This function saves found links in txt and html files :
# def Save_Links_in_HTML_and_Save_Links_in_TXT(url):
#     f = open("links.html", "w", encoding="utf-8")
#     f.write("<h1>" + " URL = " + str(url))
#     for i in range(len(links)):
#         try:
#             response2 = requests.get(links[i])
#             f.write("<h4>" + f"{links[i]}----->>> Status Code:{response2.status_code}"+"\n")
#         except requests.exceptions.RequestException as e:
#             pass
#     f.close()
#     f2 = open("links.txt", "w", encoding="utf-8")
#     for i in range(len(links)):
#             f2.write(str(links[i])+"\n")
#     f2.close()
    
# # This function goes deep into two sites and saves the found links :
# def append_links_Depthtwo_to_html(links):
#     f = open("Depthtwo.html", "w", encoding="utf-8")
#     for url2 in links:
#         f.write("<hr>")
#         f.write("<h2>" + str(url2) + "\n")
#         response2 = requests.get(url2)
#         try:
#             response2 = requests.get(url2)
#             if response2.status_code == 200:
#                 soup2 = BeautifulSoup(response2.content, 'html.parser') 
#                 if soup2 is not None:
#                     for link2 in soup2.find_all('a'):
#                         href2 = link2.get('href')
#                         if href2 is not None and href2.startswith('http'):
#                             f.write("<h4>" + f" {href2}----->>> Status Code:{response2.status_code}" + "\n")
#         except requests.exceptions.RequestException as e:
#             f.write("<h1>" + f" {url2}----->>> Status Code:{response2.status_code}" + "\n")
#     f.close()
# # This function finds and enters the subdomains of the site and finds the links inside them :
# def Find_Subdomain(ur):
#     with open("wordlist.txt", "r", encoding="utf-8") as f:
#         with open("SubdomainANDLinks.html", "w", encoding="utf-8") as f2:
#             with open("SubdomainANDLinks.txt", "w", encoding="utf-8") as f3:
#                 for line in f:
#                     sub = line.strip()
#                     Subdomain = f"http://{sub}{ur}/"
#                     Subdomain_IP = f"{sub}{ur}"
#                     IP_Str=""
#                     try:
#                         try:
#                             ip_address = socket.gethostbyname(Subdomain_IP)
#                             IP_Str=str(ip_address)
#                         except socket.error as IPP:
#                             IP_Str="¯\_(ツ)_/¯"
#                         response = requests.get(Subdomain)
#                         if response.status_code != 404:
#                             f2.write("<hr>")
#                             f2.write("<h1>"+Subdomain+f"----->>> Status Code:{response.status_code} ----->>> IP:[{IP_Str}]"+"</h1>"+"\n")
#                             soup = BeautifulSoup(response.content, 'html.parser')
#                             for link in soup.find_all('a'):
#                                 href = link.get('href')
#                                 if href is not None and href.startswith('http'):
#                                     try:
#                                         response2 = requests.get(href)
#                                         f2.write("<h3>"+href+f"----->>> Status Code:{response2.status_code}"+"</h3>"+"\n")
#                                     except requests.exceptions.RequestException as e:
#                                         f2.write("<h3>"+href+f"----->>> Status Code: ¯\_(ツ)_/¯"+"</h3>"+"\n")
#                             f3.write(Subdomain+"\n")
#                     except requests.exceptions.RequestException as e:
#                         pass

# # def Find_Subdomain_links_Depthtwo():
# #     with open("SubdomainANDLinks.txt", "r", encoding="utf-8") as f:
# #         with open("SubdomainDepthtwo.html", "w", encoding="utf-8") as f2:
# #             for line in f:
# #                     Subdomain = line.strip()
# #                     try:
# #                         response = requests.get(Subdomain)
# #                         if response.status_code != 404:
# #                             f2.write("<hr>")
# #                             f2.write("<h1>"+Subdomain+"</h1>"+"\n")
# #                             soup = BeautifulSoup(response.content, 'html.parser')
# #                             for link in soup.find_all('a'):
# #                                 href = link.get('href')
# #                                 if href is not None and href.startswith('http'):
# #                                     try:
# #                                         response = requests.get(href)
# #                                         f2.write("<h3>"+href+f"----->>> Status Code:{response.status_code}"+"</h3>"+"\n")
# #                                     except requests.exceptions.RequestException as e:
# #                                         f2.write("<h3>"+href+f"----->>> Status Code: ¯\_(ツ)_/¯"+"</h3>"+"\n")
# #                     except requests.exceptions.RequestException as e:
# #                         pass

# # This function saves the open ports of the site in the html file


# # This function performs the regex operation for the original URL





# # This function performs the whois operation

# # This function takes a screenshot of the desired site
# def Screenshot(url):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.get_screenshot_as_file("screenshot.png")
#     driver.quit()
# # arg function
# def find_link():
#     url = args.find_link
#     Find_Links(url)
#     print("<Links found>")
#     Save_Links_in_HTML_and_Save_Links_in_TXT(url)
#     print("<Links saved>")
#     Link_HTML = 'links.html'
#     webbrowser.open_new_tab(Link_HTML)
# # ><><><><><><><><><><
# def find_D2L():
#     url = args.find_D2L
#     Find_Links(url)
#     Save_Links_in_HTML_and_Save_Links_in_TXT(url)
#     print("<Start entering the program in depth 2>")
#     append_links_Depthtwo_to_html(links)
#     print("<Leaving the program from depth 2>")
#     Depth_tow = 'Depthtwo.html'
#     webbrowser.open_new_tab(Depth_tow)
# # ><><><><><><><><><><
# def find_Subdomain():
#     url = args.find_Subdomain
#     url = url.replace("http://", ".").replace("https://", ".").replace("www.", ".")
#     print("<Start fnding subdomains>")
#     Find_Subdomain(url)
#     SubdomainANDLinks_HTML = 'SubdomainANDLinks.html'
#     webbrowser.open_new_tab(SubdomainANDLinks_HTML)
# # ><><><><><><><><><><
# def find_Port():
#     url = args.find_port
#     url = url.replace("http://", "www.").replace("https://", "www.")
#     print("<Start finding open ports>")
#     Find_Port(url)
#     Port_HTML = 'Port.html'
#     webbrowser.open_new_tab(Port_HTML)
# # ><><><><><><><><><><
# def regex():
#     url = args.regex
#     url = url.replace("http://", ".").replace("https://", ".").replace("www.", ".")
#     print("<Start fnding subdomains>")
#     Find_Subdomain(url)
#     print("<Start Regex>")
#     Regex()
#     Regex_HTML = 'Regex.html'
#     webbrowser.open_new_tab(Regex_HTML)
# # ><><><><><><><><><><
# def whois_arg():
#     url = args.whois
#     url = url.replace("http://", "").replace("https://", "").replace("www.", "")
#     print("<Start whois>")
#     get_whois(url)
#     Whois_TXT = 'Whois.txt'
#     webbrowser.open_new_tab(Whois_TXT)
# # ><><><><><><><><><><
# def all():
#     url = args.start_all
#     urlCopy = url
#     Find_Links(url)
#     print("<Links found>")
#     Save_Links_in_HTML_and_Save_Links_in_TXT(url)
#     print("<Links saved>")
#     print("<Start entering the program in depth 2>")
#     append_links_Depthtwo_to_html(links)
#     print("<Leaving the program from depth 2>")
#     url1 = urlCopy.replace("http://", ".").replace("https://", ".").replace("www.", ".")
#     # print("<Start fnding subdomains>")
#     # Find_Subdomain(url1)
#     url1 = urlCopy.replace("http://", "www.").replace("https://", "www.")
#     print("<Start fnding ports>")
#     # Find_Subdomain_links_Depthtwo()
#     Find_Port(url1)
#     print("<Start Regex>")
#     Regex()
#     url1 = url.replace("http://", "").replace("https://", "").replace("www.", "")
#     print("<Start whois>")
#     get_whois(url1)
#     print("<Take Webpage Screenshot>")
#     Screenshot(url)
#     # Open all html files
#     Link_HTML = 'links.html'
#     webbrowser.open_new_tab(Link_HTML)
#     Depth_tow = 'Depthtwo.html'
#     webbrowser.open_new_tab(Depth_tow)
#     SubdomainANDLinks_HTML = 'SubdomainANDLinks.html'
#     webbrowser.open_new_tab(SubdomainANDLinks_HTML)
#     Port_HTML = 'Port.html'
#     webbrowser.open_new_tab(Port_HTML)
#     Regex_HTML = 'Regex.html'
#     webbrowser.open_new_tab(Regex_HTML)
#     Whois_TXT = 'Whois.txt'
#     webbrowser.open_new_tab(Whois_TXT)
#     Screenshot_PNG = 'screenshot.png'
#     webbrowser.open_new_tab(Screenshot_PNG)
# # ><><><><><><><><><><

# parser = argparse.ArgumentParser(description='Process some inputs.')
# parser.add_argument('--find-link', type=str, help='The process finds links')
# parser.add_argument('--find-D2L', type=str, help='This process finds links of depth two')
# parser.add_argument('--find-Subdomain', type=str, help='This process finds the links in the subdomains of the site')
# parser.add_argument('--find-port', type=str, help='This process finds the open ports of the site')
# parser.add_argument('--regex', type=str, help='This process performs regex operations')
# parser.add_argument('--whois', type=str, help='This process performs the whois operation')
# parser.add_argument('--start-all', type=str, help='Performs all tasks related to recon')

# args = parser.parse_args()

# if args.find_link:
#     find_link()
# elif args.find_D2L:
#     find_D2L()
# elif args.find_Subdomain:
#     find_Subdomain()
# elif args.find_port:
#     find_Port()
# elif args.regex:
#     regex()
# elif args.whois:
#     whois_arg()
# elif args.start_all:
#     all()
# else:
#     print("No valid operation provided.")
# # FATHI
# print("""                               
#                           ..::::::::::::::..                          
#                      .::^::..            ..::^::.                     
#                   .:^:.                        .:^:.                  
#                 :^^.                              .:^:                
#               :^:                                    :^:              
#             .^^                                        :^.            
#            :^.                                          .^:           
#           ^^.                                            .^^          
#          ^^.                                              .^^         
#          ..                                                ...        
#         ..........     ..      ...........   .        .     .         
#         :^.           .^^:         .^:       ~.       ~.   .~.        
#         :^            ^. ^:         ^:       ^.       ^.   .^.        
#         :^......     ^:   ^.        ^:       ^:.......^.   .^.        
#         :^.         :^.   :^.       ^:       ^:      .^.   .^.        
#         :^         .^......:^       ^:       ^.       ^.   .^.        
#         :^        .^.       :^      ^:       ~.       ~.   .~.        
                                                                      
#           :^.                                            .^:          
#            :^.                                          .^^           
#             .^:                                        :^.            
#               :^:                                    :^:              
#                 :^:.                              .:^:                
#                   .:^:.                        .:^:.                  
#                      .::^::..            ..::^::.                     
#                           ..::::::::::::::..                          """)