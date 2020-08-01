from xdg import BaseDirectory

defaults = {
    'database': "{}/{}".format(BaseDirectory.xdg_data_home, "modeltrains.db"),
    'arduino_port': "/dev/ttyACM0"
}
