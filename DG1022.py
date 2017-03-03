import os

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
        os.write(self.f, "FREQ %.3f" % freq)

    def sinusoid(self):
        os.write(self.f, "APPL:SIN")

    def voltage(self, vpp):
        os.write(self.f, "VOLT %.2f" % vpp)

    def read(self, length=4000):
        return os.read(self.f, length)

    def write(self, cmd):
        os.write(self.f, cmd)
