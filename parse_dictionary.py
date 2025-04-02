import re
import json

def parse_dictionary(input_file, output_file):
    """
    Parse the Shm'algyack to English dictionary from markdown format to JSONL.
    
    Args:
        input_file (str): Path to the input markdown file
        output_file (str): Path to the output JSONL file
    """
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content by section to get individual entries
    # The pattern matches \section*{word} which marks the start of each entry
    entries = re.split(r'\\section\*\{([^}]+)\}', content)
    
    # Remove the first element which is text before the first section
    entries = entries[1:]
    
    # Process entries in pairs (word and its content)
    results = []
    for i in range(0, len(entries), 2):
        if i+1 < len(entries):
            word = entries[i].strip()
            content = entries[i+1].strip()
            
            # Parse the entry
            entry_data = parse_entry(word, content)
            if entry_data:
                results.append(entry_data)
    
    # Write to JSONL file
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in results:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"Processed {len(results)} entries and saved to {output_file}")

def parse_entry(word, content):
    """
    Parse a single dictionary entry.
    
    Args:
        word (str): The Shm'algyack word
        content (str): The content of the entry
    
    Returns:
        dict: A dictionary with the parsed data
    """
    lines = content.split('\\\\')
    if not lines:
        return None
    
    # First line typically contains part of speech and definition
    first_line = lines[0].strip()
    
    # Extract part of speech and definition
    pos_def_match = re.match(r'^(noun|verb|adverb|adjective|interjection|conjunction|prefix|particle|number|phrase|pronoun|preposition|interrogative|vocative)(;?\s*[^-]*)', first_line, re.IGNORECASE)
    
    if pos_def_match:
        part_of_speech = pos_def_match.group(1).strip()
        definition = pos_def_match.group(2).strip()
        # Remove leading semicolon if present
        if definition.startswith(';'):
            definition = definition[1:].strip()
    else:
        # If no match, try to extract from the first line
        parts = first_line.split(' ', 1)
        if len(parts) > 1:
            part_of_speech = parts[0].strip()
            definition = parts[1].strip()
        else:
            part_of_speech = ""
            definition = first_line
    
    # Look for example usage lines (starting with -)
    usage_examples = []
    for line in lines[1:]:
        line = line.strip()
        if line.startswith('-'):
            # Remove the leading dash
            example = line[1:].strip()
            usage_examples.append(example)
    
    # Create the entry dictionary
    entry = {
        "shmalgyack": word,
        "part_of_speech": part_of_speech,
        "definition": definition,
    }
    
    # Add usage example and translation if available
    if usage_examples:
        # Split the first example into Shm'algyack usage and English translation
        # The pattern is typically: Shm'algyack sentence. English translation.
        example = usage_examples[0]
        parts = example.split('.')
        
        if len(parts) >= 2:
            # First part is the usage in Shm'algyack
            entry["Use"] = parts[0].strip()
            # Second part onwards is the translation
            entry["Translation"] = '.'.join(parts[1:]).strip()
        else:
            # If we can't split by period, try to find another pattern
            # Some entries might use different separators
            entry["Use"] = example
            entry["Translation"] = ""
    else:
        entry["Use"] = ""
        entry["Translation"] = ""
    
    return entry

if __name__ == "__main__":
    input_file = "Shm'algyacktoEnglish.md"
    output_file = "Shm'algyacktoEnglish.jsonl"
    parse_dictionary(input_file, output_file)
