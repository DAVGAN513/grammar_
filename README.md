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


