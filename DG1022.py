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
        os.write(self.f, "FREQ %.3f" % freq)

    def sinusoid(self):
        os.write(self.f, "APPL:SIN")

    def voltage(self, vpp):
        os.write(self.f, "VOLT %.2f" % vpp)

    def read(self, length=4000):
        return os.read(self.f, length)

    def write(self, cmd):
        os.write(self.f, cmd)
        

memtime = time.time()
def timestamp():
    global memtime
    print(str(datetime.datetime.now()))
    print("diff = %.2f s" % (time.time() - memtime))
    memtime = time.time()


f1 = 0.5 
f2 = 121
step = 0.01
pulse_time = 0.4
pause_time = 0.6
repetitions = 5
freq_change_time = 0.1
vpp = 20.0


def frequencies():
    f = f1
    while f < f2:
        yield f
        f += step
    yield f2

if __name__ == "__main__":

    print("It will take %f hours" % ((f2-f1) / step * repetitions * (pulse_time + pause_time) /3600))

    gen = DG1022('/dev/usbtmc0')
    gen.sinusoid()
    time.sleep(0.1)
    gen.voltage(vpp)
    time.sleep(0.1)


    timestamp()
    print("Beginning sweep")

    for f in frequencies():
        print("f = %.3f" % f)
        gen.frequency(f)
        time.sleep(freq_change_time)
        for i in range(5):
            timestamp()
            print("ON")
            gen.output(True)
            time.sleep(pulse_time)
            timestamp()
            print("OFF")
            gen.output(False)
            if i < 4:
                time.sleep(pause_time)
            else:
                time.sleep(pause_time - freq_change_time)

    timestamp()
    print("Sweep terminated")
