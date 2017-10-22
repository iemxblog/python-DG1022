import os
import time

class DG1022:
    def __init__(self, device):
        self.device = device
        self.f = os.open(device, os.O_RDWR)

    def output(self, state):
        if state == True:
            self.write("OUTP ON")
        else:
            self.write("OUTP OFF")

    def frequency(self, freq):
        self.write("FREQ %.3f" % freq)

    def sinusoid(self):
        self.write("APPL:SIN")

    def voltage(self, vpp):
        self.write("VOLT %.3f" % vpp)

    def offset(self, o):
        self.write("VOLT:OFFS %.3f" % o)
    
    def pos_voltage(self, vpp):
        self.voltage(vpp)
        self.offset(vpp/2) 

    def read(self, length=4000):
        return os.read(self.f, length)

    def write(self, cmd):
        os.write(self.f, cmd)
        time.sleep(0.1)
