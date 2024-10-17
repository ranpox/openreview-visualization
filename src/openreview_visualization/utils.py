import orjson


def save_json(data, filename):
    with open(filename, "wb") as f:
        f.write(orjson.dumps(data))


def save_jsonl(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write(orjson.dumps(item) + "\n")
