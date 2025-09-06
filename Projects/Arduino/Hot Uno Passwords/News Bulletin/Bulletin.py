import urllib.request 
import serial
#import time library for delays 
import time

#import xml parser called minidom: 
from xml.dom.minidom import parseString

#Initialize the Serial connection in COM3 or whatever port your arduino uses at 9600 baud rate
ser = serial.Serial("COM12", 9600)
i = 1
#delay for stability while connection is achieved
time.sleep(5)
while i == 1:
    newsSource = input("what News Source would you like to use? 1= Reuters; 2= BBC; 3 = Fox")
    #download the rss file feel free to put your own rss url in here
    if newsSource == '1':
        http = 'http://feeds.reuters.com/reuters/topNews'
        print ('1aaa')         
    elif newsSource == '2':
        http = 'http://feeds.bbci.co.uk/news/world/asia/rss.xml'
        print ('2bbb')
    elif newsSource == '3':
        http = 'http://feeds.foxnews.com/foxnews/latest'
        print ('3ccc')
    elif newsSource == '':
        time.sleep(30)
        http = 'http://feeds.foxnews.com/foxnews/latest'
    file = urllib.request.urlopen(http)
    #convert to string
    data = file.read()
#close the file
    file.close()
#parse the xml from the string
    dom = parseString(data)
#retrieve the first xml tag (data) that the parser finds with name tagName change tags to get different data
    xmlTag = dom.getElementsByTagName('title')[2].toxml()
    # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
    #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('</p><p>','').replace('<!--[CDATA[','').replace(']]-->','')
    ser.write(b'~')
#split the string into individual words
    nums = xmlData.split(' ')
#loop until all words in string have been printed
    for num in nums:
#write 1 word
        ser.write(num.encode('UTF-8'))
# write 1 space
        ser.write(b' ')
# THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[3].toxml()
    # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
    #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('</p><p>','').replace('<!--[CDATA[','').replace(']]-->','')
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
    #split the string into individual words
    nums = xmlData.split(' ')
    #loop until all words in string have been printed
    for num in nums:
        #write 1 word
        ser.write(num.encode('UTF-8'))
        # write 1 space
        ser.write(b' ')
        # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[4].toxml()
    # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
    #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
    #loop until all words in string have been printed
    for num in nums:
        #write 1 word
        ser.write(num.encode('UTF-8'))
        # write 1 space
        ser.write(b' ')
        # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[5].toxml()
    # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
    #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
         #write the marker ~ to serial
    ser.write(b'~')
    #split the string into individual words
    nums = xmlData.split(' ')
    #loop until all words in string have been printed
    for num in nums:
        #write 1 word
        ser.write(num.encode('UTF-8'))
        # write 1 space
        ser.write(b' ')
        # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[6].toxml()
     # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
     #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
     #loop until all words in string have been printed
    for num in nums:
        #write 1 word
        ser.write(num.encode('UTF-8'))
          # write 1 space
        ser.write(b' ')
          # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[7].toxml()
     # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
     #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
     #loop until all words in string have been printed
    for num in nums:
          #write 1 word
        ser.write(num.encode('UTF-8'))
          # write 1 space
        ser.write(b' ')
          # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[8].toxml()
     # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
     #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
     #loop until all words in string have been printed
    for num in nums:
          #write 1 word
        ser.write(num.encode('UTF-8'))
          # write 1 space
        ser.write(b' ')
          # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[9].toxml()
     # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
     #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
     #loop until all words in string have been printed
    for num in nums:
          #write 1 word
        ser.write(num.encode('UTF-8'))
          # write 1 space
        ser.write(b' ')
          # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[10].toxml()
     # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
     #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
    #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
     #loop until all words in string have been printed
    for num in nums:
          #write 1 word
        ser.write(num.encode('UTF-8'))
          # write 1 space
        ser.write(b' ')
          # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
        time.sleep(1)
    xmlTag = dom.getElementsByTagName('title')[11].toxml()
     # the [2] indicates the 3rd title tag it finds will be parsed, counting starts at 0
     #strip off the tag (data  --->   data)
    xmlData=xmlTag.replace('','').replace('','')
     #write the marker ~ to serial
    ser.write(b'~')
     #split the string into individual words
    nums = xmlData.split(' ')
     #loop until all words in string have been printed
    for num in nums:
          #write 1 word
        ser.write(num.encode('UTF-8'))
          # write 1 space
        ser.write(b' ')
          # THE DELAY IS NECESSARY. It prevents overflow of the arduino buffer.
    time.sleep(1)
#write ~ to close the string and tell arduino information sending is finished
    ser.write(b'~')
# wait 2 seconds before rechecking RSS and resending data to Arduino
    ser.write(b'~TOP TEN NEWS 1= Reuters; 2= BBC; 3 = Fox')
    time.sleep(2)