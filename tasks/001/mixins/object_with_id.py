class ObjectWithID():
    _id_counter = 1
    def __init__(self) -> None:
        super().__init__()
        self._id = self._count_id()

    @classmethod
    def _count_id(cls, other_class=None):
        if other_class:
            cls = other_class
        id_ = cls._id_counter
        cls._id_counter+=1
        return id_
    

    @property
    def item_id(self):
        return self._id