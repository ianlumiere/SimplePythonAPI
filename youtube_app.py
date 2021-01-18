from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# create model for the db
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes}"

# db.create_all() # only do this once

# create parameters for a valid video PUT call
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Missing Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Missing Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Missing Likes of the video", required=True)

videos = {}

def abort_if_video_missing(video_id):
    if video_id not in videos:
        abort(404, message="video_id is not valid")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="video_id already exists")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_missing(video_id)
        return videos[video_id], 200
    
    # How to do without reqparse
    # def put(self, video_id):
    #     print(request.form["likes"])
    #     return {}

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_missing(video_id)
        del videos[video_id]
        return '', 204
    

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
