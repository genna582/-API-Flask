import json

from flask import Flask, jsonify, request
from model.post import Post

app = Flask(__name__)

posts = []


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {'body': obj.body, 'author': obj.author, 'comments': obj.comment}
        else:
            return super().default(obj)


app.json_encoder = CustomJSONEncoder


# @app.route('/ping', methods=['GET'])
# def ping():
#     return jsonify({'response': 'pong'})

@app.route('/post', methods=['GET'])
def get_post():
    return jsonify({'posts': posts})


@app.route('/post', methods=['POST'])
def create_post():
    # {"body": "my first post", "author": "@genna582", "comment": " "}
    # {"body": "my second post","author": "@genna582", "comment": " "}
    post_json = request.get_json()
    post = Post(post_json['body'], post_json['author'], post_json['comment'])
    posts.append(post)

    return jsonify({'status': 'success'})


@app.route('/post/<int:task_id>', methods=['PUT'])
def update_post(task_id):
    # {"comment": "first post good"}
    # {"comment": "second post good"}
    if len(posts) != 0 and len(posts) >= task_id + 1:
        post_json = request.get_json()
        new_comments = post_json['comment']
        posts[task_id].comment = new_comments

    return jsonify({'posts': posts})


@app.route('/post/<int:task_id>', methods=['DELETE'])
def delete_post(task_id):
    if len(posts) != 0 and len(posts) >= task_id + 1:
        posts.pop(task_id)

    return jsonify({'posts': posts})


if __name__ == '__main__':
    app.run(debug=True)
