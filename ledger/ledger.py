from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = date
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)


def header(loc):
    if loc == "en_US":
        return "Date       | Description               | Change       "
    return "Datum      | Omschrijving              | Verandering  "


def get_date(entry, loc):
    if loc == "en_US":
        return entry.date.strftime("%m/%d/%Y")
    return entry.date.strftime("%d-%m-%Y")


def get_description(entry):
    return f"{entry.description if len(entry.description) <= 25 else entry.description[0:22] + '...': <25}"


def get_amount(entry, currency, loc):
    amount = f"{abs(entry.change / 100):,.2f}"
    symbol = "$" if currency == "USD" else "€"
    if loc == "en_US":
        return f"{'(' if entry.change < 0 else ''}{symbol}{amount}{')' if entry.change < 0 else ' '}".rjust(13)
    else:
        amount = amount.replace(".", "_").replace(",", ".").replace("_", ",")
        return f"{symbol} {'-' if entry.change < 0 else ''}{amount} ".rjust(13)


def format_entries(currency, loc, entries):
    out = [header(loc)]
    entries.sort(key=lambda item: (item.date, item.change))
    for entry in entries:
        date = get_date(entry, loc)
        description = get_description(entry)
        amount = get_amount(entry, currency, loc)
        out.append(" | ".join([date, description, amount]))
    return "\n".join(out)
