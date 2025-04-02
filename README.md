# Tsimshian Dictionary Project

This project contains tools and data for processing and converting Tsimshian (Shm'algyack) dictionary content between various formats. Shm'algyack is the language of the Tsimshian people, indigenous to the Pacific Northwest coast of North America, primarily in British Columbia, Canada and Alaska, USA.

The project aims to digitize, preserve, and make accessible the Shm'algyack language by converting dictionary resources between different formats (PDF, Markdown, LaTeX, JSONL) for linguistic research, language learning, and cultural preservation.

## Project Structure

### Core Files

- `parse_dictionary.py`: Script to parse Shm'algyack dictionary from markdown to JSONL format
- `processPDF.py`: Script to process PDF dictionary files and extract structured content
- `Shm'algyacktoEnglish.md`: Markdown version of the Shm'algyack to English dictionary
- `Shm'algyacktoEnglish.jsonl`: JSONL version of the Shm'algyack to English dictionary
- `EnglishtoShm'algyack.jsonl`: JSONL version of the English to Shm'algyack dictionary
- `TsimshianDictionary.tex`: LaTeX version of the Tsimshian dictionary
- `TsimshianDictionary.md`: Markdown version of the Tsimshian dictionary

### Source Dictionaries

The `Dictionaries/` directory contains source PDF files:
- `DawsonDictionaryCompress.pdf`: Compressed version of the Dawson Dictionary
- `TsimshianDictionary.pdf`: Original Tsimshian Dictionary PDF

## Data Structure

The JSONL format structures each dictionary entry as a JSON object with the following fields:

```json
{
  "shmalgyack": "aab",
  "part_of_speech": "noun",
  "definition": "my father",
  "Use": "Yagwa goom wunsh aabdu",
  "Translation": "My father is hunting for deer"
}
```

## Installation

No special installation is required beyond having Python 3.6+ installed. The scripts use standard libraries with the exception of:
- `re` for regular expression parsing
- `json` for JSON handling

## Usage

### Converting Markdown to JSONL

To convert the Shm'algyack to English dictionary from markdown to JSONL format:

```bash
python parse_dictionary.py
```

By default, this reads from `Shm'algyacktoEnglish.md` and outputs to `Shm'algyacktoEnglish.jsonl`.

### Processing PDF Dictionaries

To extract content from PDF dictionaries:

```bash
python processPDF.py
```

## Technical Implementation

The `parse_dictionary.py` script implements a parser that:

1. Reads the markdown file containing dictionary entries
2. Splits the content by section markers (`\section*{word}`)
3. For each entry:
   - Extracts the Shm'algyack word
   - Identifies part of speech and definition using regex patterns
   - Extracts usage examples and their translations
4. Outputs the structured data as JSONL (one JSON object per line)

## Future Development

The current dictionary parsing implementation has several limitations that could be addressed in future updates:

1. **Improved Example Parsing**: The current parsing of example usage and translation is simplistic, assuming they're separated by periods. A more robust parser would handle various punctuation patterns and formatting styles.

2. **Multiple Examples Support**: Currently, only the first example usage is captured for each entry. Future versions should support multiple examples per dictionary entry.

3. **Enhanced Part of Speech Extraction**: The regex for extracting part of speech and definition might not handle all cases correctly. A more comprehensive approach would better handle edge cases and variations in formatting.

4. **Bidirectional Conversion**: Add support for converting from JSONL back to markdown or other formats.

5. **Validation and Error Handling**: Implement validation for the parsed entries and better error handling for malformed input.

6. **Interactive Editing Interface**: Develop a web-based interface for viewing and editing dictionary entries.

7. **Pronunciation Support**: Add fields for pronunciation guides and audio recordings.

8. **Search Functionality**: Implement search capabilities across the dictionary entries.

9. **API Development**: Create a simple API to query the dictionary programmatically.

10. **Mobile Application**: Develop a mobile app for offline access to the dictionary.

## Contributing

Contributions to improve the Tsimshian Dictionary Project are welcome. Please consider:

1. Improving the parsing algorithms
2. Adding support for additional formats
3. Enhancing documentation
4. Reporting issues with the current implementation
5. Adding linguistic annotations or corrections

## Cultural Significance

This project recognizes the cultural importance of language preservation for indigenous communities. The Shm'algyack language is a vital part of Tsimshian cultural heritage, and this digital dictionary aims to support language revitalization efforts.

## License

This project is available under the MIT License. See the LICENSE file for more details.

## Acknowledgments

This project builds upon the work of linguists, Tsimshian language speakers, and community members who have contributed to documenting and preserving the Shm'algyack language.
