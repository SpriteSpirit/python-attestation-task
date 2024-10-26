from django.contrib import admin
from .models import NetworkNode, Product, Supplier, ContactInfo


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'supplier', 'get_products', 'debt', )
    list_filter = ('name', 'supplier', 'debt', 'level', )
    search_fields = ('name' 'supplier', 'debt', )
    ordering = ('-name',)

    actions = ('clear_debt',)

    @admin.action(description='Очистить задолженность')
    def clear_debt(self, request, queryset):
        count = queryset.update(debt=0)
        self.message_user(request, f'{count} запись успешно обновлена.')

    def get_products(self, obj):
        # Возвращает строку с названиями всех продуктов, связанных с данной сетью
        return ", ".join([product.name for product in obj.products.all()]) if obj.products.exists() else "Нет товаров"

    get_products.short_description = 'Товары'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier', )
    list_filter = ('name', 'model', 'release_date', 'supplier', )
    search_fields = ('name' 'model', 'supplier', )
    ordering = ('-name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'created_at', )
    list_filter = ('name', 'contact_info', 'created_at', )
    search_fields = ('name' 'contact_info', 'created_at', )
    ordering = ('-name',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number', )
    list_filter = ('email', 'country', 'city', )
    search_fields = ('email' 'country', 'city', )
    ordering = ('-email',)
