from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


def validate_number(number):
    return number == str(123)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        if validate_number(number):
            print("valid number")
            message = ["同学" + str(i) + "信息    排序：" for i in range(5)]
            return render_template('dynamic.html', message1=message[0],
                                   message2=message[1],
                                   message3=message[2],
                                   message4=message[3],
                                   message5=message[4],
                                   )
        else:
            # 数字不符合要求，重新渲染表单页面
            return render_template('welcome.html', error='数字不符合要求，请重新输入')
    return render_template('welcome.html', error=None)


@app.route('/getRank', methods=['POST'])
def get_rank():
    data = request.json
    print(data)
    return 'ok'


if __name__ == '__main__':
    app.run()
