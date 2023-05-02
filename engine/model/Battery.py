
class Battery:
    def needs_service(self):
        self.needs_service()


class SpindlerBattery:
    def needs_service(self, last_service_date, current_date):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < current_date:
            return True
        else:
            return False


class NubbinBattery:
    def needs_service(self, last_service_date, current_date):
         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
         if service_threshold_date < current_date:
             return True
         else:
             return False