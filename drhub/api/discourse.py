"""Discourse API views for intergration with chatfuel json api"""

import os

from flask import jsonify, Blueprint

from drhub.libs.discourse.client import DiscourseClient

discourse_client = DiscourseClient(os.environ.get('DISCOURSE_HOST'),
                                   api_username=os.environ.get(
                                       'DISCOURSE_API_USERNAME'),
                                   api_key=os.environ.get('DISCOURSE_API_KEY'))

discourse = Blueprint('discourse', __name__, url_prefix='/discourse')


@discourse.route('/topics/top', methods=['GET'])
def get_hotests_topics():
    top_topics = discourse_client.top_topics()
    topics = []
    for topic in top_topics[0]:
    return jsonify({'messages': top_topics})
