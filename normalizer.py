import json


def min_max_normalize(data):
    min_val = min(data.values())
    max_val = max(data.values())
    normalized_data = {k: (v - min_val) / (max_val - min_val) for k, v in data.items()}
    return normalized_data

if __name__ == "__main__":
    with open('data/importance.json', 'r') as f:
        importance_data = json.load(f)

    importance_data_normalized = min_max_normalize(importance_data)

    with open('data/importance.json', 'w') as f:
        json.dump(importance_data_normalized, f, indent=1)