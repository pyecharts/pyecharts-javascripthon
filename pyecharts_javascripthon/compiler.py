import io
import sys
import codecs
import inspect
import subprocess

PY2 = sys.version_info[0] == 2


class Python2Javascript:
    @staticmethod
    def translate(obj):
        source_codes = inspect.getsourcelines(obj)
        shell_flag = sys.platform == 'win32'
        with codecs.open('tmp.py', 'w', 'utf-8') as f:
            print(source_codes)
            f.write(''.join(source_codes[0]))

        proc_params = [
            'pj',
            'tmp.py'
        ]

        proc = subprocess.Popen(
            proc_params, stdout=subprocess.PIPE, shell=shell_flag)
        if PY2:
            proc.stdout.read()
        else:
            io.TextIOWrapper(proc.stdout, encoding="utf-8").read()
        with codecs.open('tmp.js', 'r', 'utf-8') as f:
            content = f.read()
        return content
