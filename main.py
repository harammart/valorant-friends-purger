import time

import urllib3

from internal import ValorantInternal

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main() -> None:
    val = ValorantInternal()
    friends = val.get_friends()
    for friend in friends.friends:
        status = val.remove_friend(friend)
        print(status)
        time.sleep(0.5)
    return


if __name__ == '__main__':
    main()
