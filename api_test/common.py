from dataclasses import asdict, is_dataclass
import json
import os

def formatted_json(data:any):
    return json.dumps(data,indent=4, ensure_ascii=False)


def to_json(data):
    if is_dataclass(data):
        data = asdict(data)    
    return json.dumps(data, indent=4)

def save_dict_as_json(data:dict, location:str) -> None:
    json_str = to_json(data)
    save_json(json_str=json_str, location=location)

def save_json(json_str:str, location:str)->None:
    os.makedirs(os.path.dirname(location), exist_ok=True)

    # Write the JSON string to the file
    with open(location, 'w', encoding='utf-8') as f:
        f.write(json_str)
        print(f"JSON saved to {location}")    

    