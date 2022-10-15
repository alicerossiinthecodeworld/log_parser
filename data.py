import glob
import os.path
from operator import itemgetter
from collections import Counter


def get_all_requests_from_file(filepath):
    if not os.path.isfile(filepath):
        return "Not a file"
    with open(filepath, mode='r', encoding="utf-8") as f:
        res = []
        for line in f:
            line = line.replace("-", "")
            line = line.replace('"', "")
            line = line.replace('[', "")
            line = line.replace(']', "")
            res.append([line.split()[0], line.split()[1] + line.split()[2], line.split()[3],
                        line.split()[len(line.split()) - 1]])
    return res


def get_all_request_from_dir(logpath):
    os.chdir(logpath)
    res = []
    for logfile in glob.glob("*log"):
        res.extend(get_all_requests_from_file(logfile))
    return res


def get_requests(path):
    if os.path.isdir(path):
        print(f"{path} is dir")
        return get_all_request_from_dir(path)
    elif os.path.isfile(path):
        print(f"{path} is file")
        return get_all_requests_from_file(path)
    return "Not a valid file or dir"


def get_most_common_request_ips(requests):
    ips_counter = Counter([value[0] for value in requests])
    return ips_counter.most_common(3)


def get_most_endured_request(requests):
    return sorted(requests, key=itemgetter(3), reverse=True)[:3]


def get_counter_for_each_request_type(requests):
    return dict(Counter([value[2] for value in requests]))
