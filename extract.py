import json


def extract_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract relevant keys from each dictionary
    extracted_data = []
    for entry in data:
        extracted_entry = {
            "id": entry.get("id", ""),
            "date_start": entry.get("date_start", ""),
            "event_title": entry.get("event_title", ""),
            "event_type": entry.get("event_type", ""),
            "description": entry.get("description", "")
        }
        extracted_data.append(extracted_entry)

    # Write the extracted data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(extracted_data, f, indent=2)


# Example usage
input_json_file = 'events.json'
output_json_file = 'ai_input.json'

extract_data(input_json_file, output_json_file)
