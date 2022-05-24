# Executer of the code

fileLoaded = False

try:
    from program import Main  # ? > Run time file
    fileLoaded = True
    print("Program belleğe alındı.")

except Exception as e:
    fileLoaded = False
    print("Bir hata oluştu. Hata:\n")  # + e)


if __name__ == "__main__":
    if fileLoaded == True:
        program.Main()
