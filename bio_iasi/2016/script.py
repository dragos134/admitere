

def scrie_antet(filename):
    filename.write("\\documentclass{article}\n")
    filename.write("\\usepackage{hyperref}\n")
    filename.write("\\usepackage{fixltx2e}\n")
    filename.write("\\usepackage{amsmath}\n")
    filename.write("\\usepackage{siunitx}\n")
    filename.write("\\usepackage{textgreek}\n")
    filename.write("\\begin{document}\n")

def scrie_subsol(filename):
    filename.write("\\end{document}")

def prelucrare(filename : str):
    file_obj = open(filename)
    content = file_obj.read()
    file_obj.close()

    content = content.split('\n!')


if __name__ == "__main__":
    pass


    