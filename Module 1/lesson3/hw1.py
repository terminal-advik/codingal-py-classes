"""
1) Ask for agent details.
   a) Ask the user to enter their real name.
   b) Ask the user to enter their favourite gadget.
   c) Store both inputs as text values.

2) Store agent information.
   a) Create variables for agent number, speed rating, mission count, height, and active status.
   b) Use different data types such as integer, float, string, and Boolean.

3) Display each value and its data type.
   a) Print the agent name and gadget.
   b) Print number, rating, mission count, height, and active status.
   c) Use `type()` to show the data type of each value.

4) Convert values into text.
   a) Use `str()` to convert numbers into strings.
   b) Convert the Boolean value into text.
   c) Print the converted values and their new data types.

5) Create a secret code name.
   a) Use slicing to get the first three letters of the name.
   b) Use negative indexing to get the last letter.
   c) Join both parts to create the code name.

6) Reverse the gadget name.
   a) Use slicing with `[::-1]` to reverse the gadget text.
   b) Print the reversed gadget name.

7) Build the badge message.
   a) Create separate lines for the agent badge.
   b) Use string concatenation to join text and variables.
   c) Use `.upper()` to make important badge text uppercase.

8) Print the secret agent badge.
   a) Print a badge heading.
   b) Print all badge lines one by one.
   c) Print a closing line to complete the badge.
"""

name = input("Enter your name, Agent: ")
gadget = input("Enter your favorite gadget: ")
agent_number = 10
speed_rate = 6.7
mission_count = 21
height = 2.167
is_active = True

print("Name:", name, "-> type:", type(name))
print("Gadget:", gadget, "-> type:", type(gadget))
print("Agent Number:", agent_number, "-> type:", type(agent_number))
print("Speed Rate:", speed_rate, "-> type:", type(speed_rate))
print("Mission Count:", mission_count, "-> type:", type(mission_count))
print("Height:", height, "-> type:", type(height))
print("Is Active:", is_active, "-> type:", type(is_active))

agent_number_text = str(agent_number) # "10"
mission_count_text = str(mission_count) # "21"
speed_rate_text = str(speed_rate)
status_text = str(is_active)

print("Agent Number as text:", agent_number_text, "-> type:", type(agent_number_text))
print("Mission Count as text:", mission_count_text, "-> type:", type(mission_count_text))
print("Speed Rate as text:", speed_rate_text, "-> type:", type(speed_rate_text))
print("Is Active as text:", status_text, "-> type:", type(status_text))

first_three_letters = name[0:3] # 0 1 2
last_letter = name[-1:] # ADVIK , [-1 : 5]
code_name = first_three_letters + last_letter 
print("First 3 letters of name:", first_three_letters)
print("Last letter of name:", last_letter)
print("Secret code name:", code_name)
reversed_gadget = gadget[::-1] 
print("Reversed Gadget Name:", reversed_gadget)
