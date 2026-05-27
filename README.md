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





