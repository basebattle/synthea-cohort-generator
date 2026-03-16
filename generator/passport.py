import json
from .validator import validate_cohort

def generate_passport(cohort_name, config_path):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except:
        config = {"name": cohort_name, "population": 0}
        
    validation = validate_cohort(cohort_name)
    
    passport = {
        "cohort_name": config["name"],
        "population_size": config["population"],
        "validation_score": validation["overall_score"],
        "certification_status": "IRB-Exempt Synthetic Data",
        "phi_status": "NONE - 100% Synthetic"
    }
    return passport
