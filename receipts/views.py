from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm


# Create your views here.
@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


def category_list(request):
    categories = ExpenseCategory.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "receipts/category_list.html", context)


def account_list(request):
    accounts = Account.objects.all()
    context = {
        "accounts": accounts,
    }
    return render(request, "receipts/account_list.html", context)
