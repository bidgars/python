import logging
import logging.handlers
import time
from typing import Text

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, d , h , midnight, w
handler = logging.handlers.TimedRotatingFileHandler(
    "timedtest.log", when="M", backupCount=3
)
fmt = logging.Formatter("%(name)s ~ %(levelname)s ~ %(message)s")
handler.setFormatter(fmt)
logger.addHandler(handler)

for i in range(10000):
    logger.info("A message from timedlogrotate index= " + Text(i))
    time.sleep(1)
