# Stream and File handler
import logging

logger = logging.getLogger(__name__)

streamH = logging.StreamHandler()
fileH = logging.FileHandler("loggerfile.log")

streamH.setLevel(logging.DEBUG)
fileH.setLevel(logging.ERROR)

fmt = logging.Formatter("%(name)s ~ %(levelname)s ~ %(message)s")
streamH.setFormatter(fmt)
fileH.setFormatter(fmt)

logger.addHandler(streamH)
logger.addHandler(fileH)

logger.warning("This is warning")
logger.error("This is error from logger")
