from microbit import *
import radio
import random

def get_serial_number(type=hex):
    NRF_FICR_BASE = 0x10000000
    DEVICEID_INDEX = 25  # deviceid[1]

    @micropython.asm_thumb
    def reg_read(r0):
        ldr(r0, [r0, 0])
    return type(reg_read(NRF_FICR_BASE + (DEVICEID_INDEX*4)))

display.show(Image.SKULL)
uuid = get_serial_number()
heart_beat = [Image.HEART, Image.HEART_SMALL]
radio.config(group=23)
radio.on()

def handshake(c_uuid):
    print("Sending c_uuid={0}".format(c_uuid))
    radio.send(c_uuid)
    sleep(100)
    r_uuid = radio.receive()
    print("Received r_uuid={0}".format(r_uuid))
    return r_uuid

c_uuid = "{0}".format(uuid)
r_uuid = None

while True:
    print('in main loop')

    while True:
        r_uuid = handshake(c_uuid)
        if(r_uuid == None):
            print('handshake was false')
            display.show(heart_beat, delay=800, wait=False, loop=True)
            sleep(random.randint(10000, 30000))
        else:
            print("r_uuid={0}".format(r_uuid))
            break

    display.show(heart_beat, delay=100, wait=False, loop=True)
    print("Out of handshake loop c_uuid={0} r_uuid={1}".format(c_uuid, r_uuid))

    if c_uuid != r_uuid:
        #received a different value than we sent, so start using that value and try the handshake again
        print("c_uuid={0} != r_uuid={1}".format(c_uuid, r_uuid))
        c_uuid = r_uuid
        display.show(Image.TARGET)
    else:
        #we sent and received the same value, so let's hold on to that one
        print("c_uuid==r_uuid {0} {1}".format(c_uuid, r_uuid))
        display.show(Image.YES)
        break

    #sleep(1000)

#now that we have settled on a uuid, let's save it as a potential contact
#also keep boadcasting it, but don't listen for others. This is now the master
print("Done")