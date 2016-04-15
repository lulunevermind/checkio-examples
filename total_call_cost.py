from datetime import datetime
from collections import Counter
from math import ceil
from itertools import groupby


def total_cost(calls):
    total = 0
    price_1_pm = 1
    price_2_pm = 2
    date_objects = []
    for call in calls:
        how_long = call.split()[-1]
        how_long_in_minutes = ceil(int(how_long)/60)
        data = ' '.join(call.split()[:-1])
        date_object = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        clear_date = date_object.date()
        date_objects.append((clear_date, how_long_in_minutes))
    for i, groups in groupby(date_objects, key=lambda x: x[0].day):
        quote = 0
        max_quote = 100
        for date, how_long in groups:
            quote += how_long
        total += quote*price_1_pm if quote < 100 else max_quote*price_1_pm + (quote-max_quote)*price_2_pm
    return total


if __name__ == '__main__':
    print(total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert total_cost(("2014-01-01 01:12:13 181",
    #                    "2014-01-02 20:11:10 600",
    #                    "2014-01-03 01:12:13 6009",
    #                    "2014-01-03 12:13:55 200")) == 124, "Base example"
    # assert total_cost(("2014-02-05 01:00:00 1",
    #                    "2014-02-05 02:00:00 1",
    #                    "2014-02-05 03:00:00 1",
    #                    "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    # assert total_cost(("2014-02-05 01:00:00 60",
    #                    "2014-02-05 02:00:00 60",
    #                    "2014-02-05 03:00:00 60",
    #                    "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
