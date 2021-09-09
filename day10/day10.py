# Functions with Outputs

# def format_name(f_name, l_name):
#    formatted_f_name = f_name.title()
#    formated_l_name = l_name.title()

#    return f"{formatted_f_name} {formated_l_name}"

# formatted_string = format_name("john", "SMITH")

# print(formatted_string)


def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the the title case version of the name."""
    if f_name == "" or l_name == "":
        return " You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formatted_f_name} {formated_l_name}"


print(format_name(input("What is your first name?: "),
      input("What is your last name?: ")))

