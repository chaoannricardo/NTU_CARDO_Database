def get_config(account, password):
    config = {
                    #'host': '127.0.0.1',
                    'host': '192.168.92.132',
                    'port': 3306,
                    'user': account,
                    'password': password,
                    'db': 'cardo',
                    'charset': 'utf8mb4',
                    'cursorclass': cursors.DictCursor,
                }
    return config
