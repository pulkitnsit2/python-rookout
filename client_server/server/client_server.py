import logging.config
import os
from os import path

from sanic import Sanic
from sanic import response
from sanic.exceptions import ServerError
import rook

logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.prod.ini'), disable_existing_loggers=False)
logging.getLogger("sanic.access").propagate = False
logging.getLogger("sanic.root").propagate = False

logger = logging.getLogger(__name__)


app = Sanic("TEE")


@app.before_server_start
async def load_rookout(_, __):
    logger.info("Loading Rookout")
    rook.start(token=os.environ["ROOKOUT_TOKEN"])
    logger.info("Rookout Loaded")


@app.get("/health")
async def get_health_status(_):
    return response.json({"success": True})


@app.route("/")
async def test_async(request):
    logger.info(f"info_test_async_1: request.args: {request.args}, request.url: {request.url}")
    logger.info("info_test_async_2")
    logger.info("info_test_async_3")
    logger.debug("debug_test_async_4")
    logger.debug("debug_test_async_5")
    return response.json({"test": True})


@app.route("/exception")
def exception(request):
    logger.info("info_exception_1")
    logger.info("info_exception_2")
    logger.debug("debug_exception_3")
    logger.debug("debug_exception_4")
    raise ServerError("It's dead")


@app.route("/await")
async def test_await(request):
    import asyncio
    await asyncio.sleep(5)
    return response.text("I'm feeling sleepy")


def main():
    logger.info(f"Client Server started listening")
    app.run(host='0.0.0.0', port=1337, workers=2, access_log=False)


if __name__ == '__main__':
    main()
