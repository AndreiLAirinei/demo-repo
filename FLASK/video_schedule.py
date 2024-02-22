from flask_restful import Resource
from file_changes import write_changes_to_file, videos
from video import parser


class VideoSchedule(Resource):

    @classmethod
    def get(cls):
        return videos

    @classmethod
    def post(cls):
        args = parser.parse_args()
        new_video = {'title': args['title'],
                     'uploadDate': args['uploadDate']}
        video_id = max(int(v.lstrip('video')) for v in videos.keys()) + 1
        video_id = f"video{video_id}"
        videos[video_id] = new_video
        write_changes_to_file()
        return videos[video_id], 201

