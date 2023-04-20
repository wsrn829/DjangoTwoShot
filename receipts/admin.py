from django.contrib import admin
from receipts.models import ExpenseCategory, Receipt, Account


# Register your models here.
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )


@admin.register(Receipt)
class ReceiptCategory(admin.ModelAdmin):
    list_display = (
        "vendor",
        "total",
        "tax",
        "date",
        "purchaser",
        "category",
        "account",
    )


@admin.register(Account)
class AccountCategory(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "owner",
    )
