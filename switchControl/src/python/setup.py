from distutils.core import setup

setup(
    name = "SwitchControl",

    version = "0.0.1",

    author = "Thomas Heinemann",

    author_email = "data1701-e@web.de",

    packages = ["configuration", "gpioMock", "gpioWrapper", "switchControl", "."],

    description="SwitchControl server to control model railways with a Raspberry Pi.",

    install_requires = ["flask", "pyxdg", "pyyaml"]

)