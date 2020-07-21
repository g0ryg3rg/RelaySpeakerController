import RPi.GPIO as GPIO

#
# This class is used to control pairs of speakers by switching pairs 
#  of relays on a sainsmart 16 relay module. The relay module is 
#  controlled by a Raspberry Pi Zero using GPIO.
#
#       Speakers <---- Relay Module <---- RPi
#
#  Call the change_spaker_state function to turn on and off different
#  speaker zones.
#
class SpeakerController(object):
        # Each element in RELAY_PIN_MAP represents the pin (broadcom numbering) which the correspond relay is connected
        #  i.e. RELAY_PIN_MAP[0] is the pin that the relay 0 is mapped to on the raspberry pi
        RELAY_PIN_MAP = [2, 3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10, 9, 25, 11, 8]

        def __init__(self):
                print("INIT OBJ")
                # initialize GPIO mapping for relays
                GPIO.setmode(GPIO.BCM) #broadcom pin numbering
                for relay in self.RELAY_PIN_MAP:
                        GPIO.setup(relay, GPIO.OUT)
                        GPIO.output(relay, GPIO.HIGH)
                        #default set to HIGH as relay board is active low


        #
        # This function takes zone and value and sets the corresponding pair
        #  of relays on the sainsmart relay module
        #
        # zone (input): an integer from 1 to 8 that represents a pair of relays
        # value (input): the state to set to the relay pair. 0 means relays on
        #                and 1 means relays off
        # return value is True if sucessfully change the zone's state otherwise
        # otherwise returns False
        #
        def change_zone_state(self, zone, value):
                if zone > 8 or zone < 0 or value > 1 or value < 0:
                        print("Invalid zone or value selected")
                        print("Zone ", zone, " Value " , value)
                        return False
                relay1 = zone * 2
                relay2 = relay1 + 1
                # value 1 -> GPIO Low  -> relay pair on
                # value 0 -> GPIO high -> relay pair off
                gpio_state = GPIO.HIGH
                if value == 1:
                        gpio_state = GPIO.LOW


                GPIO.output(self.RELAY_PIN_MAP[relay1], gpio_state)
                GPIO.output(self.RELAY_PIN_MAP[relay2], gpio_state)

                print("Turning", end = ' ')
                if value == 1:
                        print("on", end = ' '),
                else:
                        print("off", end = ' '),

                print("Zone ", zone + 1)

                return True