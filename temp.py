from distutils.command.build_scripts import first_line_re
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

    FirstCipher = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4".decode("hex")

    #print len(FirstCipher)
   
    cypherText = list(range(64))
    temp = list(range(64))


    for i in range(64):
        cypherText[i] = FirstCipher[i]
        #print cypherText[i].encode("hex")
        #cypherText[i] = cypherText[i].encode("hex")
    #print cypherText
    blockIndex = 3
    cipher = ""
    previousCipher = ""
    auxPadding = ""
    qualquer = ""
    letra = list(range(16))
    for i in range(16):
        letra[i] = (str(hex(0))[2:]).zfill(2)
        #print letra[i]

    for king in range(1, 4):

        for i in range((blockIndex-1)*16, (blockIndex*16)):
            previousCipher += cypherText[i]
        for i in range(blockIndex*16, (blockIndex+1)*16):
            cipher += cypherText[i]

        #print previousCipher.encode("hex")
        #print cipher.encode("hex")


        for f in range(1, 17):
            auxPadding = returnPadding(f)
            #print auxPadding

            for k in range(2, 256):
                #i_temp = str(i)
                #print i
                #print (str(hex(i))[2:]).zfill(2)                 
                #print letra
                #letra = (("0x000000000000000000000000000000" + (str(hex(k))[2:]).zfill(2))[2:])
                letra[16-f] =  (str(hex(k))[2:]).zfill(2)
                print letra
                auxLetra = ""
                for conc in range(16):
                    auxLetra = auxLetra + letra[conc]
                #print auxLetra
                #qualquer = >>(str(hex(k))[2:]).zfill(2))[2:])
                #print letra
                #print aux.encode("hex")
                #print auxPlainText
                #print len(letra)
                #print len(aux)
                #print len(auxPlainText)
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
        blockIndex = blockIndex -1


#print type(temp[i])
#print hex(temp[i])


#print "OK"

    #cypheText[] = int("",16)
    #cypheText =  str(hex(cypherText))
    #for i in range(256):
    #    cypherText[63] = (str(hex(i))[2:]).zfill(2)
    #    cypherTextSTR = ""
    #    for j in range(64):
    #        cypherTextSTR += cypherText[j]

    #    po = PaddingOracle()
    #    po.query(cypherTextSTR)       # Issue HTTP query with the given argument
        #print cypherTextSTR
        ##print i





    #print type(cypherText)
    #a = int("0x1a",16)
    #print hex(a)
    #print a

    #po = PaddingOracle()
    #po.query()       # Issue HTTP query with the given argument
