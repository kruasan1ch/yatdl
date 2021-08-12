class dataLine:
    def __init__(self, userId, userName, task):
        self._userData = {"id": userId, "name": userName}
        self._task = task

    @property
    def _userData(self):
        return self._userData

    @property
    def _task(self):
        return self._task
