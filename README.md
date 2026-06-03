# grammar_
David Antonio Gandara Ruiz A01713432

# Description

The language that i chose for this analysis is FRENCH, specifially focusing on school and classroom vocabulary. French is a roman language derived from latin ans is one of the most widely spoken language globally. French grammar is extensive and complex thi project will focus on a restricted contex grammar centered around classroom objects, basic verbs and how plurars are formed the language

# Language Structure

French grammar differs significantly from English in two main aspects at gender and articles, every noun in french is either masculine or feminine, French heavily realies on definite articles that are le, la, les
To reduce the scope of the grammar and focus on syntax analysis the formation of plurals will be analyzad,while English usually just add an 's' French has regular and irregular plural forms depending on the ending of the word

REGULAR PLURAL: most nouns form their plural by adding an -s at the end an example is stylo (pen) becomes stylos

IRREGULAR PLURAL: Nouns ending in -eau form their plural by adding an -x instead of an -s an example is tableau becomes tableaux

For the scope of this parser we will assume definite articles are always used while the grammar ensure the plural suffixes are grammatically correct it will not enforce deep context about gender or number agreenent between the article and the noun 

# Plural Rules 

To get a better understand how to form the plurals in this restricted grammar here are the basic rules
- 1: REGULAR WORDS = when a word does not an end in -eau the plural is formed by adding an s
- 2: WORDS ENDING in -eau the plural is formed by adding an x

# Models

The model used is a grammar that can create an validate the plurals created in a sentence here is the school related vocabulary that will be used: 
## ARTICLES
- `le` : the masculine singular
- `la` : the feminine singular
- `les` : the plural

## NOUNS ROOTS
REGULAR ENDINGS:
- `stylo`: pen
- `livre`: book
- `cahier`: notebook
- `chaise`: chair
- `table`: table
- `gomme`: eraser

IRREGULAR ENDING:
- `tableau`: board
- `bureau`: desk

## VERBS
- `a / ont`: has / have
- `utilise / utilisent`: uses / use
- `regarde / regardent`: looks at / look at

## CONJUNTIONS
- `et`: and
- `ou`: or

# Grammar

To give some context Geeks for Geeks mentions that in several phases exist in compiler design the syntax analysis checks if the input follows the grammar assigned to the compiler, the parser implemented here is an LL(1) which this operates top down without backtracking and without recursive descent making it highky efficient 
So to achive an LL(!) parser we need to do some steps this ones are the main for the initial grammar: 
- 1: Eliminate ambiguity we need to ensure only one unique syntax tree can be generated per valid input
- 2: Eliminate left recursion we need to ensure the tree grows from the right to avoid infinite loops during top down parsing

# Initial Grammar 

```text
S -> NPC VP NPC | NPC VP
NPC -> NPC Conj NPC | NP
NP -> Art Noun
Noun -> Reg | Eau
Reg -> RegR RegE
Eau -> EauR EauE
RegR -> 'stylo' | 'livre' | 'cahier' | 'chaise' | 'table' | 'gomme'
EauR -> 'tableau' | 'bureau'
RegE -> 's' | Empty
EauE -> 'x' | Empty
Art -> 'le' | 'la' | 'les'
VP -> 'utilise' | 'utilisent' | 'a' | 'ont' | 'regarde' | 'regardent'
Conj -> 'et' | 'ou'
```
The rule NPC -> NPC Conj NPC | NP is both ambiguous and left recursive. Ambiguity arises because conjunction chains can generate multiple valid parse trees, while left recursion prevents the grammar from being LL(1). By introducing the auxiliary non terminal NPC_A, the grammar is restructured to eliminate left recursion and ensure a unique parsing strategy, satisfying LL(1) constraints: 

```text
NPC -> NP NPC_A
NPC_A -> Conj NP NPC_A | Empty
```

# Grammar that recognizes the language 

Here is the final LL(1) compliant grammar:

```text
S -> NPC VP NPC | NPC VP
NPC -> NP NPC_A
NPC_A -> Conj NP NPC_A | Empty
NP -> Art Noun
Art -> 'le' | 'la' | 'les'
Noun -> Reg | Eau
Reg -> RegR RegE
Eau -> EauR EauE
RegR -> 'stylo' | 'livre' | 'cahier' | 'chaise' | 'table' | 'gomme'
EauR -> 'tableau' | 'bureau'
RegE -> 's' | Empty
EauE -> 'x' | Empty
Empty -> 
VP -> 'utilise' | 'utilisent' | 'a' | 'ont' | 'regarde' | 'regardent'
Conj -> 'et' | 'ou'
```

# Explanation of the grammar 

- S -> NPC VP NPC | NPC VP: A sentence consists of a noun phrase block, a verb, and optionally an object noun phrase block
- NPC -> NP NPC_A: A noun phrase block starts with a base noun phrase, followed by a continuation to handle conjunctions without left recursion
- NPC_A -> Conj NP NPC_A | Empty: The continuation can be a conjunction followed by another noun phrase, or it can be empty
- NP -> Art Noun: A single noun phrase strictly requires an article and a noun
- Noun -> Reg | Eau: A noun can either follow regular plural rules or irregular -eau rules
- RegR / EauR: The lexical roots of the school vocabulary
- RegE / EauE: The plural suffixes. Regular nouns take an 's' or remain empty (singular). Irregular -eau nouns take an 'x' or remain empty

# Implementatiom

To test this grammar the python program using NLTK can be utilizad tis program will require a preprocessing step that separates plural endings from their roots before passing them to the parser

# Correct Sentence
- Le stylo a le cahier
- Les stylos utilisent les tableau x
- La chaise et le bureau regardent le tableau
- Les cahier s ou les livres ont le stylo
- Le bureau a le cahier et les gommes

# Incorrect sentences
- Le stylo x xa le cahier
- Les tableau s ont le livre
- Chaise utilise stylo
- Le stylo et ou le cahier a

# Analysis
Asymptotic Analysis
For this the lexer must iterate through the users input string to separate the suffixes, this preprocessing string manipulation aperates at O(n) time complexity where the n is the number of character or words in the sentences, since the grammar was rigorously refactored to be an ll(1) parser by eliminating all ambiguity and left recursion the nltk parser will only ever find one unique valid parse tree ti doesnt need to backtrack or generate exponetial combinatorial trees, the parsinf itself is highly optimal maintaining an overall linear O(n) complexity for validating and generating the tree

# Type of Grammar
Now regarding the Chomsky Hierarchy this is a contect free grammar it is not regular grammar because regular grammars only allow a single non terinal on the left hand side and a right hand side consistieng of a single terminal or a single terminal followed by a single non terminal, this grammar contains rules like can be two non terminals on the right wich strictly categorizes it as a context free grammar.


