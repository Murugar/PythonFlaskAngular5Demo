from flask import Flask,request,jsonify
import requests;
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

languages = [{'name':'test1'},{'name':'test2'},{'name':'test3'},{'name':'test4'},{'name':'test5'},{'name':'test6'}]
@app.route('/')
def abc():
    return 'Python Angular5 World Hello world'

@app.route('/lang')
@cross_origin()
def lang():
    return jsonify({'lang': languages})


@app.route('/lang/<string:name>')
def spec(name):
    print(name);
    lang = [language for language in languages if language['name'] == name]
    if lang:
        return jsonify({'lang': lang[0]})
    else:
        return jsonify({'lang': 'Sorry'})



@app.route('/about',methods=['POST'])
def abcd():
    langs = {'name': request.json['name']}
    languages.append({'name':langs['name']})
    print(languages)
    return jsonify(langs)


if __name__ == '__main__':
    app.run(debug=True)
