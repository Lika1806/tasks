class ItemWithRates:

    def __init__(self) -> None:
        super().__init__()
        self._total_rating = None
        self._rates_total = 0
        self._rating_count = 0

    def add_rate(self,value):
        self._rates_total+=value
        self._rating_count+=1
        self._total_rating = self._rates_total / self._rating_count
    @property
    def rating(self):
        if self._total_rating is None:
            return 10
        return self._total_rating

class Rater:
    def rate(self, product, value):
        product.add_rate(value)