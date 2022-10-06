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
>
> ### 9. para fazer deploy utilizei o heroku. Atualizei os settings no app, criei as envs, procfile com gunicorn e rodei as migrates no heroku
>
> ### 10. para conectar-se com postgres você deve seguir os comandos do .env.example e criar seu arquivo .env
>
> ### 11. para rodar com django-admin basta acessar a rota: https://cnab-txt.herokuapp.com/api/upload/passar-um-parametro-qualquer e adicionar um texto
>
> ### 12. para testar pode rodar o seguinte texto cnab >> 3201903010000014200096206760174753\*\*\*\*3153153453JOÃO MACEDO BAR DO JOÃO
