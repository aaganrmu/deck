from display import display
from datetime import datetime
import subprocess

BAR_STEPS = 10


class display_stats(display):

    def run_in_shell(self, cmd):
        result_bytes = subprocess.check_output(cmd, shell=True)
        result_string = result_bytes.decode('utf-8')
        return result_string

    def make_bar_nice(self, name, value, maximum=1):
        ratio = value / maximum
        bar_full = int(ratio * BAR_STEPS)
        bar_empty = BAR_STEPS - bar_full
        bar_string = "[" + "=" * bar_full + " " * bar_empty + "]"
        percentage_string = str(int(100 * ratio)) + "%"
        full_string = f'{name: <5}{bar_string} {percentage_string: >3}'
        return full_string

    def stat_time(self):
        timestring = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return timestring

    def stat_cpu(self):
        raw_idle = self.run_in_shell("top -bn1 | grep Cpu | awk '{print $(NF-9)}'")
        idle_percent = float(raw_idle)
        usage = 1 - idle_percent / 100
        cpu_string = self.make_bar_nice("CPU", usage)
        return cpu_string

    def stat_mem(self):
        raw_mem = self.run_in_shell("top -bn1 | grep 'MiB Mem' | awk '{print $(NF-3), $(NF-7)}'")
        values = raw_mem.split()
        mem_usage = float(values[0])
        mem_max = float(values[1])
        mem_string = self.make_bar_nice("MEM", mem_usage, mem_max)
        return mem_string

    def stat_disk(self):
        raw_disk = self.run_in_shell("df -h | grep root | awk '{print $(NF-3), $(NF-2)}'")
        values = raw_disk.split()
        disk_usage = float(values[0][:-1])
        disk_max = float(values[1][:-1])
        disk_string = self.make_bar_nice("DISK", disk_usage, disk_max)
        return disk_string

    def stat_ip(self):
        raw_ip = self.run_in_shell("hostname -I | cut -d\' \' -f1")
        ip_string = f'IP   {raw_ip}'
        return ip_string

    def stat_temp(self):
        raw_temp = self.run_in_shell("vcgencmd measure_temp")
        temp = raw_temp[5:5 + 4]
        raw_throttled = self.run_in_shell("vcgencmd get_throttled")
        throttled = "".join(raw_throttled.split())[10:]
        if (throttled == '0x0'):
            throttled_description = 'ok'
        else:
            throttled_description = throttled
        temp_string = f'Temp {temp}°C ({throttled_description})'
        return temp_string

    def get_text(self):
        items = [
                 self.stat_time(),
                 self.stat_cpu(),
                 self.stat_mem(),
                 self.stat_disk(),
                 self.stat_ip(),
                 self.stat_temp()
                 ]
        return items
