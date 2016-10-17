import os
import shutil


target = [
    '.ssh/config',
    '.ssh/keys',
    '.zshrc',
    '.gitconfig'
]


def mkdir(path):
    if os.path.exists(os.path.dirname(path)):
        os.mkdir(path)
    else:
        mkdir(os.path.dirname(path))


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    home_dir = os.path.expanduser('~')

    target_table = {}

    for t in target:
        target_table[t] = {'src': current_dir + '/' + t, 'dst': home_dir + '/' + t}

    for k, v in target_table.items():
        if os.path.lexists(v['dst']):
            print(v['dst'] + ' already exists.\nOverwrite (y/n)? ', end='')
            if input().strip() in ['y', 'Y']:
                if os.path.isfile(v['dst']) and not os.path.islink(v['dst']):
                    os.remove(v['dst'])
                elif os.path.isdir(v['dst']) and not os.path.islink(v['dst']):
                    shutil.rmtree(v['dst'])
                elif os.path.islink(v['dst']):
                    os.unlink(v['dst'])
            else:
                continue

        if not os.path.exists(os.path.dirname(v['dst'])):
            mkdir(os.path.dirname(v['dst']))

        print(v['dst'] + ' -> ' + v['src'])
        os.symlink(v['src'], v['dst'])


if __name__ == '__main__':
    main()
