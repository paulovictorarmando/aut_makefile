# ðŸ› ï¸ Auto Makefile Generator
Este projeto foi criado para **gerar automaticamente um Makefile** bem estruturado para projetos em **C** ou **C++**. 
Basta executar o script Python na raiz do projeto e ele se encarrega de procurar todos os arquivos-fonte (`.c` / `.cpp`) e cabeÃ§alhos (`.h` / `.hpp`) â€” mesmo em **subpastas** â€” e criar um **Makefile limpo, funcional e atualizado**. 
Se um Makefile jÃ¡ existir, ele serÃ¡ **substituÃ­do por um novo**, mantendo a estrutura padrÃ£o e regras consistentes. 
---
## ðŸš€ Como usar
### ðŸ“ ExecuÃ§Ã£o
Na raiz do seu projeto, execute o script principal passando os seguintes argumentos:
```bash
python3 main.py <linguagem> <compilador> <nome_exec> "<flags>"
```
### ðŸ“˜ ParÃ¢metros
| Argumento       | DescriÃ§Ã£o                                                                 | Exemplo                     |
|-----------------|------------------------------------------------------------------------------|------------------------------|
| `linguagem`     | Define o tipo de projeto: `c` ou `cpp`.                                     | `c` ou `cpp`                 |
| `compilador`    | O compilador a ser usado (`cc` ou `c++`).                                   | `cc`, `gcc`, `c++`, `g++`    |
| `nome_exec`     | O nome do executÃ¡vel que serÃ¡ gerado.                                       | `programa`, `app`, `main`    |
| `"flags"`       | (Opcional) Flags de compilaÃ§Ã£o. Devem ser passadas entre aspas.             | `"-Wall -Wextra -Werror"`    |
---
## ðŸ’¡ Exemplo de uso
### ðŸ”¹ Para projeto em C:
```bash
python3 main.py c cc my_program "-Wall -Wextra -Werror"
```
### ðŸ”¹ Para projeto em C++:
```bash
python3 main.py cpp c++ my_project "-std=c++98 -Wall -Wextra -Werror"
```
ApÃ³s a execuÃ§Ã£o, um **Makefile completo** serÃ¡ criado automaticamente na raiz do projeto. 
Ele incluirÃ¡ regras como:
- `all` â†’ Compila o projeto 
- `clean` â†’ Remove arquivos objeto 
- `fclean` â†’ Remove arquivos objeto e o executÃ¡vel 
- `re` â†’ Recompila tudo do zero 
---
## ðŸ§  O que o script faz
âœ… Detecta automaticamente todos os arquivos `.c` / `.cpp` no projeto (inclusive em subdiretÃ³rios) 
âœ… Gera variÃ¡veis organizadas como `SRCS`, `OBJS`, `CC`, `CFLAGS`, `NAME` etc. 
âœ… Cria um Makefile padronizado e legÃ­vel 
âœ… Substitui Makefiles antigos de forma segura 
âœ… Garante compatibilidade com a estrutura tradicional dos projetos da **42 School** ou projetos pessoais 
---
## ðŸ“‚ Estrutura esperada
```
ðŸ“¦ seu_projeto/
 â”£ ðŸ“œ main.py
 â”£ ðŸ“œ Makefile      â† serÃ¡ criado automaticamente
 â”£ ðŸ“ src/
 â”ƒ â”£ main.c
 â”ƒ â”£ utils.c
 â”ƒ â”— ...
 â”£ ðŸ“ includes/
 â”ƒ â”£ utils.h
 â”ƒ â”— ...
```
> âš ï¸ O script **deve ser executado na raiz do projeto**, para que consiga localizar todos os arquivos corretamente.
---
## ðŸ§¾ SaÃ­da gerada (exemplo simplificado)
```makefile
NAME = my_program
CC = cc
CFLAGS = -Wall -Wextra -Werror
SRCS = src/main.c \
       src/utils.c
OBJS = $(SRCS:.c=.o)
all: $(NAME)
$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)
clean:
	rm -f $(OBJS)
fclean: clean
	rm -f $(NAME)
re: fclean all
```
---
## ðŸ§° Requisitos
- **Python 3.6+**
- Um projeto em **C** ou **C++** com estrutura organizada (subpastas opcionais)
---
## ðŸ§‘â€ðŸ’» Autor
**Paulo Armando** 
ðŸ“ Desenvolvido para automatizar a criaÃ§Ã£o de Makefiles limpos e padronizados. 
ðŸ’¬ Se gostou, deixe uma â­ no repositÃ³rio!
---
## ðŸ–¤ LicenÃ§a
Este projeto Ã© de uso livre. 
Sinta-se Ã  vontade para modificar, distribuir ou incorporar em seus prÃ³prios projetos.
