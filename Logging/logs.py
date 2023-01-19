import logging

class LogGen:

    @staticmethod
    def logged():
        logger  = logging.getLogger("Test Login")
        fileHandler  = logging.FileHandler('.\\MyLogs')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger