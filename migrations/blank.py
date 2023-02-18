def _csv_data(filename: str) -> Iterator[dict]:
    with open(filename) as handle:
        reader = csv.reader(handle)
        header = next(reader)
        for row in reader:
            data = dict(zip(header, row))
            yield data


data = (
    ("npk", npkdata),
    ("schedule", schedule),
    ("items", items),
    ("gpscoords", gpscoords),
)
for name, model in data:
    filename = f"./migrations/data/{name}.csv"
    gen = _csv_data(filename)
    op.bulk_insert(model, list(gen))
