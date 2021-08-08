class dataLine:
    def __init__(self, ID, timestamp, text, userName, status):
        self._id = ID
        self._timestamp = timestamp
        self._text = text
        self._userName = userName
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def text(self):
        return self._text
    
    @property
    def userName(self):
        return self._userName

    @property
    def status(self):
        return self._status
