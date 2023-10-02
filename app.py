from flask import Flask, render_template

app = Flask(__name__)

@app.route('/url/task')
def task():
    # You can generate dynamic data here and pass it to the template
    dynamic_data = "This is dynamic data from the server!"
    return render_template('task.html', dynamic_data=dynamic_data)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
