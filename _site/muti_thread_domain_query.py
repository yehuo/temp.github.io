#!/usr/bin/env python
import threading
import os
import re

domains = []
ips = []
thread_limit = 4
threading.Semaphore(thread_limit)


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def domain_reader():
    file = open('domain.txt', 'r+')
    content = file.readlines()
    # 验证ip\域名有效性
    for domain in content:
        domains.append(domain.strip())
    file.close()
    return domains


def loop(domain_name):
    print(threading.current_thread().name, domain_name)
    command = "ping " + domain_name + " -w 5 -n 1"
    # print(command)
    result = os.popen(command)
    result = result.read()
    ip = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
                    result)
    if len(ip) != 0:
        ips.append(ip[0])


def main():
    threads = []
    domain_reader()
    count_domain = range(len(domains))
    for i in count_domain:
        # print(domains[i])

        t = threading.Thread(target=ThreadFunc(loop, (domains[i],), loop.__name__))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    iplist = list(set(ips))
    print(iplist)


if __name__ == '__main__':
    main()
