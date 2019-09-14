

class SectionControl:
    def __init__(self, gpio, section_dao):
        self.gpio = gpio
        self.section_dao = section_dao

    def register_section(self, pin):
        existing_section = self.section_dao.get_section_for_pin(pin)
        if existing_section is not None:
            raise RuntimeError("Pin {} already is registered as section {}".format(pin, existing_section))
        section = self.section_dao.insert_section(pin)
        self.gpio.setup(pin, self.gpio.OUT)
        self.gpio.output(pin, self.gpio.HIGH)
        return section

    def set_section(self, section, configuration):
        pin = self.section_dao.get_pin_for_section(section)
        if configuration["enabled"]:
            self.gpio.output(pin, self.gpio.LOW)
        else:
            self.gpio.output(pin, self.gpio.HIGH)

    def get_sections(self):
        return self.section_dao.get_all_sections()
