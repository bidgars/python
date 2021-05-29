import logging
import logging.config
import yaml
from os import path

log_conf_path = path.join(path.dirname(path.abspath(__file__)), "logging.conf")
logging.config.fileConfig(log_conf_path)


log_conf_path = path.join(path.dirname(path.abspath(__file__)), "loggingconf.yml")
with open(log_conf_path, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# create logger
logger = logging.getLogger(path.basename(__file__).strip(".py"))

# 'application' code
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
