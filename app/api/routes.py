from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Dict, dict_schema, dicts_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/dicts', methods = ['POST'])
@token_required
def create_dict(current_user_token):
    word = request.json['word']
    meaning = request.json['meaning']
    part_of_speech = request.json['part_of_speech']
    gender = request.json['gender']
    plural = request.json['plural']
    present_tense = request.json['present_tense']
    past_tense = request.json['past_tense']
    past_part = request.json['past_part']
    perfect_aux = request.json['perfect_aux']
    preposition = request.json['preposition']
    case_triggered = request.json['case_triggered']
    user_token = current_user_token.token

    print(f'NOW TESTING: {current_user_token.token}')

    dict = Dict(word, meaning, part_of_speech, gender, plural, present_tense, past_tense, past_part, perfect_aux, preposition, case_triggered, user_token = user_token)

    db.session.add(dict)
    db.session.commit()

    response = dict_schema.dump(dict)
    return jsonify(response)

@api.route('/dicts', methods = ['GET'])
@token_required
def get_dict(current_user_token):
    a_user = current_user_token.token
    dicts = Dict.query.filter_by(user_token = a_user).all()
    response = dicts_schema.dump(dicts)
    return jsonify(response)

@api.route('/dicts/<id>', methods = ['GET'])
@token_required
def get_dict_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        dict = Dict.query.get(id)
        response = dict_schema.dump(dict)
        return jsonify(response)
    else:
        return jsonify({"message":"You must have a valid token."}), 401

@api.route('/dicts/<id>', methods = ['POST','PUT'])
@token_required
def update_dict(current_user_token,id):
    dict = Dict.query.get(id) 
    dict.word = request.json['word']
    dict.meaning = request.json['meaning']
    dict.part_of_speech = request.json['part_of_speech']
    dict.gender = request.json['gender']
    dict.plural = request.json['plural']
    dict.present_tense = request.json['present_tense']
    dict.past_tense = request.json['past_tense']
    dict.past_part = request.json['past_part']
    dict.perfect_aux = request.json['perfect_aux']
    dict.preposition = request.json['preposition']
    dict.case_triggered = request.json['case_triggered']
    dict.user_token = current_user_token.token

    db.session.commit()
    response = dict_schema.dump(dict)
    return jsonify(response)

@api.route('/dicts/<id>', methods = ['DELETE'])
@token_required
def delete_dict(current_user_token, id):
    dict = Dict.query.get(id)
    db.session.delete(dict)
    db.session.commit()
    response = dict_schema.dump(dict)
    return jsonify(response)