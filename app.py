from flask import Flask, jsonify, make_response, request
from translate import bp_trans


app = Flask(__name__) 

app.register_blueprint(bp_trans)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'URL Não encontrada!'}), 404)

app.run(use_reloader=True)