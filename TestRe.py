import re
# a = "The BodyGuard is the best album"

# # Define the pattern to search for
# pattern = r"BodyGuarl"

# # Use the search() function to search for the pattern in the string
# result = re.search(pattern, a)

# # Check if a match was found
# if result:
#     print("Match found!")
# else:
#     print("Match not found.")
pattern = r"\D\D\D\D\D"
text = "My Phone Number is $@ 9080850614"
match = re.search(pattern,text)
if match:
    print("Mobile Number Found:",match.group())
else:
    print("Match Not Found!")


s2 = "The BodyGuard is the best album of 'Whitney Houston'."
result = re.findall("st", s2)
print(result)


split_array = re.split(r"\D\D\D", s2)
print(split_array)

import re
# Define the regular expression pattern to search for
pattern = r"Whitney Houston"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 
