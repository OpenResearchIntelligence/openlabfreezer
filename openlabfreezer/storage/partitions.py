"""The partition class collects information about
storage components and usage in a generic way"""

import shutil
import platform
import os
import psutil


class Partition:
    def __init__(self):
        self.machine_id = "{}-{}-{}".format(platform.machine(),
                                            os.getlogin(),
                                            hash(platform.processor()))
        self.machine_id = hash(self.machine_id)
        self._number_partitions = None

    @property
    def number_partitions(self):
        """Uses psutil.disk_partitions to count the number of physical
        partitions available on the machine"""

        self._number_partitions = list(psutil.disk_partitions())

        return len(self._number_partitions)

    @property
    def size_partitions(self):
        disk_usage = []

        for p in psutil.disk_partitions():
            try:
                disk_usage.append({"partition": p,
                                   "size": shutil.disk_usage(p.mountpoint)})
            except PermissionError as e:
                disk_usage.append({"partition": p, "size": None})

        return disk_usage
