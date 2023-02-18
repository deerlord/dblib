data = (
        ("npk", npkdata),
        ("schedule", schedule),
        ("items", item),
        ("gpscoords", gpscoords)
    )
for name, model in data:
    filename = f"./migrations/data/{name}.csv"
    gen = _csv_data(filename)
    op.bulk_insert(model, list(gen))