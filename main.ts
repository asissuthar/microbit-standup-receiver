radio.onReceivedNumber(function (receivedNumber) {
    signal = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    near = Math.constrain(Math.map(signal, -90, -50, 0, 100), 0, 100)
    if (near <= 45) {
        if (goFar) {
            music.playTone(659, music.beat(BeatFraction.Whole))
            basic.clearScreen()
            goFar = false
        } else {
            counter = 0
        }
    } else if (near >= 80) {
        if (counter == 600) {
            music.playTone(988, music.beat(BeatFraction.Whole))
            basic.showIcon(IconNames.StickFigure)
            goFar = true
            counter = 0
        } else if (!(goFar)) {
            counter += 1
        }
    }
})
let goFar = false
let near = 0
let signal = 0
let counter = 0
led.setBrightness(20)
radio.setGroup(1)
counter = 0
