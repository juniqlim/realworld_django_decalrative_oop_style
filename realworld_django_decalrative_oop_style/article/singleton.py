class Singleton:
    _instance = {}

    def __new__(self, cls, *args, **kwargs):
        if cls.__name__ not in self._instance:
            self._instance[cls.__name__] = cls(*args)
        return self._instance[cls.__name__]

    @staticmethod
    def remove_all():
        Singleton._instance = {}