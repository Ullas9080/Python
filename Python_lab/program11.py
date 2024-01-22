def freqency(file_name,letter):
    file=open(file_name)
    text=file.read()
    return text.count(letter)
print("Freqency of letter e")
print(freqency("D:/Programs/Python_lab/program10.txt","e"))