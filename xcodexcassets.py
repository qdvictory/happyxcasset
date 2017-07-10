#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: qdvictory
# date: 2017-07-08
# version: 1.0

import sys, getopt, os, shutil, json
try: input = raw_input
except NameError: pass

helpStr = "\nWelcome to Happyxcasset\n\
This version has been tested in Xcode8 and supports both python2 and python3\n\
To prevent unknown bugs, please back up your data before using it\n\
Use commands easy to understand\n\
python xcodexcassets.py -i <inputdir> -o <outputdir> -e <fileextension>\n\
-i The resource's input directory can contain subfolders\n\
-o The output directory of the resource, which is the directory of the .xcasset in Xcode\n\
-e File extension. Default 'png,jpg,jpeg,pdf'\n\
-h Help\n\
This is all, enjoy.\n"

class FileModel:
   path = ''
   fileFinder = ''
   fileName = ''
   fileFinder = ''
   singleName = ''
   extension = ''

   def __init__(self, path):
      self.path = path
      self.fileFinder,self.fileName=os.path.split(path)
      self.finderName = self.fileFinder.split('/')[-1].split(".")[0]
      self.extension = self.fileName.split('.')[1]
      self.singleName = self.fileName.split('.')[0].replace('@1x','').replace("@2x",'').replace("@3x",'')

   def __str__(self):
      return "singleName:%s, finder:%s"%(self.singleName,self.fileFinder)

   def __repr__(self):
      return "singleName:%s, finder:%s"%(self.singleName,self.fileFinder)

def walkDir(rootDir,key='finderName',extension=[]):
   allFiles = {}
   list_dirs = os.walk(rootDir) 
   for root, dirs, files in list_dirs: 
     # for d in dirs: 
     #     print os.path.join(root, d)      
     for f in files: 
         filePath = os.path.join(root, f)
         m = FileModel(filePath)
         if len(m.singleName) == 0 or not (m.extension.lower() in extension):
            continue
         k = getattr(m, key)
         if k in list(allFiles.keys()):
            allFiles[k].append({k:m})
         else:
            allFiles[k] = [{k:m}]
   return allFiles

#replace file
#If the old file already exists, delete the file except for Contents.json
#new Contents.json and files insert
def replaceFileModel(inputModel,outputModel):
   #clean old finder
   outputPath = None
   contentPath = None
   if type(outputModel) != str:
      for d in outputModel:
         m = d[list(d.keys())[0]]
         outputPath = ("/").join(m.fileFinder.split("/")[:-1])
         if m.fileName != "Contents.json":
            os.remove(m.path)
         else:
            contentPath = m.path
   else:
      outputPath = outputModel

   jsondic = None

   if contentPath != None:
      file_object = open(contentPath)
      try:
         file_context = file_object.read()
         jsondic = json.loads(file_context)
      finally:
         file_object.close()
      

   if jsondic == None:
      jsondic = {"images":[
         {"idiom" : "universal", "scale":"1x"},
         {"idiom" : "universal", "scale":"2x"},
         {"idiom" : "universal", "scale":"3x"},
      ],
      "info":{"version":1,"author":"xcode"}
      }

   for d in inputModel:
      nm = d[list(d.keys())[0]]
      alreadyinsert = False
      for key in ["@1x.","@2x.","@3x."]:
         if key in nm.fileName:
            for sdic in jsondic["images"]:
               if sdic["scale"] == key[1:3]:
                  sdic["filename"] = nm.fileName
                  alreadyinsert = True
      if not alreadyinsert:
         for sdic in jsondic["images"]:
            if "scale" in list(sdic.keys()) and sdic["scale"] == "1x":
                  sdic["filename"] = nm.fileName
                  alreadyinsert = True
      if not alreadyinsert:
         for sdic in jsondic["images"]:
            sdic["filename"] = nm.fileName
            alreadyinsert = True

      finderPath = outputPath+"/"+nm.singleName+".imageset/"
      if not os.path.exists(finderPath):
         os.mkdir(finderPath)
      shutil.copy2(nm.path, finderPath)
      if contentPath == None:
         contentPath = finderPath+"Contents.json"

   content = json.dumps(jsondic,indent=4)
   file_object = open(contentPath,"w")
   try:
      file_object.write(content)
   finally: 
      file_object.close

   print(">>> "+finderPath+" output is complete")


#    {
#   "images" : [
#     {
#       "idiom" : "universal",
#       "filename" : "message_btn_download.pdf",
#       "scale" : "1x"
#     },
#     {
#       "idiom" : "universal",
#       "scale" : "2x"
#     },
#     {
#       "idiom" : "universal",
#       "scale" : "3x"
#     }
#   ],
#   "info" : {
#     "version" : 1,
#     "author" : "xcode"
#   }
# }



def main(argv):
   inputfinder = ''
   outputfinder = ''
   extensionname = ['png', 'jpg', 'pdf', 'jpeg',"json"]
   try:
      opts, args = getopt.getopt(argv,"hi:o:e:",["inputfinder=","outfinder=","extension="])
   except getopt.GetoptError:
      print (helpStr)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print (helpStr)
         sys.exit()
      elif opt in ("-i", "--inputfinder"):
         inputfinder = arg
      elif opt in ("-o", "--outputfinder"):
         outputfinder = arg
      elif opt in ("-e", "--extension"):
         extensionname = arg.split(",")

   if len(inputfinder) == 0 or len(outputfinder) == 0 or len(extensionname)==0:
      print (helpStr)
      sys.exit(2)

   extensionname.append("json")

   if not "xcassets" in outputfinder:
      print ("\n\nPlease enter the directory for xcassets in xcode correctly.\nlike \"/Users/Desktop/project/projectname/Image.xcassets\"")
      sys.exit(2)

   while (True):
      confirm = input("\n>>> This script will output all the files %s in the directory\n\
   (%s)\n\
   to the target directory\n\
   (%s)\n\
   and adapt to the xcode. \n\
   Before this, please back up the file in advance to prevent the file from being lost. \n\
   Please confirm the operation (y / n) "%(str(extensionname),inputfinder,outputfinder))
      
      if confirm.lower() == 'y':
         break;
      elif confirm.lower() == 'n':
         sys.exit(2)         

   outputFiles = walkDir(outputfinder,extension=extensionname)
   inputFiles = walkDir(inputfinder,'singleName',extensionname)
   for k in list(inputFiles.keys()):
      d = inputFiles[k]
      if k in list(outputFiles.keys()):
         replaceFileModel(d,outputFiles[k])
      else:
         replaceFileModel(d, outputfinder)

if __name__ == "__main__":
   main(sys.argv[1:])