from twisted.internet import protocol, reactor
import json

#f = open("C:\\titles.txt", 'w')
f = open("titles.txt", 'a')

class Write(protocol.Protocol):
    def dataReceived(self, data):
        data = data[data.index("{"):]
        writeData = json.loads(data)
        print("Writing: "+writeData['titletag'])
        f.write(writeData['titletag']+"\n")
        self.transport.write(data)      

class WriteFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Write()

reactor.listenTCP(1234, WriteFactory())
reactor.run()
