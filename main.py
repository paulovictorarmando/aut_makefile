import pathlib
import sys


if len(sys.argv) != 5:
    print("Erro, forma de usar: ")
    print("python3 main.py linguagem(c/cpp) compilador(cc/c++) nome_exec \"flags(-Wall -Wextra -Werror)\"")
    sys.exit(1)


if sys.argv[1].lower() != 'c' and sys.argv[1].lower() != 'cpp':
    print("Erro, só linguagens c e c++ permitidas")
    sys.exit(1)


try:
    pathlib.Path('./Makefile').unlink()
except:
    pass


srcs =  [
		str(f) for f in pathlib.Path('./').rglob('*')
		if f.is_file() and (
			f.suffix == '.cpp' and sys.argv[1].lower() == 'cpp'
			or
			f.suffix == '.c' and sys.argv[1].lower() == 'c'
		)
	]
headers =[
		str(f) for f in pathlib.Path('./').rglob('*')
		if f.is_file() and (
			f.suffix == '.hpp' and sys.argv[1].lower() == 'cpp'
			or
			f.suffix == '.h' and sys.argv[1].lower() == 'c'
		) 
	]

with open("./Makefile", "a+") as file:
    file.write(f"NAME = {sys.argv[3]}\n\n")
    file.write(f"HEAD = ")
    for f in headers:
        file.write(f"\t\t\t{f}\\\n")
    file.write("\n")
    file.write(f"SRC = ")
    for f in srcs:
        file.write(f"\t\t\t{f}\\\n")
    file.write("\n")
    file.write(f"CXX = {sys.argv[2].lower()}\n\n")
    file.write(f"CXXFLAGS = {sys.argv[4]}\n\n")
    file.write(f"OBJ = $(SRC:.{sys.argv[1].lower()}=.o)\n\n")
    file.write(f"all: $(NAME)\n\n")
    file.write(f"$(NAME): $(OBJ) $(HEAD)\n")
    file.write(f"\t$(CXX) $(CXXFLAGS) $(OBJ) -o $(NAME)\n\n")
    file.write(f"clean:\n\trm -f $(OBJ)\n\n")
    file.write(f"fclean: clean\n\trm -f $(NAME)\n\n")
    file.write(f"re: fclean all")
