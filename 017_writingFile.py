text = "this is line 1\nthis is line 2\n\nthis is line 4"

# truncation mode is enabled by default
with open('C:\\Users\\Uday\\Desktop\\test_for_python_writing.txt', 'w') as file: # second arg is for the writing mode
    file.write(text)

with open('C:\\Users\\Uday\\Desktop\\test_for_python_writing.txt') as file1:
    print(file1.read())

# use 'a' instead of 'w' for append mode