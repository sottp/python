class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__premute = self.__volume
        pass
    pass

    def power(self):
        if self.__status:
            self.__status = False
            pass
        else:
            self.__status = True
            pass
        pass
    pass

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                pass
            else:
                self.__muted = True
            pass
        pass
    pass

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                pass
            else:
                self.__channel = Television.MIN_CHANNEL
                pass
            pass
        pass
    pass

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                pass
            else:
                self.__channel = Television.MAX_CHANNEL
                pass
            pass
        pass
    pass

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                pass
            pass
        pass

    def volume_down(self):
        pass

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        pass
    pass
