"""Catalog periods: one catalog label may cover one or more academic years."""
# A catalog may be published for more than one academic year: Cal Poly prints '2026-2028 Catalog' / '2026-2028 Edition'
# (shared reader request #153). The label is kept exactly as printed (catalog_year '2026-2028'); the record's
# academic_year is the year of the period it is read for (academic_year_of). Periods of one or two years are read.
PERIOD_SPANS = (1, 2)


def academic_year_of(label, today=None):
    """Academic year a record read from a catalog labelled `label` ('2026-2027', '2026-2028') belongs to: a one-year label
    gives its own year; a multi-year period gives the current academic year when it falls inside the period (`today`
    '2026-27', or the date: July starts a year), otherwise the period's first year. The label itself is never changed."""
    y1, y2 = int(label[:4]), int(label[5:9])
    if y2 - y1 <= 1: return f'{y1}-{str(y1 + 1)[2:]}'
    if today: cur = int(today[:4])
    else:
        import datetime
        d = datetime.date.today(); cur = d.year if d.month >= 7 else d.year - 1
    start = cur if y1 <= cur < y2 else y1
    return f'{start}-{str(start + 1)[2:]}'
