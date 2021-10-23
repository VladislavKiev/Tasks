"""
2) Write a function that takes a filename and outputs its extension. If the file extension cannot be determined, throw an exception.
        Call example
            get_ext ('text.txt') => 'txt'
            get_ext ('. git') => 'git'
            get_ext ('somefile.txt.log') => 'log'
            get_ext ('script.py') => 'py'
            get_ext ('script.py.') => ValueErorr
"""


def extension(fn):
    filename = fn.split('.')
    if len(filename) < 2:
        return False
    first, *middle, last = filename
    if not last or not first and not middle:
        return False
    return filename[-1]


print(extension('text.txt'))
print(extension('. git'))
print(extension('somefile.txt.log'))
print(extension('script.py'))
print(extension('aaaa'))
print(extension('afdasf.asdffs.'))
