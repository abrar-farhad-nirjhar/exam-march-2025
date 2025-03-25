# DRF Implementation:

We have 3 different models:

- Inventory Tag
- Inventory Lang
- Inventory

For each of them we need to make sure we have a restframework serializer. But while writing the serializer we need to make sure about the requirements, do we need nested serialization or just ID is fine. Based on that we create the serializer.

Then we need to create a view. When creating views django provides us with a lot of options, viewsets, mixins, generic views.

But for this we can use a CreateAPIView from restframework.generics and complete it. Within the view you need to set the serializer_class, and the queryset.

Now set up the urls so that this view can be accessed.

Now based on how you setup your serializer, make a request with the required data and it should work.
