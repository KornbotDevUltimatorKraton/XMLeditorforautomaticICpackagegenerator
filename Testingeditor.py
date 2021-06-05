import os 
import json #import the config file to checking the package running in the xml list data
import subprocess
import xml.etree.ElementTree as ET
import difflib #Finding the similarlity of the matching sequence 

tree = ET.parse("WSON.lbr")  #Loading the lbr file from the package recheck from the OS python library 
root = tree.getroot()       
for child in root: 
       print(child.tag,child.attrib)
print(root[0][0].text)
#Getting the intersection function for the list data processing 
os.system("echo 'Rkj3548123' | sudo -S mkdir Configuresearch") #Create the configure file for the search in json 
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 Configuresearch") # Activate the permission

username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file
listconfig = os.listdir(CONFIG) #Getting the directory in the configsearch directory 
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3  
def show(elem):
      print(elem.tag)
      for child in elem.findall('*'):
            show(child)
#for grid in root.iter('grid'):
#     print(grid.attrib)  
#for eagle in root.iter('eagle'):
#     print(eagle.attrib)   #Getting the eagle version data 
Dataindex = 'VM'
for drawing in root.findall('drawing'):
        print("Found drawing")
        print(drawing.attrib)
        if drawing.find('library'):
            print("Found library")
            if drawing.find('library').find('packages3d'):
                print("Found packages3d")
                package3ddata = drawing.find('library').find('packages3d')
                if package3ddata.find('package3d'):
                            print("Found Package3d data") 
                            if package3ddata.find('package3d').findall('description'):
                                   print("Found description")
                                   for package in root.iter('package'):
                                           print(package.attrib)
                                           desc = package.find('description').text
                                           print(desc,type(desc))
                                           Packagecheckdata = desc.split(",")[0].split(" ")[0] #Getting the package recheck from the json file 
                                           print("Package data:",desc.split(",")[0].split(" ")[0]) #Getting the package data
                                           try: 
                                               print("Start extracting the config file")
                                               print(listconfig) #Getting file listconfig
                                               data = open(CONFIG+"/"+listconfig[0],'r') #Open the file from the listconfig file 
                                               datas = data.readline()
                                               transfer = json.loads(datas)
                                               print(transfer)
                                               packageout = transfer.get("package").get("rootpackages")
                                               print(packageout)
                                               for rik in range(0,len(packageout)):
                                                       print("Package checking......")
                                                       decryptionext = desc.split(",")[0].split(" ")[0].split("-")[1] #Extracting the description extraction 
                                                       checkingintersec = intersection(packageout[rik],desc.split(",")[0].split(" ")[0].split("-")[1])
                                                       print(checkingintersec,packageout[rik],decryptionext) #Checking the library packageout on the intersection process 
                                                       percent=difflib.SequenceMatcher(None,packageout[rik],decryptionext)
                                                       print(percent.ratio()*100)
                                                       if percent.ratio()*100 == 100:
                                                             for package in root.iter('package3d'):
                                                                    print(package.attrib)  
                                                             if drawing.find('library').find('symbols'):
                                                                   print("Found symbols")
                                                                   print(drawing.find('library').find('symbols'))
                                                                   for pin in drawing.find('library').find('symbols').iter('pin'):
                                                                            print(pin.attrib)
                                                                            pin.set('name','testing')  #Getting the data index input from the pdf extraction 
                                                                            
                                                                   #print(root.tag) #tag is the start item in the xml file 
                                                                   show(root)
                                                             tree.write('/home/kornbotdev/Automaticsoftware/output2.xml')
                                                                            
                                                             break       
                                           except:
                                               print("Not found configfile in the config search directory")
                                           print(desc.split(","))
                                           
                            
                            
#tree.write('/home/kornbotdev/Automaticsoftware/output.xml')
