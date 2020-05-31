
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


class _MoistureSensor:
        def __init(self):
            spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
            cs = digitalio.DigitalInOut(board.D5)
            mcp = MCP.MCP3008(spi, cs)
            self.channel = AnalogIn(mcp, MCP.P0)


class MoistureSensor:

    def __init__(self):
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D5)
        mcp = MCP.MCP3008(spi, cs)
        self.channel = AnalogIn(mcp, MCP.P0)

    def probe(self):
        print('Raw ADC Value: ', self.channel.value)
        print('ADC Voltage: ' + str(self.channel.voltage) + 'V')