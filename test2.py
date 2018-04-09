from aip import AipSpeech
from qiniu import Auth, put_data

APP_ID = '***APPID***'
API_KEY = '***API_KEY***'
SECRET_KEY = '***SECRET_KEY***'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis(
	'现在的男生为什么不追女生？因为不划算。要我付出，对方白白享受我的好处，凭什么？要聊天、交流可以。但是要我花钱，对不起一分钱没有，有也不花在这个上，要么AA制要么拜拜。说我直男癌，不在乎女生怎么想？拜托，凭什么要我一味地迁就你怎么想？就算要，你也得在乎我怎么想。你不在乎我怎么想，你就不会成为我觉得重要的人，我自然也不会在乎你怎么想。不是因为你是女生我就要天然地让着你。很多女生抱怨男生急着上床，其实很好理解：他对你那么好，如果不是想上你，凭什么？凭什么给你做这做那，凭什么每天甜言蜜语哄着你？你以为你是谁？从这些男生的角度，他对你的付出（言语上、物质上）的在没发生关系前都属于沉没成本。单方面做了这么多，你要是最后不给上怎么办？所以很多男生自然急着上床：不上床心里就没底，上床了至少不亏.',
	'zh', 1, {
		'vol': 7,
		'per': 3
	})

AK = '***AK***'
SK = '***SK***'
bucket_name = 'video'
q = Auth(AK, SK)
key = 'test2.mp3'
token = q.upload_token(bucket_name, key, 3600)
ret, info = put_data(token, key, result)
print(ret)
