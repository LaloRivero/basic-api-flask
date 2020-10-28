from flask import jsonify, request
from flask_pymongo import pymongo
from app import create_app
from bson.json_util import dumps
import db_config as db

app = create_app()

@app.route('/api/top_songs/', methods=['GET'])
def show_songs():
    all_songs = dumps(list(db.db.top_songs.find()))
    return all_songs


@app.route('/api/top_songs/<int:n_top>/', methods=['GET'])
def show_a_top_song(n_top):
    song = dumps(db.db.top_songs.find_one({'n_top':n_top}))
    return song


@app.route('/api/new_song/', methods=['POST'])
def add_new_song():
    db.db.top_songs.insert_one({
        "n_top": request.json["n_top"],
        "name":request.json["name"],
        "author":request.json["author"],
        "album":request.json["album"],
        "img":request.json["img"],
    })
    return jsonify({
        "message":"A new song wass added with success",
        "status": 200,
    })


@app.route('/api/top_songs/update/<int:n_top>',methods=['PUT'])
def update_song(n_top):

    if db.db.top_songs.find_one({'n_top':n_top}):
        db.db.top_songs.update_one({'n_top':n_top},
        {'$set':{
            "n_top": request.json["n_top"],
            "name":request.json["name"],
            "author":request.json["author"],
            "album":request.json["album"],
            "img":request.json["img"],
        }})
    else:
        return jsonify({"status":400, "message": f"Song #{n_top} not found"})

    return jsonify({"status":200, "message": f"The song #{n_top} of the top was updated"})


@app.route('/api/top_songs/del/<int:n_top>',methods=['DELETE'])
def delete_song(n_top):
    if db.db.top_songs.find_one({'n_top':n_top}):
        db.db.top_songs.delete_one({'n_top':n_top})
    else:
        return jsonify({"status":400, "message": f"Song #{n_top} not found"})
    return jsonify({"status":200, "message": f"The song #{n_top} was deleted"})

if __name__ == '__main__':
    app.run(load_dotenv=True, port=8080)