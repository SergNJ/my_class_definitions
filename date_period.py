class Period:
    def __init__(self, year: str, month: str):
        self.__year = year
        self.__month = month
        self.__comparable_date = date(int(year), int(month), 15)

    def __repr__(self):
        return f'{self.year}_{self.__month}'

    def __eq__(self, other):
        return self.__comparable_date == other.__comparable_date

    def __lt__(self, other):
        return self.__comparable_date < other.__comparable_date

    def __gt__(self, other):
        return self.__comparable_date > other.__comparable_date

    def __le__(self, other):
        return self.__comparable_date <= other.__comparable_date

    def __ge__(self, other):
        return self.__comparable_date >= other.__comparable_date

    @property
    def year(self) -> str:
        return self.__year

    @property
    def month(self) -> str:
        return self.__month

    @property
    def comparable_date(self) -> str:
        return self.__comparable_date

    def reset(self, year: str, month: str):
        self.__init__(year, month)

    def shift(self, delta_years=0, delta_months=0):
        start_date = date(int(self.__year), int(self.__month), 15)
        end_date = start_date + relativedelta(years=delta_years, months=delta_months)
        return Period(str(end_date.year), str(end_date.month))

    def get_periods_string(self, howmany, offset):
        p = []
        for i in range(offset, howmany + offset):
            p.append(str(Period(self.__year, self.__month).shift(0, i)))
        return p