from pyspectator.processor import Cpu
from time import sleep

cpu = Cpu(monitoring_latency=1) # changed here
print(cpu.temperature)