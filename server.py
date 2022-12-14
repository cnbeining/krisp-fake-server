#!/usr/bin/env python
# encoding: utf-8
import json
import requests
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

## edit response


@app.route('/v2/user/profile/2/1')
def user_profile_2_1():
    req = requests.get('https://api.krisp.ai/v2/user/profile/2/1', headers={'Authorization': request.headers['Authorization']})
    data = req.json()
    #print(data)
    try:
        data['data']['mode']['props']['nc_out']['balance'] = 31536000
        data['data']['mode']['props']['nc_out']['template']['ui_info']['plan_title_text'] = 'NULLED PLAN'
        data['data']['mode']['props']['nc_out']['template']['balance'] = 31536000
        data['data']['mode']['props']['nc_out']['template']['range'] = 31536000
        data['data']['settings']['nc_out']['minutes_settings']['range_ends'] = 31536000
        data['data']['settings']['nc_out']['minutes_settings']['balance'] = 31536000
        data['data']['settings']['nc_out']['minutes_settings']['template']['balance'] = 31536000
        data['data']['settings']['nc_out']['minutes_settings']['template']['range'] = 31536000
        data['data']['settings']['asr_features']['available'] = True
        data['data']['settings']['nc_delay']['available'] = True
        data['data']['settings']['send_usage_data']['available'] = False
    except:
        pass
    return jsonify(data), req.status_code


@app.route('/v2/user/minutes/balance')
def user_minutes_balance():
    request_body = request.get_json()
    request_body['nc_out'][0]['used_seconds'] = 1
    req = requests.post('https://api.krisp.ai/v2/user/minutes/balance', json=request_body, headers={'Authorization': request.headers['Authorization']})
    data = req.json()
    #print(data)
    try:
        data['data']['nc_out']['range_ends'] = 31536000
        data['data']['nc_out']['balance'] = 31536000
        data['data']['nc_out']['template']['balance'] = 31536000
        data['data']['nc_out']['template']['range'] = 31536000
    except:
        pass
    return jsonify(data), req.status_code


## proxy

@app.route('/v2/auth/verify', methods = ['POST'])
def auth_verify():
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/verify', json=request_body)
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/email/web-sign-in', methods = ['POST'])
def auth_email_web_sign_in():
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/email/web-sign-in', json=request_body)
    return jsonify(req.json()), req.status_code


@app.route('/v2/user/accounts')
def user_accounts():
    req = requests.get('https://api.krisp.ai/v2/user/accounts', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/token/web', methods = ['PATCH'])
def auth_token_web():
    request_body = request.get_json()
    req = requests.patch('https://api.krisp.ai/v2/auth/token/web', json=request_body, headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code

@app.route('/v2/auth/token/app/1', methods = ['POST'])
def auth_token_app_1():
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/token/app/1', json=request_body, headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/user/organizations/teammates/count')
def user_organizations_teammates_count():
    req = requests.get('https://api.krisp.ai/v2/user/organizations/teammates/count', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/code', methods = ['POST'])
def auth_code():
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/code', json=request_body, headers={'Authorization': request.headers['Authorization'], 'jwt': request.headers['jwt']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/insights/summary')
def insights_summary():
    req = requests.get('https://api.krisp.ai/v2/insights/summary', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


# this is used in web only
@app.route('/v2/user/profile/2')
def user_profile_2():
    req = requests.get('https://api.krisp.ai/v2/user/profile/2', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/notification')
def notification():
    req = requests.get('https://api.krisp.ai/v2/notification', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/payment/plans')
def payment_plans():
    req = requests.get('https://api.krisp.ai/v2/payment/plans', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/payment/billing')
def payment_billing():
    req = requests.get('https://api.krisp.ai/v2/payment/billing', headers={'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/installation', methods = ['POST', 'GET'])
def installation():
    if request.method == 'POST':  # app
        request_body = request.get_json()
        req = requests.post('https://api.krisp.ai/v2/installation', json=request_body, headers={'Authorization': request.headers['Authorization']})
        return jsonify(req.json()), req.status_code
    
    # web
    return jsonify({"code":0,"message":"Success","data":{"isOldVersion":False},"req_id":"rq"}), 200


## static

@app.route('/v2/health/')
def health():
    return jsonify({
        "api_version": "1.0.4"
    })


@app.route('/v2/resource/chat')
def resource_chat():
    req = requests.get('https://api.krisp.ai/v2/resource/chat?ajax=1')
    return jsonify({"code":0,"data":{"name":"any","url":"https://help.krisp.ai/hc/en-us/requests/new?ajax=1"},"message":"Success","req_id":"rq"}), req.status_code


if __name__ == '__main__':
    app.run()

