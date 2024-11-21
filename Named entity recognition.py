import spacy

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text for entity recognition
text = """
Apple is looking at buying U.K. startup for $1 billion. The deal, if completed, could create a significant impact in the tech world.
Elon Musk has announced that the SpaceX launch will take place in 2023.
"""

# Processing the text using spaCy NLP pipeline
doc = nlp(text)

# Extracting the named entities and their labels
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Printing the results
print("Named Entities, Phrases, and Concepts:")
for entity in entities:
    print(f"{entity[0]} - {entity[1]}")
