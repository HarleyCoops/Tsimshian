import json
import os

# Define the input and output file paths relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(script_dir, "Shm'algyacktoEnglish.jsonl")
output_filename = os.path.join(script_dir, "groundtruth_output.jsonl")

print(f"Input file: {input_filename}")
print(f"Output file: {output_filename}")

try:
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:

        line_number = 0
        processed_count = 0
        error_count = 0

        for line in infile:
            line_number += 1
            try:
                # Strip whitespace and parse the JSON object
                line = line.strip()
                if not line: # Skip empty lines
                    continue

                data = json.loads(line)

                # Extract the required fields
                use_text = data.get("Use")
                translation_text = data.get("Translation")

                # Check if both fields exist
                if use_text is not None and translation_text is not None:
                    # Create the new structure
                    new_data = {
                        "shmalgyack": use_text,
                        "english": translation_text
                    }
                    # Write the new JSON object to the output file as a line
                    outfile.write(json.dumps(new_data, ensure_ascii=False) + '\n')
                    processed_count += 1
                else:
                    print(f"Warning: Missing 'use' or 'translation' key on line {line_number}. Skipping.")
                    error_count += 1

            except json.JSONDecodeError:
                print(f"Error: Invalid JSON on line {line_number}. Skipping.")
                error_count += 1
            except Exception as e:
                print(f"Error processing line {line_number}: {e}. Skipping.")
                error_count += 1

    print(f"\nProcessing complete.")
    print(f"Successfully processed lines: {processed_count}")
    print(f"Skipped lines due to errors or missing keys: {error_count}")

except FileNotFoundError:
    print(f"Error: Input file not found at {input_filename}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
