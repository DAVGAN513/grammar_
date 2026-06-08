import nltk
from nltk import CFG

grammar_string = """
    S -> NPC VP NPC | NPC VP
    NPC -> NP NPC_A
    NPC_A -> Conj NP NPC_A | 
    NP -> Art Noun
    Art -> 'le' | 'la' | 'les'
    Noun -> Reg | Eau
    Reg -> RegR RegE
    Eau -> EauR EauE
    RegR -> 'stylo' | 'livre' | 'cahier' | 'chaise' | 'table' | 'gomme'
    EauR -> 'tableau' | 'bureau'
    RegE -> 's' | 
    EauE -> 'x' | 
    VP -> 'utilise' | 'utilisent' | 'a' | 'ont' | 'regarde' | 'regardent'
    Conj -> 'et' | 'ou'
"""
french_grammar = CFG.fromstring(grammar_string)

parser = nltk.ChartParser(french_grammar)

def preprocess_sentence(sentence):
    words = sentence.split()
    processed_words = []
    
    excepciones = ['les', 'utilisent', 'regardent']
    
    for word in words:
        if word in excepciones:
            processed_words.append(word)
        elif word.endswith('eaux'):
            processed_words.append(word[:-1]) 
            processed_words.append('x')
        elif word.endswith('s'):
            processed_words.append(word[:-1]) 
            processed_words.append('s')
        else:
            processed_words.append(word)
            
    return processed_words

def validate_french_sentence(sentence):
    print("-" * 50)
    print(f"Original sentence: '{sentence}'")
    
    processed_words = preprocess_sentence(sentence)
    print(f"Processed tokens: {processed_words}")
    
    try:
        trees = list(parser.parse(processed_words))
        
        if len(trees) > 0:
            print("The sentence is:\n")
            for tree in trees:
                tree.pretty_print()
        else:
            print("The sentence is incorrect.")
            
    except ValueError as e:

        print(f"The sentence is incorrect: {e}")

if __name__ == "__main__":
    print("INPUT SENTENCES")
    
    print("CORRECT SENTENCES")
    validate_french_sentence("le stylo a le cahier")
    validate_french_sentence("les stylos utilisent les tableaux")
    validate_french_sentence("la chaise et le bureau regardent le tableau")
    validate_french_sentence("les cahiers ou les livres ont le stylo")
    
    print("\n INCORRECT SENTENCES")
    validate_french_sentence("le stylo x a le cahier") 
    validate_french_sentence("chaise utilise stylo") 
    validate_french_sentence("les tableaus ont le livre")