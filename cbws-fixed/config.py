import sys
import subprocess

try:
    import websocket
except ImportError:
    subprocess.check_call([sys.executable,'-m','pip','install','websocket-client'])