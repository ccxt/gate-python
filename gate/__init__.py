import sys
import gate.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from gate.ccxt import gate as GateSync
from gate.ccxt.async_support.gate import gate as GateAsync
from gate.ccxt.pro.gate import gate as GateWs
