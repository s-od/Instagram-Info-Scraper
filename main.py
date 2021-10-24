##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#Copyright 2021 JimmeyC                                                                                                                                                                                                                                                                                                                                                                                                                                                       #
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:                            #
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.                                                                                                                                                                                                                                                                                                                                              #
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.#
##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#imports
from os import mkdir, system
import pyinsta, time, os, pathlib, webbrowser
from os import name,system
from pyinsta.download import post, profile_pic
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#defines
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#make all of the directories

googledrive = input('Are you wanting the files to go to google drive: y/n: ')
if googledrive.capitalize() == 'Y':
    webbrowser.open('https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf')
    gauth = GoogleAuth()           
    drive = GoogleDrive(gauth)  
ndir = os.path.join(os.getcwd(),'/Insta-stuff')
if not os.path.exists(ndir):
    mkdir(ndir)


ndirr = os.path.join(os.getcwd(),'/Lists')
if not os.path.exists(ndirr):
    mkdir(ndirr)

while True:
    clear()
    print('Instagram info and photo scraper')
    print('By JimmeyC')
    print()
    print()
    print('0. Exit')
    print('1. Instagram Photo Scraper')
    print('2. Instagram Account info Scraper')
    print('3. Instagram Photo and Info Scraper')
    print('4. Other')
    option = int(input('Choose a option: '))
    if option == 0:
        clear()
        exit()
    elif option == 1:
        clear()
    elif option == 2:
        clear()
    elif option == 3:
        clear()
        time.sleep(1)
        try:
            f = open(ndirr+'/List.txt', 'r')
        except FileNotFoundError:
            print('Please make sure the List.txt file is in the folder of:\n'+ndirr)
         

    



