from flask_restful import Resource, abort, reqparse
from video_file_changes import write_changes_to_file, videos


parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, location='form')
parser.add_argument('uploadDate', type=int, required=False, location='form', help='Upload date must be an integer')


class Video(Resource):

    @classmethod
    def get(cls, video_id):
        if video_id == "all":
            return videos
        if video_id not in videos:
            abort(404, message=f'Video {video_id} was not found!')
        return videos[video_id]

    @classmethod
    def put(cls, video_id):
        args = parser.parse_args()
        new_video = {'title': args['title'],
                     'uploadDate': args['uploadDate']}
        videos[video_id] = new_video
        write_changes_to_file()
        return {video_id: videos[video_id]}, 201

    @classmethod
    def delete(cls, video_id):
        if video_id not in videos:
            abort(404, message=f'Video {video_id} was not found!')
        del videos[video_id]
        write_changes_to_file()
        return "", 204
