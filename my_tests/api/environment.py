import os


class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: '',
        PROD: '',
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS.get(self.env)

        raise Exception(f'Unknown value of ENV variable {self.env}')


ENV_OBJECT = Environment()
