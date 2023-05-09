import unittest
from datetime import datetime
from ..engine.model import Engine


class MyTestCase(unittest.TestCase):

    def test_Capulet_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 3001
        last_service_mileage = 0
        self.assertEqual(Engine.CapuletEngine.needs_service(last_service_date, current_mileage, last_service_mileage))

    def test_WilloughbyEngine_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        self.assertEqual(
            Engine.WilloughbyEngine.needs_service(last_service_date, current_mileage, last_service_mileage))

    def test_SternmanEngine_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        self.assertEqual(Engine.SternmanEngine.needs_service(last_service_date, warning_light_is_on))


if __name__ == '__main__':
    unittest.main()
