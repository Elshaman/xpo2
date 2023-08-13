from . import products

@products.route('/')
def index():
    return "modeulo de productos"