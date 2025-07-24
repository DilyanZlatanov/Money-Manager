from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import redirect, render
from core.forms import TransactionForm


# Create your views here.

def transactions_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'transactions',
                {
                    'type': 'send_transaction',
                    'data': {
                        'type': transaction.type,
                        'amount': transaction.amount,
                        'description': transaction.description,
                        'date': transaction.date.isoformat()
                    }
                }
            )
            return redirect('dashboard')
    else:
        transaction_form = TransactionForm()

    return render(request, 'dashboard.html', {'form': transaction_form})