import argparse

from .main import BME280

parser = argparse.ArgumentParser(description='BME280 sensor communication module.')
parser.add_argument('-b', '--bus', dest='spi_bus', action='store',
                    type=int, default=0, help='spi bus (default: 0)')
parser.add_argument('-d', '--dev', dest='spi_dev', action='store',
                    type=int, default=0, help='spi device (default: 0)')
args = parser.parse_args()
device = BME280(args.spi_bus, args.spi_dev)
print(f"""Temperature: {device.temperature}
Humidity: {device.humidity}
Pressure: {device.pressure}""")
