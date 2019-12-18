# https://www.cnblogs.com/lmx123/p/9246215.html 破解滑块（极验）验证码思路

def get_track(self, distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    track = []
    # 当前位移
    current = 0
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    while current < distance:
        if current < mid:
            # 加速度为正1
            a = 1
        else:
            # 加速度为负2
            a = -2
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track

if __name__ == '__main__':
    rslt = get_track("abc", 154)
    print(rslt)