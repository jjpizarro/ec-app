# ec-app
Creamos el repositorio local y se sincroniza con el repositorio remoto 

<code>
git config --global pull.rebase true

echo "# ec-app" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/jjpizarro/ec-app.git

git push -u origin main

</code>

## Instalando las dependecias 
<code>pip install fastapi

pip install "uvicorn[standard]"

 pip install SQLAlchemy</code>

#Listado de requeriments
<code>pip freeze > requirements.txt
</code>



