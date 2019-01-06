import hashlib
import random

    
def sha512(text):
    text = bytearray(text, 'utf-8')
    return hashlib.sha512(text).hexdigest()

# Init--> Ledger, content,mine,
class blockchain:
    def __init__(self, content):
        self.chains = []
        self.ledger = 0
        self.content = content
        self.journal = [self.ledger, self.content]
        self.current = sha512(str(self.journal))
        self.journal.append( self.current )

        self.chains.append( self.journal )
        
    def issue(self, content):
        self.content = content
        self.ledger += 1
        self.journal = [self.ledger, self.content, self.current]
        self.current = sha512(str(self.journal))
        self.journal.append( self.current )
        self.chains.append( self.journal )

    def export(self):
        for block in self.chains:
            fd = open('blocks/'+str(block[0]), 'w')
            data = fd.write(str(block))
            fd.close()

b = blockchain('Author:')
for i in range(100):
    b.issue('Novice Wrote This Program')

b.export()
