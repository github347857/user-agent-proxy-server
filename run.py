# user-agent代理池
# 提供app端和PC端接口

import sys
import io
from tools.scheduler import Scheduler
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()

if __name__ == '__main__':
    main()