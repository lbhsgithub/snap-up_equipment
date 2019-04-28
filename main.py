import request
import identify


def main(time_start, time_end, cookie, bookid):
    request.download_verification_code(cookie)
    verification_code = identify.binarize()
    # 3 post
    r = request.post_dayi(verification_code, time_start, time_end, cookie, bookid)
    text = r.json()  # requests自带json解码，转json为dict
    print(text['result'])
    return text


if __name__ == "__main__":
    main('2019-05-13 15:00', '2019-05-13 16:00', '496612347D012C2453D4CA230EA1C6E9', None)
