# Named Entity Recognition (NER) postprocessing

This script is designed to correct unintended text modifications that occur during the Named Entity Recognition (NER) process following the TEI (Text Encoding Initiative) standard. It primarily addresses issues like unintended text duplications introduced by the NER tool.

## Problem Example

An example of an unintended modification that this script corrects is:

**Before Correction:**
```xml
(...) Seminar der Univer<lb break="no" facs="#facs_290_r33"/>sität</orgName>sität</cell>
```

**After Correction:**
```xml
(...) Seminar der Univer<lb break="no" facs="#facs_290_r33"/>sität</orgName></cell>
```

## How it Works
- The NER process checks the documents and detects errors. Documents with errors are saved in an /error folder. 
- The script takes these NER-processed files (referred to as the "edited files") and the corresponding original files.
- It extracts all TEI entities from the edited files (\<placeName>, \<persName>, \<orgName>) and their surrounding context.
- It then merges these entities into the original files (the files prior to NER processing) using a context-aware search-and-replace method. This ensures that the corrections are made in the correct context, preserving the integrity of the original document.
- After processing, the script validates the output files by comparing them to the original and NER-processed documents. It checks for content integrity, ensuring that all unintended modifications made by the NER tool have been corrected and that the content remains consistent with the original files. Validation results, including any discrepancies found, are logged and presented in the statistics.csv file.
- Additionally, the script generates diff files that highlight the differences between the NER-processed and postprocessed files. This allows users to review the specific changes made during the postprocessing, facilitating a more transparent review of the corrections applied.

## Input Format

The notebook accepts XML files with a `.xml` extension as input.

## Output

The corrected XML files are saved in a specified output directory.

## Validation
This script is designed to process a large number of documents, making automated validation essential, as manual checks on such a scale would be impractical. 
The following checks are implemented:
- **Content integrity**: Is the content of the postprocessed file the same as the original file?
  - It can detect: Missing/too much text and words, missing whitespaces
  - It can not detect: Too much whitespaces
  - Possible Values: Yes/No
  - If Yes: All errors (unintendend modifications by the NER) have been corrected and the content of the document has not been changed compared to the original document
- **Missing entities**: This check compares the number of identified entities (\<placeName>, \<persName>, \<orgName>) in the postprocessed file against the NER-processed file (before postprocessing).
  - It can detect: A reduction in the number of marked entities, indicating losses during the postprocessing.
  - It cannot detect: Entities that are present but incorrectly placed.
  - Possible Values: >= 0 (Number of missing entities)
  - If >0 : Not all entities could be retained from the NER-processed file.
- **XML Validation**: Does the postprocessed XML conform to the TEI schema?
  - It can detect: Structure errors, missing required elements, and incorrect nesting of tags.
  - It cannot detect: Logical errors related to content semantics.
  - Possible Values: Valid/Invalid.
  - If Valid: The postprocessed XML file adheres to the TEI standards and is structurally sound.
- **Generation of Diff Files**: Comparison files are created that highlight the differences between the postprocessed file and the NER-processed (before postprocessing) file to facilitate manual review.
  - The diff files are stored by default in the "diffs" folder.
  
Validation results are presented in the statistics.csv.

## Requirements

To run this notebook, you need to have the following Python packages installed:

- `beautifulsoup4`
- `lxml`
- `xmlschema`

## Installation Instructions

To install the required packages, run the following command in your command line:

```bash
pip install beautifulsoup4 lxml xmlschema
```

## How to Start the Jupyter Notebook

1. **Install Jupyter Notebook**: If you haven't already installed Jupyter Notebook, you can do so by running:
   ```bash
   pip install notebook
   ```

2. **Launch Jupyter Notebook**: Open your command line or terminal and navigate to the directory where the notebook is located. Then, run:
   ```bash
   jupyter notebook
   ```

3. **Open the Notebook**: A new tab will open in your web browser showing the Jupyter Notebook interface. Click on the notebook file (`Postprocessing_NER.ipynb`) to open it.

4. **Adjust the Configurations**: Modify the configuration parameters in the script to align with your specific setup. Please refer to the "Configuration Options" section below for detailed information on how to customize these settings.

5. **Install the required packages**: Install the required packages as described above.

6. **Run the Notebook**: Follow the instructions in the notebook to execute the cells.


## Configuration Options

The script provides several configuration parameters to customize the processing of your documents. Below are the available configuration options that you can adjust in the code:

### 1. Directory Paths

```python
edited_dir = 'test_data/TEI-XML_NER/error/Amtsblatt/'  # Directory containing NER-processed files with errors
original_dir = 'test_data/TEI-XML/Amtsblatt/'          # Directory containing the original files
output_dir = 'test_data/postprocessed/'                # Output directory for the merged files generated by this script
output_dir_diff_files = 'diffs'                        # Output directory for the diff files
```

- **edited_dir**: Set this to the directory where the NER-processed files with errors are stored.
- **original_dir**: Specify the path to the directory containing the original XML files.
- **output_dir**: This is the directory where the corrected and merged XML files will be saved after processing.
- **output_dir_diff_files**: Define the path for storing the generated diff files that highlight the differences between the postprocessed file and the NER-processed (before postprocessing) file.

### 2. XML Validation

```python
XML_VALIDATION_ACTIV = True
```

- **XML_VALIDATION_ACTIV**: Set this option to `True` to enable validation of the postprocessed XML files against the TEI schema. Note that enabling this option may increase processing time significantly.


## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Authors
- [Roman Siegenthaler](https://github.com/sigiro)
- [Rebekka Plüss](https://github.com/rebplu) (code auditor)
