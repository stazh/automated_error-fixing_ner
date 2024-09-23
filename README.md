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

## Input Format

The notebook accepts XML files with a `.xml` extension as input.

## Output

The corrected XML files are saved in a specified output directory.

## Requirements

To run this notebook, you need to have the following Python packages installed:

- `beautifulsoup4`
- `lxml`

## Installation Instructions

To install the required packages, run the following commands in your command line:

```bash
pip install beautifulsoup4
pip install lxml
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

4. **Adjust the Paths**: Update the path variables in the script to match the locations of your edited NER files, original XML files, and desired output directory.

5. **Install the required packages**: Install the required packages as described above.

6. **Run the Notebook**: Follow the instructions in the notebook to execute the cells.

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Authors
- [Roman Siegenthaler](https://github.com/sigiro)
- [Rebekka Plüss](https://github.com/rebplu) (code auditor)
