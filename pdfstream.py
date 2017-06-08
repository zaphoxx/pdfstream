#!/usr/bin/python3
# row row row your boat gently down the stream ... merrily merrily merrily merrily life is but a dream

__author__  = 'zaphoxx'
__email__   = 'zaphoxx@gmail.com'
__url__     = ''
__git__     = 'http://github.com/zaphoxx/pdfstream.git'
__twitter__ = ''
__version__ = '0.1a'
__license__ = ''
__banner__  = "# pdfstream - {} - {} - {}".format(__version__,__author__, __git__)
__description__ ="row row row your boat gently down the stream ... merrily merrily merrily merrily life is but a dream"

import zlib
import sys
import argparse

gVerbose=False

def verb(msg):
    if gVerbose:
        print("[+] {}".format(msg));

def initParser():
    print("[+] init parser.")
    parser=argparse.ArgumentParser()
    parser.add_argument("-in",dest="fileIn",required=True,help="input file with encoded text or text to encode")
    parser.add_argument("-out",dest="fileOut",required=True,help="output file")
    parser.add_argument("-encode",dest="encode",action="store_true",default=False,required=False,help="default is to decode the content of the input file")
    parser.add_argument("-v",dest="verbose",action="store_true",default=False,required=False,help="turn verbose mode on/off")
    parser.set_defaults(verbose=False,encode=False)
    args=parser.parse_args()
    return args

# import data from input file and save in buffer
def importBuffer(fileIn,encodeData):
    print("[+] import data from input file '{}'.".format(fileIn))
    buffer=b''
    # read data from input file and save to buffer
    try:
        with open(fileIn,'rb') as fin:
            buffer=fin.read()
    except Exception as e0:
        verb("\n[ERROR reading input file] {}".format(e0))

    # check if data needs to be decompressed or compressed according to commandline arguments    
    if not encodeData:
        print("[+] decompress input data.")
        try:
            bDecoded=zlib.decompress(buffer)
            buffer=bDecoded
        except Exception as e1:
            verb("\n[ERROR decompress] {}".format(e1))
    else:
        print("[+] compress input data.")
        try:
            bEncoded=zlib.compress(buffer)
            buffer=bEncoded
        except Exception as e2:
            verb("\n[ERROR compress] {}".format(e2))

    return buffer

# save buffer content to output file
def exportBuffer(fileOut,buffer,encodeData):
    # check if encode/decode and set necessary values accordingly for saving to fileOut
    print("[+] export data to output file '{}'.".format(fileOut))
    fileAccess=''
    if encodeData:
        fileAccess='wb'
        wBuffer=buffer
    else:
        fileAccess='w'
        wBuffer=str(buffer)
        
    with open(fileOut,fileAccess) as fout:
        try:
            fout.write(wBuffer)
        except Exception as e3:
            verb("\n[ERROR write buffer to file] {}".format(e3))

def main():
    global gVerbose
    print(__banner__)
    encodeData=False
    args=initParser()
    gVerbose=args.verbose
    encodeData=args.encode
    buffer=importBuffer(args.fileIn,encodeData)
    verb("\n[+] --- DATA ---")
    verb(str(buffer))
    verb("\n[+] ------------")
    exportBuffer(args.fileOut,buffer,encodeData)

if __name__=="__main__":
    main()
