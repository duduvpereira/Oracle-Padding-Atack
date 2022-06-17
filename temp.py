from distutils.command.build_scripts import first_line_re
import urllib2
import sys
import codecs
import time
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
                print "OK"
                return True # good padding

            return False # bad padding

def strxor(a, b, c = None):
	if c:
		return strxor(strxor(a, b), c)
	assert len(a) == len(b)
	return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

#def usxor(a, b, c = None):
#    return 
def returnPadding(index):
    auxPlainText = ""
    for i in range(0,16):
        if i >= (16 - index):
            #print "ENTROU"
            auxPlainText = (auxPlainText + (str(hex(index))[2:]).zfill(2))
        else:
            auxPlainText += ("0x00"[2:])
    #print auxPlainText
    return auxPlainText



if __name__ == "__main__":
    start_time = time.time()
    FirstCipher = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4".decode("hex")

    #print len(FirstCipher)
   
    cypherText = list(range(64))
    temp = list(range(64))


    for i in range(64):
        cypherText[i] = FirstCipher[i]
        
    blockIndex = 3
    cipher = ""
    previousCipher = ""
    auxPadding = ""
    salvo = ""
    letra = list(range(16))
    for i in range(16):
        letra[i] = (str(hex(0))[2:]).zfill(2)
        #print letra[i]

    for king in range(1, 4):
        cipher = ""
        previousCipher = ""
        auxPadding = ""
        for i in range((blockIndex-1)*16, (blockIndex*16)):
            previousCipher += cypherText[i]
        for i in range(blockIndex*16, (blockIndex+1)*16):
            cipher += cypherText[i]

        for f in range(1, 17):
            auxPadding = returnPadding(f)
            #print auxPadding

            for k in range(2, 256):
                letra[16-f] =  (str(hex(k))[2:]).zfill(2)
                print letra
                auxLetra = ""
                for conc in range(16):
                    auxLetra = auxLetra + letra[conc]

                temp = strxor(previousCipher, auxPadding.decode("hex"), auxLetra.decode("hex"))
                #print temp.encode("hex")

                temp = temp + cipher
                #print temp.encode("hex")
                po = PaddingOracle()
                #ok = po.query(temp.encode("hex"))
                if po.query(temp.encode("hex")):
                    letra[16-f] = (str(hex(k))[2:]).zfill(2)      # Issue HTTP query with the given argument
                    #print letra[f]
                    break
        auxLetra = ""
        for conc2 in range(16):
            auxLetra = auxLetra + letra[conc2]
        salvo = auxLetra + salvo
        print salvo
        blockIndex = blockIndex -1
    print("--- %s seconds ---" % (time.time() - start_time))
