import unittest
import os
import platform
import sys
from openlabfreezer.storage.partitions import Partition


class TestOpenLabStorage(unittest.TestCase):
    def setUp(self):
        self.partitions = Partition()

    def test_machine_id(self):
        hashed_machine = "{}-{}-{}".format(platform.machine(), os.getlogin(),
                                           hash(platform.processor()))
        assert self.partitions.machine_id == hash(hashed_machine)

    def test_number_partitions(self):
        number_partitions = self.partitions.number_partitions
        # on my laptop to start with
        assert number_partitions == 3

    def test_size_partitions(self):
        size_partitions = self.partitions.size_partitions

        assert size_partitions[0]
        assert size_partitions[0]['size'].free > 100
