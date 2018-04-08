from zhihu_oauth import ZhihuClient

client = ZhihuClient()
TOKEN_FILE = 'token.pkl'
client.load_token(TOKEN_FILE)

me = client.me()
