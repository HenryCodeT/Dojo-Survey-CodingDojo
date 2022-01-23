# Dojo-Survey-CodingDojo
### Python - Flask - Fundamentls
### Install packages
* ```pipenv install flask```
* ```pipenv shell```
* ```pipenv server.py```
### project structure flask
| routs                  | Funtions         | return                         | methods |
|------------------------|------------------|--------------------------------|---------|
| Localhost:5000/        | index()          | render_template("index.html")  | GET     |
| Localhost:5000/        | index()          | return redirect('/results')    | POST    |
| Localhost:5000/results | results_survey() | render_template("result.html") | GET     |
### Sessions
* ```forms```
