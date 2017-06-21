from abc import ABCMeta, abstractmethod

class Display(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class CurrentConditionDisplay(Display):
    def update(self, temperature, humidity, pressure):
        print('curren condition: {}, {}, {}'.format(temperature, humidity, pressure))

class StatisticsDisplay(Display):
    def update(self, temperature, humidity, pressure):
        print('statistics: {}, {}, {}'.format(temperature, humidity, pressure))

class ForecastDisplay(Display):
    def update(self, temperature, humidity, pressure):
        print('Forecast: {}, {}, {}'.format(temperature, humidity, pressure))

class Data(object):
    def __init__(self):
        self.displays = []
    def notify(self):
        for display in self.displays:
            display.update(self.get_temperature(), self.get_humidity(), self.get_pressure())
    def get_temperature(self):
        raise NotImplementedError
    def get_humidity(self):
        raise NotImplementedError
    def get_pressure(self):
        raise NotImplementedError

class AsiaWeatherData(Data):
    def __init__(self):
        Data.__init__(self)
    def get_temperature(self):
        return 'asia_t'
    def get_humidity(self):
        return 'asia_h'
    def get_pressure(self):
        return 'asia_p'

class USWeatherData(Data):
    def __init__(self):
        Data.__init__(self)
    def get_temperature(self):
        return 'us_t'
    def get_humidity(self):
        return 'us_h'
    def get_pressure(self):
        return 'us_p'

def main():
    asia_data = AsiaWeatherData()
    asia_data.displays.append(CurrentConditionDisplay())
    asia_data.displays.append(StatisticsDisplay())
    asia_data.displays.append(ForecastDisplay())
    asia_data.notify()  # one method gets all updated data, and show in all displays

if __name__ == '__main__':
    main()
    