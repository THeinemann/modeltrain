from distutils.core import setup
import setuptools

setup(
    name = "SwitchControl",

    version = "0.0.1",

    author = "Thomas Heinemann",

    author_email = "heinemann.thomas@arcor.de",

    packages = setuptools.find_packages('.'),

    description="SwitchControl server to control model railways with a Raspberry Pi.",

    install_requires = ["flask", "pyxdg", "pyyaml", "pyserial"]

)
