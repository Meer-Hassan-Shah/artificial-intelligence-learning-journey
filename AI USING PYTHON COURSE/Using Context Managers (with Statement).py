

with open ("example.txt", "r") as file:  # Open the file in read mode using a context manager
    data = file.read()  # Read the contents of the file and store it in the variable `data`
    print(data)  #  Print the contents of the file to the console

    # The file will be automatically closed after the block of code is executed, even if an error occurs. This is one of the main advantages of using a context manager with the `with` statement.