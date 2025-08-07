# MorphoMatrix

An interactive English language morphological analyzer.

MorphoMatrix provides a simple graphical user interface (GUI) for analyzing and parsing English words into their constituent morphemes. It identifies prefixes, root words, and suffixes, and then displays their meanings, grammatical types, and a simple tree diagram to illustrate the word's structure. This tool assists in understanding the internal makeup of words — a fundamental concept in linguistics.

---

## 🌟 Features

- *GUI Input* – Enter English words via a user-friendly Tkinter interface  
- *Morpheme Analysis* – Breaks the word into *prefix, **root, and **suffix*  
- *Meaning & Type Display* – Shows meaning and grammatical type (inflectional / derivational) of each morpheme  
- *Visual Representation* – Displays a text-based morpheme tree diagram  
- *File Saving* – Save complete analysis and morpheme tree to a .txt file  
- *Clear Function* – Refresh all fields for new analysis  
- *Help Menu* – Integrated help for user guidance  

---

## 📚 What is Morphology?

*Morphology* is the study of the internal structure of words and how the smallest meaningful 
units (called *morphemes*) combine to form new words. This program focuses on two key types of 
morphemes in English:

| Type of Morpheme       | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| *Inflectional*       | Adjusts grammatical category (e.g., -s, -ed) without changing word class |
| *Derivational*       | Forms new words or parts of speech (e.g., un-, -ness)                    |

---

## ⚙ Dependencies

- Python *3.6+*
- NLTK – Natural Language Toolkit  
  - Data packages required:
    - wordnet
    - omw-1.4
    - averaged_perceptron_tagger
    - punkt
- Tkinter (usually ships with Python)

---

## 📦 Installation & Usage

### 1. Clone the repository and change the directory.

  ```bash
  git clone https://github.com/Yash6012/MorphoMatrix.git
  cd MorphoMatrix/gui
  ```

### 2. Install NLTK and its data packages.

  ```bash
  pip install nltk
  python -m nltk.downloader wordnet omw-1.4 averaged_perceptron_tagger punkt
  ```

### 3. Run the script
  ```bash
  python morphmatrix_gui.py
  ```

### 4. Enter a word in the input box and click Analyze to see the morphological breakdown.

### 5. Use the Refresh button to clear the fields or the File menu to Save the output or Exit the program.


## Streamlit file:

  `https://morphomatrix-a6yehmny6nxthogahxbvh9.streamlit.app/`

## 📝 Notes

- The program uses WordNet to help verify if a substring is a valid root word, 
which enhances the accuracy of its analysis.

- The focus of this tool is on prefix and suffix morphology. It does not currently 
handle infixes or other more complex morphological processes.

- The morpheme tree is a simple text-based diagram for conceptual visualization, 
not a detailed linguistic tree structure.

## 📌 Key Points
This is a deterministic, rule-based, dictionary-verified 
affix analyzer — ideal for educational use or lightweight NLP tasks.

| Feature | Description |
| :--- | :--- |
| **Analysis Method** | Rule-based, deterministic affix stripping |
| **Expected Accuracy** | ~75–90% (depends on rule and dictionary coverage) |
| **Intended Use** | Classroom learning, NLP experiments |
| **Not Suitable For** | Advanced, production-grade linguistics pipelines |

