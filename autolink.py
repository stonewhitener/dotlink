import os
import shutil
import glob


def main():
    targets = glob.glob('.*')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    home_dir = os.path.expanduser('~')

    for target in targets:
        src = f"{current_dir}/{target}"
        dst = f"{home_dir}/{target}"

        if os.path.lexists(dst):
            print(f"{dst} already exists.\nOverwrite (y/N)? ", end='')
            if input().strip() in ['y', 'Y']:
                if os.path.isfile(dst) and not os.path.islink(dst):
                    os.remove(dst)
                elif os.path.isdir(dst) and not os.path.islink(dst):
                    shutil.rmtree(dst)
                elif os.path.islink(dst):
                    os.unlink(dst)
            else:
                continue

        print(f"{dst} -> {src}")
        os.symlink(src, dst)


if __name__ == '__main__':
    main()
