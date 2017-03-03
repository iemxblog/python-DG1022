from DG1022 import DG1022
import time
import datetime


class Timestamp:
    def __init__(self):
        self.memtime = time.time()

    def display(self):
        print(str(datetime.datetime.now()))
        print("diff = %.2f s" % (time.time() - self.memtime))
        self.memtime = time.time()
  
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

print("It will take %f hours" % ((f2-f1) / step * repetitions * (pulse_time + pause_time) /3600))

gen = DG1022('/dev/usbtmc0')
timestamp = Timestamp()
gen.sinusoid()
time.sleep(0.1)
gen.voltage(vpp)
time.sleep(0.1)


timestamp.display()
print("Beginning sweep")

for f in frequencies():
    print("f = %.3f" % f)
    gen.frequency(f)
    time.sleep(freq_change_time)
    for i in range(5):
        timestamp.display()
        print("ON")
        gen.output(True)
        time.sleep(pulse_time)
        timestamp.display()
        print("OFF")
        gen.output(False)
        if i < 4:
            time.sleep(pause_time)
        else:
            time.sleep(pause_time - freq_change_time)

timestamp.display()
print("Sweep terminated")
