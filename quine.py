import time


# x = "%d"
# y = 42
# print(x%y)
# 42

def almost_quine():
    # %r calls the __repr__ method that returns a printable representation of
    # the object passed
    s='test %r';print(s%s)


def quine():
    s='s=%r;print(s%%s)';print(s%s)

def intron():
    t='';s='t=input()or t;print(f"t={repr(t)};s={repr(s)};exec(s)#{t}")';exec(s)#

def lambda_quine():
    print((lambda s: s % s)('print((lambda s:s%%s)(%r))'))

def infinite_exec():
    s = 's=%r;print("hello");time.sleep(1);exec(s%%s)';
    exec(s % s)

if __name__ == '__main__':
    # quine()
    # intron()
    # lambda_quine()
    infinite_exec()