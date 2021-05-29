# Basic handler
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s ~ %(name)s ~ %(levelname)s ~ %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# logging.exception("exception")
# print("Empty Line")

logger1 = logging.getLogger(__name__)
logger1.info("Hello from logger")
logger1.debug("Hello from logger")

del logger1

try:
    a = [1, 2, 3, 4]
    val = a[5]
except IndexError as e:
    logging.error(e, exc_info=True)
