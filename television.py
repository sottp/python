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

    def power(self):
        """
        used to turn off and on the tv
        """
        if self.__status:
            self.__status = False
            pass
        else:
            self.__status = True
            pass
        pass

    def mute(self):
        """
        used to mute and unmute the tv while it is powered on
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                pass
            else:
                self.__muted = True
            pass
        pass

    def channel_up(self):
        """
        used to increase the tv channel value while the tv is powered on
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                pass
            else:
                self.__channel = Television.MIN_CHANNEL
                pass
            pass
        pass

    def channel_down(self):
        """
        used to decrease the tv channel value while the tv is powered on
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                pass
            else:
                self.__channel = Television.MAX_CHANNEL
                pass
            pass
        pass

    def volume_up(self):
        """
        used to increase the tv volume while the tv is powered on
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                pass
            pass
        pass

    def volume_down(self):
        """
        used to decrease the tv volume while it is powered on
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                pass
            pass
        pass

    def __str__(self):
        """
        used to show the tv status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        pass
