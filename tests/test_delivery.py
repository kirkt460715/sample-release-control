"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        cartons = read_table("cartons.json")
        lots = {r["lot"] for r in read_table("lots.json")}
        self.assertTrue(all(set(r["candidates"]) <= lots for r in cartons))
        checks = read_table("checks.json")
        self.assertTrue(any(r["origin"] == "指定" and r["result"] == "关键" for r in checks))
        self.assertTrue(any(r["revision"] and not r["destructive"] for r in checks))
        self.assertTrue({r["carton"] for r in read_table("fulfillment.json")} <= {r["carton"] for r in cartons})
