import time


class Token(object):
    def __init__(self, expire_time, token_string):
        self.expire_time = expire_time
        self.token_string = token_string

    def is_valid(self):
        """
        :return: If the token is valid or not
        """
        return self.expire_time <= time.clock().real
pass

