from flask import Flask
from flask_restful import Api
from video import Video
from video_schedule import VideoSchedule


app = Flask("VideoAPI")
api = Api(app)


api.add_resource(Video, '/videos/<video_id>')
api.add_resource(VideoSchedule, '/videos')

if __name__ == '__main__':
    app.run()
