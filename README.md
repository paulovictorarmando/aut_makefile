
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
