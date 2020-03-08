class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def ymd(cls, year, month, date):
        cls.date = date
        cls.month = month
        cls.year = year
        return cls(cls.date, cls.month, cls.year)


d1 = Date(1, 1, 2020)
print(d1.year)

d2 = Date.ymd(2019, 2, 2)
print(d2.year)
