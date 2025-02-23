```markdown
# CatalogoJosefina

O **CatalogoJosefina** é um sistema desenvolvido em Django para atender às demandas da Escola Municipal Professora Josefina Teixeira de Azevedo. O sistema foi criado com o objetivo de digitalizar e gerenciar documentos antigos, como históricos escolares, registros de matrícula e atas finais.

## Objetivo

O objetivo principal do **CatalogoJosefina** é:

- **Reduzir o espaço físico** ocupado pelos documentos antigos.
- **Proteger a integridade** dos documentos com backups digitais.
- **Facilitar a recuperação de informações** pela secretaria e diretoria da escola.

## Funcionalidades

- **Digitalização e Organização de Documentos:**
  - A secretaria tem acesso completo ao sistema para digitalizar, organizar e gerenciar documentos antigos.
  
- **Acesso Restrito à Diretoria:**
  - A diretoria tem acesso restrito, com permissões apenas para visualização dos documentos digitalizados.

## Tecnologias Utilizadas

- **Django:** Framework web para desenvolvimento do backend.
- **HTML:** Estruturação das páginas web.
- **JavaScript (JS):** Interatividade e funcionalidades dinâmicas no frontend.
- **Tailwind CSS:** Framework para estilização rápida e responsiva.
- **CSS:** Estilos personalizados para o design das páginas.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/PratesLucas/SistemaDeCatalogo.git
   cd SistemaDeCatalogo
   ```

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações:**
   Configure o banco com o de sua preferência no settings.py de acordo com a documentação do django e faça as migrações como descrito abaixo:

   ```bash
   python manage.py migrate
   ```

5. **Crie um usuário administrador:**

   Como este será o primeiro usuário administrador do sistema, você precisará criá-lo manualmente através do terminal. Execute o seguinte comando:

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções no terminal para definir um nome de usuário, email e senha para o administrador.

6. **Inicie o servidor:**

   ```bash
   python manage.py runserver
   ```

7. **Acesse o sistema no navegador:**

   Abra `http://127.0.0.1:8000/` para acessar o sistema.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.