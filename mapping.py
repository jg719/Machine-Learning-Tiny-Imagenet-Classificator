def load_mapping(fname):
    with open(fname, mode="r") as f:
        folder_to_class = json.load(f)
