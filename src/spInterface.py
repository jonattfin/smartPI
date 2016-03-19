import spidev

class SpInterface(object):
    """ The SP Interface class provide access to the sensors on the Serial Peripheral Interface (SPI)"""

    def __init__(self):
        """ prepare the SPI for reading """
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)

    def readADC(self, position):
        """ reads the position pin from the SPI interface """
        if ((position > 7) or (position < 0)):
            return -1
        r = self.spi.xfer2([1,(8+position)<<4,0])
        adcout = ((r[1]&3) << 8) + r[2]
        return adcout
