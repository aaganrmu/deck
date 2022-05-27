from datetime import datetime
import subprocess
import time
from oled_manager import oled_manager
from system_stats import system_stats

def main():
    oled_thread = oled_manager()
    oled_thread.start()
    stats = system_stats()

    try:
        while True:
            oled_thread.items = stats.stats()
    except KeyboardInterrupt:
        oled_thread.running = False

if __name__ == "__main__":
    main()

