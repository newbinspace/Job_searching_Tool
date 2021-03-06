from flask import Flask, render_template, url_for, request
from web_scraping.scraping import *
from web_scraping.utils import *
app = Flask(__name__)
df = pd.read_csv("%s/data/Job_search.csv" % main_path())

@app.route("/")
def main():
    return render_template('main.html')
@app.route("/", methods=['POST'])
def main_post():
    job_name = request.form['text']
    job_name = job_name.lower()
    df = search_algorithm(job_name)
    df['Job_link'] = df['Job_link'].apply(lambda x: '<a href="{0}">{0}</a>'.format(x))
    old_width = pd.get_option('display.max_colwidth')
    pd.set_option('display.max_colwidth', -1)
    return render_template('job_list.html',  tables=[df.to_html(classes='table table-striped table-hover',escape=False, index=False, justify='center')])

if __name__ == '__main__':
    app.run(debug=True)
