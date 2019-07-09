# 数据库交互模块
import redis
from tools.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD,PC_KEY,APP_KEY
# 代理池数据库连接
class RedisClient(object):

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis密码
        """
        self.db = redis.Redis(host=host, port=port, password=password, decode_responses=True)

    # 代理随机获取功能
    def get_pc_agent(self):

        return self.db.srandmember(PC_KEY,1)

    def get_app_agent(self):
        return self.db.srandmember(APP_KEY,1)


    # 返回当前代理池总计数
    def get_all(self):

        data={
            'app':self.db.scard(APP_KEY),
            'pc':self.db.scard(PC_KEY),
        }

        return data

if __name__ == '__main__':

    run = RedisClient()
    print(run.get_pc_agent())
    print(run.get_app_agent())
    print(run.get_all())
    agent = run.get_pc_agent()
    if agent:
        print(agent[0])


