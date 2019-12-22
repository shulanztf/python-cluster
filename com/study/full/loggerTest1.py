"""
https://www.cnblogs.com/qianyuliang/p/7234217.html
Python logger模块
"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
val1 = 33
# finish_msg = """
# finish,test
# """ + val1
finish_msg = "finish,test:%s,%s" % (33, 53)
logger.info(finish_msg)
