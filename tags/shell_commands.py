from tags.models import Tag

Tag.objects.all()
#<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>

Tag.objects.last()
#<Tag: Black>

black = Tag.objects.last()
black.title
'Black'
black.slug
'black'
black.active
True
black.products
#<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x10c2f3da0>
black.products.all()
#<ProductQuerySet [<Product: T-Shirt>, <Product: Hat>, <Product: T-Shirt>]>
black.products.all().first()
#<Product: T-Shirt>
exit()

from products.models import Product
qs = Product.objects.all()
qs
#<ProductQuerySet [<Product: T-Shirt>, <Product: Hat>, <Product: Supercomputer>, <Product: T-Shirt>, <Product: Lorem Ipsum>]>
tshirt = qs.first()
tshirt
#<Product: T-Shirt>
tshirt.description()

tshirt.description
'This is a t-shirt. Buy it :)'

tshirt.tag_set.all()
#<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>