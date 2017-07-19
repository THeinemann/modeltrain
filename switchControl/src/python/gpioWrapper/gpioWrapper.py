import sys
try:
    import RPi.GPIO as _GPIO
except ModuleNotFoundError:
    sys.stdout.write("Could not import RPi.GPIO - Will continue with GPIO Mock.\n")
    sys.stdout.write("If you are running this program on a Raspberry Pi, this is probably not what you want.\n")
    sys.stdout.write("The GPIO pins will not actually be changed, i.e. connected devices are not controlled.\n")
    from gpioMock import GPIO as _GPIO


class GpioWrapper:
    def __init__(self, gpio):
        self.gpio = gpio
        self.channels = set()

    def setup(self, channel, direction, initial=None):
        self.gpio.setup(channel, direction, initial=initial)
        self.channels.add(channel)

    def output(self, channel, state):
        if channel not in self.channels:
            self.setup(channel, self.OUT, initial=state)
        else:
            self.gpio.output(channel, state)

    def cleanup(self, channel=None):
        self.gpio.cleanup(channel)
        if channel is None:
            self.channels = set()
        else:
            try:
                self.channels -= channel
            except TypeError:
                self.channels.remove(channel)

    def __getattr__(self, item):
        return getattr(self.gpio, item)

GPIO = GpioWrapper(_GPIO)