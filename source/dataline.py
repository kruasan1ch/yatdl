class dataLine:
    def __init__(self, ID, timestamp, text, userId, status):
        self._id = ID
        self._timestamp = timestamp
        self._text = text
        self._userId = userId
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
    def userId(self):
        return self._userId

    @property
    def status(self):
        return self._status
