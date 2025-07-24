# Bridge Configuration Handler
import yaml

def load_config(path="bridgeconfig.yml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
