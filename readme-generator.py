# coding=utf-8

import os, re
from operator import attrgetter

# github_url = 'https://github.com/Tony5t4rk/LeetCode/blob/master/'
readme_file = os.path.join('.', 'README.md')
readme_head = '''# LeetCode

My own leetcode practice record.

The detailed blog is at [LeetCode](https://www.wolai.com/tony5t4rk/6dxxdnKmbu3rpFuKtFyGvj).

## Problem List

'''


class Problem:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return 'Problem:{title:' + str(self.title) + ' url:' + str(self.url) + '}'


problems = []


def add_file(path):
    full_filename = path.split(os.sep)[-1]
    filename, ext = '.'.join(full_filename.split('.')[:-1]), full_filename.split('.')[-1]

    title = filename[filename.find('(')+1:filename.rfind(')')]
    # url = github_url + '/'.join(path.split(os.sep)[1:])
    url = path[path.find(os.sep) + 1:].replace('(', '%28').replace(')', '%29').replace(' ', '%20')

    problems.append(Problem(title, url))


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
        readme.write('[{}]({})\n\n'.format(problem.title, problem.url))
    readme.close()


daily_path = os.path.join('.', 'daily')

search_file(daily_path)
write_readme(readme_file)
