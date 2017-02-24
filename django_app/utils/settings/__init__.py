import json

from pathlib import Path


def get_config():
    root_path = Path(__file__).parents[3]
    conf_file = Path(root_path).joinpath('.conf', 'settings_local.json')
    config = json.loads(conf_file.open().read())
    return config
