def get_config(account, password):
    config = {
                    'host': '127.0.0.1',
                    'port': 3306,
                    'user': account,
                    'password': password,
                    'db': 'cardo',
                    'charset': 'utf8mb4',
                    'cursorclass': cursors.DictCursor,
                }
    return config