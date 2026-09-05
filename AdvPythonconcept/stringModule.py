# import string module 
import string 

# Python strings are:
# Ordered → characters have positions/indexes... e.g "string" = 0123456 .
# Immutable → you cannot directly change an existing string.                                                     
# Iterable → you can loop through characters.
# Unicode-based → they can store text from many languages.
 

#  string.lower(), string.upper(), string[index no], string.strp()- remove space from last and start , lstrip (remove left side space ), rstrip(right side / end space ), string.title(capslock or cappital), string.index(python),

replace = "I love Java"

replaced = replace.replace("Java", "Python")
print(replaced)

text = "cat cat cat"   
# replace * 2
# print(text.replace("cat", "dog", 2))
# print(text.find("Python"))

# string validation check 
# if there only letter True else false 
# isalpha → letters only
# isdigit  → digits only
# isalnum  → letters + digits
text = "python"
text.isalpha() #True
# text = "73" text.isdigit() #return True 

#letter + num 
# text.isalnum()
# print("Python ".isspace())
# # False

# "ABC".isalpha()      → True
# "123".isdigit()      → True
# "ABC123".isalnum()   → True
# "   ".isspace()      → True
# "abc".islower()      → True
# "ABC".isupper()      → True
# "Hello World".istitle() → True

#  Str immutablity 

# text = "Python"
# newtext= "C" + text[0:]
# print(f"after: {newtext},before : { text}")


# import string

# string.ascii_letters
# string.ascii_lowercase
# string.ascii_uppercase
# string.digits
# string.punctuation
# string.whitespace
# string.printable


text = string.ascii_letters
print(text)
text = string.ascii_lowercase
print(text)
text = string.ascii_uppercase
print(text)
text = string.digits
print(text)

#template text 

template_text = "hello $name, welcome to $company"

# Template is a Class so we need to first create a obj..
template = string.Template(template_text)

# then we just use template formated dict. 
formated_text = template.substitute(
    {
        "name": "Anish", 
        "company" : "OpenAI"
    }
    )

print(formated_text)

# templated used when you doesn't know the what data will come . 