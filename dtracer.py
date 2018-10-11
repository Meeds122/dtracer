# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:10:08 2018

@author: Tristan

DEVELOPMENT NOTES:
    I want to try to keep all of the work in a single file. This is supposed to be a "simple" script :D

dtracer:
    a document tracing and attribution solution. Keeps a central registry
        In generate mode:
    will assign a registry unique ID to a paper, insert required encoding,
    and return a copy of that data. 
        In attribution mode:
    will reverse generate the id and do a table lookup in a specified registry
    to attribute the paper to somebody
    
Quick Summary: this program will allow you to attribute the release of a document
                to an individual or group.

Command Line Use Examples:
    dtracer --registry reg.csv --generate --document file.txt --attribution JohnDoe123MainSt --output dtraced_file.txt
    dtracer --registry reg.csv --finger --document dtraced_file.txt 

TODO:
    document encoding and decoding methods in a Encoding() class
        NOTE - The only reason I'm putting these in a class is for extensibility and namespace resolution issues
    document typing, reading, writing, in Document() class
    command line functionality in the mainCmd() function
    GUI functionality in the mainGUI() function --> GUI() class
    implement GUI() class 

Would be nice:
    more document formats
    optional sql integration w/ user defined fields
    method selection based on config file to doc type
    
Modus Operandi:
    Depending on the document type, a series of filters will be applied including:
        make small font size changes to periods, commas, etc.
        an encoded number of UTF8/Unicode/ASCII encoded "do nothing" bytes will be inserted.
        an encoded number of UTF8/Unicode characters will be switched with visually similar but diffrent characters
        an encoded hash will be set in any metadata sections availiable. 
        an encoded hash will be set in binary slack space
        and more... some methods listed here may not be implemented yet. Look at line XXX to see what's implemented
"""

class Document(object):
    def __init__(self, work_mode=None, read_from_name=None, write_to_name=None):
        """
        Document.__init__(work_mode, read_from_name, write_to_name)
        
        don't be lazy you fuck. set ALL of the init vars for proper function ima chech foo
        """
        #sanity checks
        if read_from_name == None or write_to_name == None or work_mode == None:
            raise Exception("You fool! READ THE DOCS REEEE")
        self.text = None
        self.encoded_text = None
        self.read_name = read_from_name
        self.write_name = write_to_name
        self.file_type = self.getFileType()
        #sanity checks and running requested operations. This is the BRAIN of Document()
        self.mode = work_mode
        if self.mode == "generate":
            #do generating things
            self.generate()
        elif self.mode == "finger":
            #finger the leaky bastard
            self.finger()
        else:
            raise Exception("You fool! READ THE DOCS REEEE")
        return
    def getFileType(self, file_name=None):
        """
        Document.getFiletype(file_name):
            file_name defaults to self.read_name if not set. This is for non-object calls if needed
            Algorithmicly determines file type using exif, extention, and other analysis techniques*.
            [* May not be implemented correctly] [* Case sensitive RN FIX PLS! :D]
            returns a 3 letter string corrosponding to the document type as follows:
                unk - unknown type
                txt - text document
        """
        if file_name == None:
            file_name = self.read_name
        #quick garbage test to detect test documents for the POC shell
        if file_name[-3:] == "txt":
            return "txt"
        return "unk"
    def readDocument(self):
        """
        self.readDocument()
        reads self.read_name into self.text
        will throw TypeError Exception if type is unk
        """
        if self.file_type == "unk":
            raise TypeError("Unknown File Type!") 
        elif self.file_type == "txt":
            with open(self.read_name) as file:
                self.text = file.read()
            #auto closes self.read_name
        else:
            raise TypeError("Unable to read this type of file!")
        return
    def generate(self):
        """
        self.generate()
        calls Encoding.encode(text, file_type)
        Encoding.encode will determine the proper 
        """
        self.encoded_text = Encoding.encode(self.text, self.file_type)
        return
    def finger(self):
        self.text = Encoding.finger(self.encoded_text, self.file_type)
        return

class Encoding():
    def encode(text, file_type, ID):
        """
        Encoding.encode(text, file_type)
        returns a copy of the file encoded with ID 
        """
        return "Not yet implemented :("
    def finger(text, file_type):
        """
        Encoding.finger(text, file_type) returns the calculated ID of the document
        """








































        