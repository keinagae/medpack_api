from django.contrib import admin
from nested_admin.nested import NestedModelAdmin,NestedStackedInline
from .models import Product, Variant, VariantAttribute, VariantAttributeValues



class InlineVariantAttributeValuesAdmin(NestedStackedInline):
    list_display = ('id', 'attribute', 'value')
    list_filter = ('attribute',)
    model = VariantAttributeValues
    extra=1

class InlineVariantAttributeAdmin(NestedStackedInline):
    list_display = ('id', 'variant', 'name',)
    list_filter = ('variant',)
    search_fields = ('name',)
    model = VariantAttribute
    inlines = [
        InlineVariantAttributeValuesAdmin
    ]
    extra=1


class InlineVariantAdmin(NestedStackedInline):
    list_display = ('id', 'product', 'name')
    list_filter = ('product',)
    search_fields = ('name',)
    model = Variant
    inlines = [
        InlineVariantAttributeAdmin
    ]
    extra=1


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'image',
        'expiry_date',
        'quantity',
        'provider',
    )

    list_filter = ('expiry_date', 'provider')
    search_fields = ('name',)
#
#
# @admin.register(Variant)
# class VariantAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'name')
#     list_filter = ('product',)
#     search_fields = ('name',)


# @admin.register(VariantAttribute)
# class VariantAttributeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'variant', 'name', )
#     list_filter = ('variant',)
#     search_fields = ('name',)
#
#
# @admin.register(VariantAttributeValues)
# class VariantAttributeValuesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'attribute', 'value')
#     list_filter = ('attribute',)
