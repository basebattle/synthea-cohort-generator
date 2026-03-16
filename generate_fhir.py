import os
import json
import uuid
import random
from datetime import datetime, timedelta

folders = {
    'oncology': 'generator/output/oncology',
    'high_risk_readmission': 'generator/output/high_risk_readmission',
    'hospital_at_home': 'generator/output/hospital_at_home'
}

for fold, path in folders.items():
    os.makedirs(path, exist_ok=True)
    
    for i in range(20):
        # Generate dummy FHIR R4 Bundle
        patient_id = str(uuid.uuid4())
        bundle = {
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {
                    "resource": {
                        "resourceType": "Patient",
                        "id": patient_id,
                        "gender": random.choice(["male", "female"]),
                        "birthDate": (datetime.now() - timedelta(days=random.randint(40*365, 80*365))).strftime("%Y-%m-%d")
                    }
                }
            ]
        }
        
        with open(os.path.join(path, f"{patient_id}.json"), "w") as f:
            json.dump(bundle, f, indent=2)
            
print("Generated 60 mock FHIR bundles")
