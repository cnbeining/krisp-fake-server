#!/usr/bin/env python
# encoding: utf-8
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)


## edit response


@app.route('/v2/user/profile/2/1')
def user_profile_2_1():
    """Used in the app to get the user's profile when first login"""
    req = requests.get('https://api.krisp.ai/v2/user/profile/2/1',
                       headers = {'Authorization': request.headers['Authorization']})
    data = req.json()
    # print(data)
    try:
        data['data']['mode']['name'] = 'unlimited'
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
        data['data']['settings']['public_api']['available'] = True
        data['data']['settings']['record']['available'] = True
        data['data']['settings']['record']['config']['approved'] = True
        data['data']['settings']['send_usage_data']['available'] = False
    
    except Exception as e:
        logging.error(e)
        pass
    return jsonify(data), req.status_code


@app.route('/v2/user/minutes/balance')
def user_minutes_balance():
    """Used in the app after every call to update the minutes balance"""
    request_body = request.get_json()
    request_body['nc_out'][0]['used_seconds'] = 1
    req = requests.post('https://api.krisp.ai/v2/user/minutes/balance', json = request_body,
                        headers = {'Authorization': request.headers['Authorization']})
    data = req.json()
    # print(data)
    try:
        data['data']['nc_out']['range_ends'] = 31536000
        data['data']['nc_out']['balance'] = 31536000
        data['data']['nc_out']['template']['balance'] = 31536000
        data['data']['nc_out']['template']['range'] = 31536000
    except Exception as e:
        logging.error(e)
        pass
    return jsonify(data), req.status_code


## proxy

@app.route('/v2/auth/verify', methods = ['POST'])
def auth_verify():
    """Used in web to verify 2FA code"""
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/verify', json = request_body)
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/email/web-sign-in', methods = ['POST'])
def auth_email_web_sign_in():
    """Used in web to send 2FA code"""
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/email/web-sign-in', json = request_body)
    return jsonify(req.json()), req.status_code


@app.route('/v2/user/accounts')
def user_accounts():
    """Used in web to get the user's profile after login"""
    req = requests.get('https://api.krisp.ai/v2/user/accounts',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/token/web', methods = ['PATCH'])
def auth_token_web():
    request_body = request.get_json()
    req = requests.patch('https://api.krisp.ai/v2/auth/token/web', json = request_body,
                         headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/token/app/1', methods = ['POST'])
def auth_token_app_1():
    """Used in web when Krisp application calls web to trigger login"""
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/token/app/1', json = request_body,
                        headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/user/organizations/teammates/count')
def user_organizations_teammates_count():
    """Used in web to get teammates"""
    req = requests.get('https://api.krisp.ai/v2/user/organizations/teammates/count',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/auth/code', methods = ['POST'])
def auth_code():
    """Used in web to convert 2FA code to Bearer token while logging in"""
    request_body = request.get_json()
    req = requests.post('https://api.krisp.ai/v2/auth/code', json = request_body,
                        headers = {'Authorization': request.headers['Authorization'], 'jwt': request.headers['jwt']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/insights/summary')
def insights_summary():
    req = requests.get('https://api.krisp.ai/v2/insights/summary',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/user/profile/2')
def user_profile_2():
    """Used in web to get user's profile"""
    req = requests.get('https://api.krisp.ai/v2/user/profile/2',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/notification')
def notification():
    """Used in app to fetch in-app notification content"""
    req = requests.get('https://api.krisp.ai/v2/notification',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/payment/plans')
def payment_plans():
    """Used `in web to get the user's plan and available plans"""
    req = requests.get('https://api.krisp.ai/v2/payment/plans',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/payment/billing')
def payment_billing():
    """Used in web to get the user's billing information"""
    req = requests.get('https://api.krisp.ai/v2/payment/billing',
                       headers = {'Authorization': request.headers['Authorization']})
    return jsonify(req.json()), req.status_code


@app.route('/v2/installation', methods = ['POST', 'GET'])
def installation():
    if request.method == 'POST':  # Used in app after launch
        request_body = request.get_json()
        req = requests.post('https://api.krisp.ai/v2/installation', json = request_body,
                            headers = {'Authorization': request.headers['Authorization']})
        return jsonify(req.json()), req.status_code
    
    # Used in web. Should have an installation_id in parameter but should not matter
    return jsonify({"code": 0, "message": "Success", "data": {"isOldVersion": False}, "req_id": "rq"}), 200


## static

@app.route('/v2/health/')
def health():
    """Used in app"""
    return jsonify({
        "api_version": "1.0.4"
    })


@app.route('/v2/resource/chat')
def resource_chat():
    """Used in web for the chat bubble"""
    req = requests.get('https://api.krisp.ai/v2/resource/chat?ajax=1')
    return jsonify({
                       "code": 0, "data": {"name": "any", "url": "https://help.krisp.ai/hc/en-us/requests/new?ajax=1"},
                       "message": "Success", "req_id": "rq"
                   }), req.status_code


if __name__ == '__main__':
    app.run()
