import json
from hermes.io import read_json, write_json
from hermes.paths import NEWS

output_path = "_data/items.json"
with open(output_path, "w") as f:
    json.dump(read_json(NEWS), f, indent=2)
