fname = str(input("Enter first name: "))
lname = str(input("Enter last name: "))
section = str(input("Enter section: "))
favSubj = str(input("Enter favorite subject: "))

full_name = f"{fname.strip()} {lname.strip()}"
code_name = full_name.title()
upper_name = full_name.upper()
upper_section = section.strip().upper()
title_subj = favSubj.strip().title()
char_count = len(full_name)

print("\nFormatted Output: ")
print(f"Name: {code_name}")
print(f"Name Code: {upper_name}")
print(f"Section: {upper_section}")
print(f"Favorite Subject: {title_subj}")
print(f"Character Count: {char_count}")
