# Empty lines must be removed from the list of lines.

str_list = ["first", "", "second", "", ""]
while '' in str_list:
    str_list.remove('')
print(str_list)
