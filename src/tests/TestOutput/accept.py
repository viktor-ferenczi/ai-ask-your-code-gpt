import os

for an in os.listdir('.'):
    if an.endswith('.actual.py'):
        en = an.replace('.actual.py', '.expected.py')
        if os.path.exists(en):
            os.remove(en)
        os.rename(an, en)
