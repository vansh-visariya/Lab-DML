from flask import Flask, render_template, request, redirect

app = Flask(__name__)

blogs = []

@app.route('/')
def home():
    return render_template('index.html', blogs=blogs)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        blogs.append({
            'id': len(blogs),
            'author': request.form['author'],
            'title': request.form['title'],
            'content': request.form['content']
        })
        return redirect('/')
    return render_template('write.html')

@app.route('/blog/<int:id>')
def view_blog(id):
    if id < len(blogs):
        return render_template('blog.html', blog=blogs[id])
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
