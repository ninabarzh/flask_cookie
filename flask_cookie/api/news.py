from flask import jsonify

from flask_cookie.services import news as news_services


def list_news():
    """API to list News"""
    return jsonify({"result": news_services.list_news()})


def create_news(body):
    """API to create News"""
    new_data = news_services.create_news(body["title"], body.get("description"))
    return jsonify(new_data), 201
