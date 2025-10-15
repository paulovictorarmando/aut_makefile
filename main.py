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


srcs = [
            [ str(f) for f in pathlib.Path('./').rglob('*')
                if f.is_file()
                and (f.suffix == '.' + 'h' if sys.argv[1].lower() == 'c' else 'hpp') 
            ],
            [ str(f) for f in pathlib.Path('./').rglob('*')
                if f.is_file()
                and (f.suffix == '.' + 'c' if sys.argv[1].lower() == 'c' else 'cpp') 
            ]
        ]

with open("./Makefile", "a+") as file:
    file.write(f"NAME = {sys.argv[3]}\n\n")
    file.write(f"HEAD = ")
    for f in srcs[0]:
        file.write(f"\t\t\t{f}\\\n")
    file.write("\n")
    file.write(f"SRC = ")
    for f in srcs[1]:
        file.write(f"\t\t\t{f}\\\n")
    file.write("\n")
    file.write(f"CXX = {sys.argv[2].lower()}\n\n")
    file.write(f"CXXFLAGS = {sys.argv[4]}\n\n")
    file.write(f"OBJ = $(SRC:.{srcs[1][0].split('.')[1]}=.o)\n\n")
    file.write(f"all: $(NAME)\n\n")
    file.write(f"$(NAME): $(OBJ) $(HEAD)\n")
    file.write(f"\t$(CXX) $(CXXFLAGS) $(OBJ) -o $(NAME)\n\n")
    file.write(f"clean:\n\trm -f $(OBJ)\n\n")
    file.write(f"fclean: clean\n\trm -f $(NAME)\n\n")
    file.write(f"re: fclean all")