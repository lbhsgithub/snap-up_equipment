import time
import main
import request


def current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def x_sharp(time1, time2, cookie):
    k = 1
    while True:
        print("post time is", current_time(), time.time() % 1)
        post_result = main.main(time1, time2, cookie, None)
        k = k + 1  # avoid something unexpected!
        if if_stop(post_result, cookie) | k > 5:
            break


def if_stop(text, cookie):
    if not text['result']['result']:
        message = text['result']['message']
        result_ = text['result']
        if '?' in message:  # merge?
            r = request.post_dayi(result_['validate'], result_['bstart'], result_['bend'], cookie, result_['bid'])
            print(r.text)  # return r.ok
        else:
            return '已经被' in message  # 已被其他人预约,终止。已被。。。10000次  # False的情况：未开放预约+超过240小时+其他人正在预约
    return True


def auto_post(cookie, time_list_):
    while True:
        # for debug
        if time_list_:
            time_list = time_list_
        else:
            time_list = ['09', '10', '11', '14', '15', '16']
        # if at time
        if current_time()[11:13] in time_list:
            # history: add -30min to avoid error from across the hour
            time1 = time.strftime('%Y-%m-%d %H:00', time.localtime(time.time() + 10 * 24 * 60 * 60))
            time2 = time1[0:-4] + str(int(time1[12]) + 1) + ':00'  # str is immutable in Python
            print("at the target time period [", time1, "] to [", time2, "]")
            # gap to the accurate time to post
            gap = 3600.001 - time.time() % 3600
            print("wait", round(gap // 60), "minutes", round(gap % 60), "seconds to oclock and post")
            time.sleep(gap)
            # the true gap time should contain print and code identify in main, so the gap time can be reduced properly
            # at sharp
            x_sharp(time1, time2, cookie)
        else:
            print("current time is [", current_time(), "] , out of target time period", time_list)
            time.sleep(30*60)


if __name__ == "__main__":
    auto_post('496612547D018C2213D4CA960EA1C6E9', '22')
    # for debug
    # x_sharp('2019-05-13 15:00', '2019-05-13 16:00', '496612547D014C2213D4CA910EA1C6E3')

# 猜测服务器时间
# post time is 2019-04-27 23:00:00 0.0012314319610595703
# {'result': False, 'message': '预约的结束时间必须距离当前时间240小时内！'}
