import os, re
from operator import attrgetter

github_url = 'https://github.com/Tony5t4rk/LeetCode/blob/master/'
readme_file = os.path.join('.', 'README.md')
readme_head = '''# LeetCode

My own leetcode practice record.

The detailed blog is at [leetcode](https://www.wolai.com/tony5t4rk/6dxxdnKmbu3rpFuKtFyGvj).

## Problem List
'''


class Problem:
    def __init__(self, qid, url):
        self.qid = qid
        self.url = url

    def __repr__(self):
        return 'Problem:{qid:' + str(self.qid) + ' url:' + str(self.url) + '}'


problems = []


def add_file(path):
    full_filename = path.split(os.sep)[-1]
    filename, ext = full_filename.split('.')

    extract_re = re.compile(r'[(](.*?)[)]', re.S)
    qid = int(re.findall(extract_re, filename)[0])
    url = github_url + '/'.join(path.split(os.sep)[1:])

    problems.append(Problem(qid, url))


def search_file(path):
    dirs = os.listdir(path)
    for dir in dirs:
        cur_path = path + os.sep + dir
        if os.path.isdir(cur_path):
            search_file(cur_path)
        else:
            add_file(cur_path)


def write_readme(readme_file):
    readme = open(readme_file, 'w')
    readme.write(readme_head)
    for problem in problems:
        readme.write('\n[{}]({})\n'.format(problem.qid, problem.url))
    readme.close()


daily_path = os.path.join('.', 'daily')

search_file(daily_path)
problems.sort(key=attrgetter('qid'))
write_readme(readme_file)
