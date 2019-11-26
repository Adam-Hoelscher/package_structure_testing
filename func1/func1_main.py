from func1_help import where_am_i


def main_1():
    msg = ''.join(['Hello from ', where_am_i(), '!'])
    return msg


if __name__ == '__main__':
    print(main_1())
