import json
import os

def load_bundles(cohort_name):
    path = os.path.join(os.path.dirname(__file__), f"../../generator/output/{cohort_name}")
    bundles = []
    if os.path.exists(path):
        for f in os.listdir(path):
            if f.endswith('.json'):
                with open(os.path.join(path, f), 'r') as file:
                    bundles.append(json.load(file))
    return bundles
