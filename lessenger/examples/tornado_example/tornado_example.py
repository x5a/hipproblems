"""
To run:
    (from this directory)
    install requirements:
        make sure you have a python 2 or 3 runtime
        $ pip install -r requirements.txt
    run flask server:
        $ python -m tornado_example
"""

from tornado import ioloop, web
import json
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class MessagesHandler(web.RequestHandler):
    def post(self):
        # an HTML form can have multiple values per key, but the Lessenger API
        # has only one value per key
        form = {k: v[0] for k, v in self.request.body_arguments.items()}
        log.info("Recieved Form from Lessenger UI:%s", form)

        # set CORS wildcard header
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write(json.dumps(None))


def run():
    app = web.Application([
        (r"/chat/messages", MessagesHandler),
    ])
    app.listen(9000)
    ioloop.IOLoop.current().start()

if __name__ == "__main__":
    run()
