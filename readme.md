# CNAB TEXT

---

## Raciocínio

> ### 1. criado models e serializer para colocar os dados no banco de dados
>
> ### 2. não achei necessário criação de um swagger para aplicação pequena
>
> > 2.1 toda documentação está no readme.md
>
> ### 3. alterado settings do meu app cnab_txt conforme necessidade do projeto
>
> ### 4. na views, seguindo a documentação do django rest frame work devemos passar um filename no momento de fazer download do arquivo
>
> ### 5. testes rodados no insomnia foi jogado todos os dados para o banco de dados
>
> ### 6. rodei as makemigrations/migrates para criar o banco de dados
>
> ### 7. aplicação faz upload de um arquivo cnab.txt, arquivo diferente não terá leitura
>
> ### 8. utilizando FileUploadParser para fazer as validações de upload
