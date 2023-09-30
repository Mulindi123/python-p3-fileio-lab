def write_file(file_name, file_content):
    file_name  = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(file_content)
        print(f"Successfully wrote to {file_name}")


       
           


def append_file(file_name, append_content):
    file_name = file_name + ".txt"
    with open(file_name, "a") as text_file:
        text_file.write(append_content)
        print(f"Succefully appended to {file_name}")



def read_file(file_name):
    file_name = file_name + ".txt"
    with open(file_name)as text_file:
        content = text_file.read()
    return content


write_file("log", "Log 1: 5 bananas added. " )
append_file("log", "Log 2: 3 bananas subtracted.")
read_file("log")
