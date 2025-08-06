import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary NLTK data once, then comment these out after first run
import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary NLTK data once, then comment these out after first run
try:
    nltk.data.find('corpora/wordnet')
    nltk.data.find('corpora/omw-1.4')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:  # Change here from nltk.downloader.DownloadError to LookupError
    st.info("Downloading necessary NLTK data. This might take a moment...")
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('averaged_perceptron_tagger')




# Affix dictionaries with meanings
prefixes = {
    "un": "not, opposite of", "re": "again", "dis": "not, opposite of",
    "pre": "before", "in": "not or into", "im": "not or into",
    "inter": "between", "mis": "wrongly", "sub": "under, below",
    "super": "above, beyond", "trans": "across, beyond", "anti": "against",
    "auto": "self", "bi": "two", "circum": "around", "de": "down, away, reverse",
    "ex": "out of, former", "fore": "before", "mid": "middle",
    "over": "excessive", "semi": "half", "under": "below, insufficient",
}

suffixes = {
    "ing": "action or process", "ness": "state or quality", "ed": "past tense",
    "er": "one who, comparative", "ly": "characteristic of", "tion": "state or action",
    "ity": "state or quality", "ment": "action or process", "able": "capable of being",
    "al": "pertaining to", "ence": "state or quality", "est": "superlative adjective",
    "ful": "full of", "ic": "pertaining to", "ish": "like, characteristic of",
    "let": "small", "ous": "full of", "ship": "state or condition", "y": "characterized by",
}

# Morpheme type classifications with brief descriptions
prefix_types = {
    "un": ("bound morpheme", "derivational (negation)"),
    "re": ("bound morpheme", "derivational (repetition)"),
    "dis": ("bound morpheme", "derivational (negation)"),
    "pre": ("bound morpheme", "derivational (temporal: before)"),
    "in": ("bound morpheme", "derivational (negation or direction)"),
    "im": ("bound morpheme", "derivational (negation or direction)"),
    "inter": ("bound morpheme", "derivational (between)"),
    "mis": ("bound morpheme", "derivational (wrongly)"),
    "sub": ("bound morpheme", "derivational (spatial: under, below)"),
    "super": ("bound morpheme", "derivational (spatial: above, beyond)"),
    "trans": ("bound morpheme", "derivational (across, beyond)"),
    "anti": ("bound morpheme", "derivational (against)"),
    "auto": ("bound morpheme", "derivational (self)"),
    "bi": ("bound morpheme", "derivational (two)"),
    "circum": ("bound morpheme", "derivational (around)"),
    "de": ("bound morpheme", "derivational (down, away, reverse)"),
    "ex": ("bound morpheme", "derivational (out of, former)"),
    "fore": ("bound morpheme", "derivational (temporal: before)"),
    "mid": ("bound morpheme", "derivational (spatial: middle)"),
    "over": ("bound morpheme", "derivational (excessive)"),
    "semi": ("bound morpheme", "derivational (half)"),
    "under": ("bound morpheme", "derivational (below, insufficient)"),
}

suffix_types = {
    "ing": ("bound morpheme", "inflectional (progressive verb form)"),
    "ness": ("bound morpheme", "derivational (forms nouns from adjectives)"),
    "ed": ("bound morpheme", "inflectional (past tense of verbs)"),
    "er": ("bound morpheme", "derivational (agent noun or comparative adjective)"),
    "ly": ("bound morpheme", "derivational (forms adverbs from adjectives)"),
    "tion": ("bound morpheme", "derivational (forms nouns)"),
    "ity": ("bound morpheme", "derivational (forms nouns)"),
    "ment": ("bound morpheme", "derivational (forms nouns)"),
    "able": ("bound morpheme", "derivational (capable of being)"),
    "al": ("bound morpheme", "derivational (pertaining to)"),
    "ence": ("bound morpheme", "derivational (state or quality)"),
    "est": ("bound morpheme", "inflectional (superlative adjective)"),
    "ful": ("bound morpheme", "derivational (full of)"),
    "ic": ("bound morpheme", "derivational (pertaining to)"),
    "ish": ("bound morpheme", "derivational (like, characteristic of)"),
    "let": ("bound morpheme", "derivational (small)"),
    "ous": ("bound morpheme", "derivational (full of)"),
    "ship": ("bound morpheme", "derivational (state or condition)"),
    "y": ("bound morpheme", "derivational (characterized by)"),
}

lemmatizer = WordNetLemmatizer()


def is_real_word(word):
    """Check if WordNet contains the given word"""
    return bool(wordnet.synsets(word))


def analyze_word(word):
    """Analyze prefix, root, suffix and return a string with the results"""
    word = word.lower()
    found_prefix = ""
    found_suffix = ""
    root_candidate = word
    results = []

    # Detect prefix (longest first)
    for p in sorted(prefixes, key=len, reverse=True):
        if word.startswith(p):
            maybe_root = word[len(p):]
            if is_real_word(maybe_root):
                found_prefix = p
                root_candidate = maybe_root
                break

    # Detect suffix (longest first)
    for s in sorted(suffixes, key=len, reverse=True):
        if root_candidate.endswith(s):
            maybe_root = root_candidate[:-len(s)]
            if is_real_word(maybe_root):
                found_suffix = s
                root_candidate = maybe_root
                break

    root_lemma = lemmatizer.lemmatize(root_candidate)

    if is_real_word(root_lemma):
        root_meaning = wordnet.synsets(root_lemma)[0].definition()
    else:
        root_meaning = "Not found in WordNet"

    results.append(f"**Results for:** **`{word}`**")
    if found_prefix:
        p_type = prefix_types.get(found_prefix, ("unknown", "unknown"))
        results.append(f"**Prefix:** `{found_prefix}` | **Meaning:** _{prefixes[found_prefix]}_ | **Type:** `{p_type[0]}, {p_type[1]} morpheme`")
    results.append(f"**Root:** `{root_lemma}` | **Meaning:** _{root_meaning}_ | **Type:** `free root morpheme`")
    if found_suffix:
        s_type = suffix_types.get(found_suffix, ("unknown", "unknown"))
        results.append(f"**Suffix:** `{found_suffix}` | **Meaning:** _{suffixes[found_suffix]}_ | **Type:** `{s_type[0]}, {s_type[1]} morpheme`")
    if not (found_prefix or found_suffix):
        results.append("No prefix or suffix found. The whole word may be the root.")
    
    return "\n\n".join(results)


def get_morpheme_tree(word):
    """Return a string representing the morpheme tree."""
    word = word.lower()
    found_prefix = ""
    found_suffix = ""
    root_candidate = word

    # Detect prefix (longest first)
    for p in sorted(prefixes, key=len, reverse=True):
        if word.startswith(p):
            maybe_root = word[len(p):]
            if is_real_word(maybe_root):
                found_prefix = p
                root_candidate = maybe_root
                break

    # Detect suffix (longest first)
    for s in sorted(suffixes, key=len, reverse=True):
        if root_candidate.endswith(s):
            maybe_root = root_candidate[:-len(s)]
            if is_real_word(maybe_root):
                found_suffix = s
                root_candidate = maybe_root
                break

    root_lemma = lemmatizer.lemmatize(root_candidate)
    
    tree_lines = []
    
    tree_lines.append(f"**Morpheme Tree for:** **`{word}`**\n")

    if found_prefix and found_suffix:
        # prefix, root, suffix all present (horizontal three-branch)
        tree_lines.append(f"`        {word}`")
        tree_lines.append("`    /     |     \\`")
        tree_lines.append(f"`   {found_prefix}   {root_lemma}   {found_suffix}`")
    elif found_prefix:
        # Only prefix case tree:
        tree_lines.append(f"`       {word}`")
        tree_lines.append("`     /    |`")
        tree_lines.append(f"`   {found_prefix}    {root_lemma}`")
    elif found_suffix:
        # Only suffix case tree:
        tree_lines.append(f"`       {word}`")
        tree_lines.append("`      |     \\`")
        tree_lines.append(f"`    {root_lemma}     {found_suffix}`")
    else:
        # Only root case:
        tree_lines.append(f"`      {root_lemma}`")
        tree_lines.append("`    /   |   \\`")
        tree_lines.append(f"`  ...   {root_lemma}   ...`")

    return "\n".join(tree_lines)


def app():
    """Main function for the Streamlit app."""
    st.set_page_config(page_title="Morpheme Analyzer", layout="centered")

    st.title("Linguistic Morpheme Analyzer")
    st.markdown("""
        **Enter a word below** and this app will attempt to break it down into its
        constituent morphemes (prefix, root, suffix). It provides a linguistic analysis
        and a simple tree diagram. 🌳
    """)
    
    user_input = st.text_input("Enter a word:", "unbelievably").strip()

    if user_input:
        if not user_input.isalpha():
            st.warning("Please enter a valid alphabetic word only.")
        else:
            st.markdown("---")
            analysis_text = analyze_word(user_input)
            st.markdown(analysis_text)
            
            st.markdown("---")
            tree_text = get_morpheme_tree(user_input)
            st.markdown(f"```\n{tree_text}\n```")


if __name__ == "__main__":
    app()
