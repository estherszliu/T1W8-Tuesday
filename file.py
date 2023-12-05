readme_file = open("readme.txt", "r+")

print(readme_file.read())

readme_file.write("I am writing something in the file")

readme_file.close()