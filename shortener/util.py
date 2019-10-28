import random
import string

def code_generator(size = 6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size = 6):
    newcode = code_generator(size = size)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__
    qs = Klass.objects.filter(shortcode=newcode).exists()
    if qs:
        return create_shortcode(size=size)
    return newcode