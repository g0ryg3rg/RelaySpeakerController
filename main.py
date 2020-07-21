import blynklib
from speakerController import SpeakerController

BLYNK_AUTH = '-8bzpjozCLL44vHkamtOCb3iC145GXlA'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

speaker_controller = SpeakerController()

# register handler for virtual pin write event
@blynk.handle_event('write V*')
def write_virtual_pin_handler(pin, value):
        speaker_controller.change_zone_state(pin,int(value[0]))

# infinite loop that waits for event
while True:
        blynk.run()