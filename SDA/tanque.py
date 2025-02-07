import math
from threading import Thread
from opcua import Client
from timer import LoopTimer
from time import sleep

y1 = 1.2
y2 = 1.4
y3 = 1.6
r0 = 1.0
r1 = 2.0

max_height = 5.0
alpha = (r1-r0)/max_height
T = 0.1

class TanqueConico(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.h1 = 0.0
        self.h2 = 0.0
        self.h3 = 0.0

    def run(self):
        clientOPC = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer")

        clientOPC.connect()

        node1 = clientOPC.get_node("ns=3;i=1008")
        node2 = clientOPC.get_node("ns=3;i=1009")
        node3 = clientOPC.get_node("ns=3;i=1010")
        node4 = clientOPC.get_node("ns=3;i=1011")
        node5 = clientOPC.get_node("ns=3;i=1012")
        node6 = clientOPC.get_node("ns=3;i=1013")

        qin1 = node2
        qin2 = node4
        qin3 = node6

        def tank1_behavior():
                self.h = (qin1.get_value()-y1*math.sqrt(self.h1)-qin2.get_value())/(math.pi*(r1+alpha*self.h1)**2)
                print("Altura do líquido do tanque 1: ", self.h1)
                self.qin1_ = y1*math.sqrt(self.h1);
                node1.set_value(self.h1) 
                node2.set_value(self.qin1_)
        def tank2_behavior():
                self.h = (qin2.get_value()-y2*math.sqrt(self.h2)-qin3.get_value())/(math.pi*(r1+alpha*self.h2)**2)
                print("Altura do líquido do tanque 2: ", self.h2)
                self.qin2_ = y2*math.sqrt(self.h2);
                node3.set_value(self.h2)
                node4.set_value(self.qin2_)
        def tank3_behavior():
                self.h = (qin3.get_value()-y3*math.sqrt(self.h3))/(math.pi*(r1+alpha*self.h3)**2)
                print("Altura do líquido do tanque 3: ", self.h3)
                self.qin3_ = y3*math.sqrt(self.h3);
                node5.set_value(self.h3)
                node6.set_value(self.qin3_)

        timer = LoopTimer(0.1, tank1_behavior)
        timer.start()
        timer2 = LoopTimer(0.1, tank2_behavior)
        timer2.start()
        timer3 = LoopTimer(0.1, tank3_behavior)
        timer3.start()

        sleep(120)

        timer.cancel()

        clientOPC.disconnect()