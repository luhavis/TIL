
# Example : SELECT * FROM TEST WHERE ID = ?
query = ""

# Example : 1(Integer), John(String)
parameter = ""


parameters = parameter.split(",")



for val in parameters:
    qIndex = query.find("?")

    value = val[:val.find("(")].strip()
    value_type = val[val.find("(")+1:val.find(")")].strip()

    replaceChar = ""

    if value_type == "String":
        replaceChar = f"'{value}'"
    elif value_type == "Integer":
        replaceChar = value
    else:
        replaceChar = ""


    query = query[:qIndex] + replaceChar + query[qIndex+1:]

print(query)


