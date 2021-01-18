from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
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

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Missing Name of the video")
video_update_args.add_argument("views", type=int, help="Missing Views of the video")
video_update_args.add_argument("likes", type=int, help="Missing Likes of the video")

resource_fields = {
    "id": fields.String,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields) # need this because you cannot return an object, it needs to be serializable
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first() # look through all videos and return first response that has that id
        if not result:
            abort(404, message="video_id does not exist")

        return result, 200

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video_id already exists")

        video = VideoModel(id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    # UPDATE call
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video_id does not exist")
        
        if args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.name = args["views"]
        if args["likes"]:
            result.name = args["likes"]

        db.session.commit()
        return result, 200

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        db.session.delete(result)
        db.session.commit()
        return '', 204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
