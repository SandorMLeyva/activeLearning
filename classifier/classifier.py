from flask import Flask, render_template, make_response
from flask.json import jsonify
import json
import time

app = Flask(__name__)
app.__setattr__('_id_', -1)
app.__setattr__('name_file', "./"+str(time.time())+"_result.json")
# global _id_
# print('cojoneeeeeee')
with open('./comments.json','r',encoding='utf8') as f:
#     json = f.read()
    dataset = json.loads(f.read())
    x_unlabeled = [item for item in dataset['texts']]

result = []

@app.route('/')
def index():
	return make_response(render_template('index.html'))


@app.route('/data')
def data():
    app._id_ += 1
    return jsonify({
            'current': x_unlabeled[app._id_],
            'id': app._id_
        })



@app.route('/classificate/<answ>/<_id>')
def classs(answ,_id):
    result.append({
        'text': x_unlabeled[int(_id)],
        'answers': [{
            'answer': answ
        }]
    })
    with open(app.name_file,'w',encoding='utf8') as f:
#     json = f.read()
        dataset = json.dumps(result)
        f.write(dataset)
    return jsonify({})


app.run(host='0.0.0.0',port=8080,debug=False)