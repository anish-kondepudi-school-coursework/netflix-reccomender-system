from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Retrieve the values from the form
        tmdb_score = float(request.form.get('tmdb_score'))
        imdb_votes = int(request.form.get('imdb_votes'))
        runtime = int(request.form.get('runtime'))
        release_year = int(request.form.get('release_year'))
        seasons = int(request.form.get('seasons'))

        # Calculate the sum
        total = tmdb_score + imdb_votes + runtime + release_year + seasons
        result = f"The sum is: {total}"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
