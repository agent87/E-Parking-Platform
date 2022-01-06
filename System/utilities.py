


def time_str(time_int):
    #recieve time in seconds int
    if time_int < 60:
        return f'0 Minutes'

    else:
        intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),)
        result = []
        granularity=1
        for name, count in intervals:
            value = round(time_int // count)
            if value:
                time_int -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return f'{result[0]}'