class test(object):
    color = []
    def __init__(self):
        self.main(self)
        self.jumb(self)

    @staticmethod
    def main(self):
        print "1"
        print self.color
        self.idi()

    @staticmethod
    def jumb(self):
        print 'k'

    def idi(self):
        print 'l'

t = test()
t.idi()
