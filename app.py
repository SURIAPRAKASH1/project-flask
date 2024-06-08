from flask import Flask,render_template,request,redirect
from tmdb import movie_search
from moviedata import datas
from retrivedata import retrive_datas

app = Flask(__name__)


@app.route('/')
def index():


    try:

        response = request.args.get('movie')

    
        if (response):
            retrive_data= retrive_datas()
            
            for data in retrive_data:
                if str(response) in data[0].lower():
                    return render_template('contant2.html' , datas = retrive_data , condition = response)
                

            result = movie_search(response)

            for row in result['results']:

                title = row['title']
                release_date = row['release_date']
                datas(title,release_date)

            return render_template('contant.html',movies=result)
            
        return render_template('render.html')
    except Exception:
        return ('<h1>Something Went Worng ! Try again</h1>')



if __name__=='__main__':
    app.run(debug=True)