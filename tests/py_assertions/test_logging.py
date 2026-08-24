import logging
logger = logging.getLogger(__name__)

def test_myloggings():
    logger.info('Info log')
    logger.warning("Warning Logs")
    logger.error("Error logs")
    logger.critical('Critical error')
    assert True