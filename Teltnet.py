import telnetlib

class Telnet:
   def __init__(self,host,port):
       self.tn = telnetlib.Telnet(host,port)

   def read(self):
        return self.tn.read_until(b\"n")
   def write(self,data):
      def close(self):
     self.tn.close()