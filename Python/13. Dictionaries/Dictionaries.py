# stores in information in keyvalue pair. which can be accessed with its keys.
# Just like a normal dictionary, here the word=key, definition=value. "key:value".Both int and string work

month_conversion = {"Jan": "January", "Feb": "February", "Mar": "March"}

print(month_conversion["Feb"])
print(month_conversion.get("Feb"))

#  with the get() function you can handle errors as well

print(month_conversion.get("Dec"))  # Yields "None"
print(month_conversion.get("Dec", "Invalid Key"))  # Yields the message
