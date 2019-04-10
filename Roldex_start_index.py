from flask import Flask, request, render_template


app = Flask(__name__)
number_img = 1


@app.route('/')
@app.route('/roldex')
def roldex_sample():
    return render_template('index_roldex.html')


@app.route('/gallery')
def gallery():
    return render_template('index_gallery.html')


@app.route('/img_file', methods=['POST', 'GET'])
def sample_file_upload():
    global number_img
    if request.method == 'GET':
        return render_template('index_form.html')
    elif request.method == 'POST':
        f = request.files['file']
        file_name = 'static/img/img_' + str(number_img) + '.png'
        out = open(file_name, "wb")
        out.write(f.read())
        out.close()
        print('Success: file received')
        for i in range(1):
            number_img += 1
        return render_template('index_gallery.html'), number_img


@app.route('/my_work')
def my_work():
    return render_template('index_my_work.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
