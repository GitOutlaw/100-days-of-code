# Get names
with open("day24/Mail Merge Project Start/Input/Names/invited_names.txt", encoding="utf8") as file:
    
    contents = file.readlines()
    # get_name = contents[0:-1]
    # final_name = get_name.strip("\n")
    
    # with open("day24/Mail Merge Project Start/Input/Letters/starting_letter.txt", 'r', encoding='utf-8') as letter_file:
    #     first_line = letter_file.readlines(1)
    #     get_first_line = first_line[0]        
    #     write_new_line = get_first_line.replace("[name],", f"{final_name},")
    #     all_lines = letter_file.read()

    #     with open(f"day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{final_name}.txt", "w", encoding="utf8") as mail_file:
    #         mail_file.write(write_new_line)
    #         mail_file.write(all_lines)
