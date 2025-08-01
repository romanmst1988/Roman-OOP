class StripChars:

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return args[0].strip(self.chars)

st1 = StripChars("?")

res = st1("?Example?")

print(res)

res = st1("!SomeExample!")
print(res)