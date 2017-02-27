import os
import time
import datetime

class DG1022:
    def __init__(self, device):
        self.device = device
        self.f = os.open('/dev/usbtmc0', os.O_RDWR)

    def output(self, state):
        if state == True:
            os.write(self.f, "OUTP ON")
        else:
            os.write(self.f, "OUTP OFF")

    def frequency(self, freq):
        os.write(self.f, "FREQ %f" % freq)

    def sinusoid(self):
        os.write(self.f, "APPL:SIN")

    def read(self, length=4000):
        return os.read(self.f, length)

    def write(self, cmd):
        os.write(self.f, cmd)
        


gen = DG1022('/dev/usbtmc0')
gen.sinusoid()
time.sleep(0.1)
gen.frequency(1234)
time.sleep(0.1)

print(str(datetime.datetime.now()))
for i in range(10):
    gen.output(True)
    time.sleep(0.5)
    gen.output(False)
    time.sleep(0.5)

print(str(datetime.datetime.now()))

cmd = ""
while cmd != "exit":
    cmd = raw_input("> ")
    gen.write(cmd)
    time.sleep(1)
    print("...")
    print(gen.read())

