# 🛠️ Auto Makefile Generator

Este projeto foi criado para **gerar automaticamente um Makefile** bem estruturado para projetos em **C** ou **C++**.  
Basta executar o script Python na raiz do projeto e ele se encarrega de procurar todos os arquivos-fonte (`.c` / `.cpp`) e cabeçalhos (`.h` / `.hpp`) — mesmo em **subpastas** — e criar um **Makefile limpo, funcional e atualizado**.  

Se um Makefile já existir, ele será **substituído por um novo**, mantendo a estrutura padrão e regras consistentes.  

---

## 🚀 Como usar

### 📍 Execução
Na raiz do seu projeto, execute o script principal passando os seguintes argumentos:

```bash
python3 main.py <linguagem> <compilador> <nome_exec> "<flags>"
```


# 💡 Exemplo de uso
## 🔹 Para projeto em C:
```
  python3 main.py c cc my_program "-Wall -Wextra -Werror"
```

## 🔹 Para projeto em C++:
```
  python3 main.py cpp c++ my_project "-std=c++98 -Wall -Wextra -Werror"
```

Após a execução, um Makefile completo será criado automaticamente na raiz do projeto. <br>
Ele incluirá regras como: <br>
```
  all → Compila o projeto
  
  clean → Remove arquivos objeto
  
  fclean → Remove arquivos objeto e o executável
  
  re → Recompila tudo do zero
```
## 🧠 O que o script faz
```
  ✅ Detecta automaticamente todos os arquivos .c / .cpp no projeto (inclusive em subdiretórios)
  ✅ Gera variáveis organizadas como SRCS, OBJS, CC, CFLAGS, NAME etc.
  ✅ Cria um Makefile padronizado e legível
  ✅ Substitui Makefiles antigos de forma segura
  ✅ Garante compatibilidade com a estrutura tradicional dos projetos da 42 School ou projetos pessoais
```
## ⚠️ O script deve ser executado na raiz do projeto, para que consiga localizar todos os arquivos corretamente
