
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


class MoistureSensor:

    def __init__(self):
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D5)
        mcp = MCP.MCP3008(spi, cs)
        self.channel = AnalogIn(mcp, MCP.P0)

    def probe(self) -> tuple:
        raw_value = self.channel.value
        voltage = self.channel.voltage
        print('Raw ADC Value: ', raw_value)
        print('ADC Voltage: ' + str(voltage) + 'V')
        return raw_value, voltage