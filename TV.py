class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0   # constant
        self.VOLUME_MAXIMUM = 10  # constant
        self.volume = self.VOLUME_MAXIMUM // 2  # Initialize volume to half of maximum

    def power(self):
        self.isOn = not self.isOn  # Toggle TV power

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # Unmute sound when changing volume
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return None
        if self.isMuted:
            self.isMuted = False  # Unmute sound when changing volume
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex >= self.nChannels:
            self.channelIndex = 0  # Wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1  # Wrap around to the last channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print('TV Status:')
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')
