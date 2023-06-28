from xml.etree.ElementTree import Comment
from flask import Flask,render_template,request
#from requests import request
app = Flask(__name__)
app.debug=True

@app.route('https://editor-edt.github.io/my-blog-EDT.github.io/blog_for_problems/templates/frame.html',methods=["GET","POST"])
def frame():
    if request.method == 'POST':
        print(request.form)
        if len(request.form) == 1:
            f = open('infor.txt','a')
            f.write(request.form['text']+')]}\n')
            f.close()
        else:
            f = open('comments.txt','a')
            f.write(request.form['id']+'{[('+request.form['comment']+')]}\n')
            f.close()
    f = open('infor.txt','r')
    fricts = f.read().split(')]}\n')[:-1]
    num_f = [ y for y in range(len(fricts))]
    print(fricts,num_f)
    f.close()

    f = open('comments.txt','r')
    comment_f = f.read().split(')]}\n')[:-1]
    comments = {}
    for z in comment_f:
        try:
            comments[int(z.split('{[(')[0])].append(z.split('{[(')[1])
        except:
            comments[int(z.split('{[(')[0])] = [z.split('{[(')[1]]
    print(comment_f,comments)
    f.close()
    return render_template('https://editor-edt.github.io/my-blog-EDT.github.io/blog_for_problems/templates/frame.html',posts = fricts, num_f = num_f, comments = comments)

@app.route('https://editor-edt.github.io/my-blog-EDT.github.io/blog_for_problems/templates/input.html')
def input():
    return render_template('https://editor-edt.github.io/my-blog-EDT.github.io/blog_for_problems/templates/input.html')

if __name__ == '__main__':
    app.run()
