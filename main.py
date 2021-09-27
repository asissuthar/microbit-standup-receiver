def on_received_number(receivedNumber):
    global signal, near, goFar, counter
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    near = Math.constrain(Math.map(signal, -90, -50, 0, 100), 0, 100)
    if near <= 45:
        if goFar:
            music.play_tone(659, music.beat(BeatFraction.WHOLE))
            basic.clear_screen()
            goFar = False
        else:
            counter = 0
    elif near >= 80:
        if counter == 600:
            music.play_tone(988, music.beat(BeatFraction.WHOLE))
            basic.show_icon(IconNames.STICK_FIGURE)
            goFar = True
            counter = 0
        elif not (goFar):
            counter += 1
radio.on_received_number(on_received_number)

goFar = False
near = 0
signal = 0
counter = 0
led.set_brightness(20)
radio.set_group(1)
counter = 0