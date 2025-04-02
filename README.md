t # Tsimshian Dictionary Project

This project contains tools and data for processing and converting Tsimshian (Shm'algyack) dictionary content between various formats.

## Files

- `parse_dictionary.py`: Script to parse Shm'algyack dictionary from markdown to JSONL format
- `processPDF.py`: Script to process PDF dictionary files
- `Shm'algyacktoEnglish.md`: Markdown version of the Shm'algyack to English dictionary
- `Shm'algyacktoEnglish.jsonl`: JSONL version of the Shm'algyack to English dictionary
- `EnglishtoShm'algyack.jsonl`: JSONL version of the English to Shm'algyack dictionary
- `TsimshianDictionary.tex`: LaTeX version of the Tsimshian dictionary
- `TsimshianDictionary.md`: Markdown version of the Tsimshian dictionary

## Usage

To convert the Shm'algyack to English dictionary from markdown to JSONL format:

```
python parse_dictionary.py
```

## Future Development

The current dictionary parsing implementation has several limitations that could be addressed in future updates:

1. **Improved Example Parsing**: The current parsing of example usage and translation is simplistic, assuming they're separated by periods. A more robust parser would handle various punctuation patterns and formatting styles.

2. **Multiple Examples Support**: Currently, only the first example usage is captured for each entry. Future versions should support multiple examples per dictionary entry.

3. **Enhanced Part of Speech Extraction**: The regex for extracting part of speech and definition might not handle all cases correctly. A more comprehensive approach would better handle edge cases and variations in formatting.

4. **Bidirectional Conversion**: Add support for converting from JSONL back to markdown or other formats.

5. **Validation and Error Handling**: Implement validation for the parsed entries and better error handling for malformed input.

6. **Interactive Editing Interface**: Develop a web-based interface for viewing and editing dictionary entries.

7. **Pronunciation Support**: Add fields for pronunciation guides and audio recordings.
