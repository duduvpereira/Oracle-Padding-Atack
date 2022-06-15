import urllib2
import sys
import codecs
#import numpy as np

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                print "OK caralho"
                return True # good padding

            return False # bad padding

if __name__ == "__main__":

    #.encode("hex")

    plainText = list(range(64))
    cypherText = list(range(64))

    for i in range(64):
        plainText[i] = ("0xff"[2:])
        #print i, ":", plainText[i]

    for i in range(64):
        if i == 63:
            cypherText[i] = ("0x01"[2:])
        else:
            cypherText[i] = ("0xff"[2:])
        #print i, ":", cypherText[i]

    #cypheText[] = int("",16)
    #cypheText =  str(hex(cypherText))
    for i in range(256):
        cypherText[63] = (str(hex(i))[2:]).zfill(2)
        cypherTextSTR = ""
        for j in range(64):
            cypherTextSTR += cypherText[j]

        po = PaddingOracle()
        po.query(cypherTextSTR)       # Issue HTTP query with the given argument
        #print cypherTextSTR
        print i





    #print type(cypherText)
    #a = int("0x1a",16)
    #print hex(a)
    #print a

    #po = PaddingOracle()
    #po.query()       # Issue HTTP query with the given argument
