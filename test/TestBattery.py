
import unittest
from datetime import datetime
from ..engine import Battery


class MyTestCase(unittest.TestCase):

  def test_Spindler_battery_should_be_serviced(self):
       current_date = datetime.date
       last_service_date = datetime.today().replace(year = datetime.today.year - 3)
       self.assertEqual(Battery.SpindlerBattery.needs_service(current_date, last_service_date))

  def test_Nubbin_battery_should_be_serviced(self):
      current_date = datetime.date
      last_service_date = datetime.today().replace(year=datetime.today.year - 5)
      self.assertEqual(Battery.NubbinBattery.needs_service(current_date, last_service_date))


if __name__ == '__main__':
    unittest.main()
