from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction, SavingsGoal
from .forms import TransactionForm, SavingsGoalForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth import logout

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'tracker_app/dashboard.html', {
        "transactions": transactions,
        "goals": goals,
    })

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker_app/add_transaction.html', {'form': form})

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'tracker_app/edit_transaction.html', {'form': form})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('dashboard')
    return render(request, 'tracker_app/delete_transaction.html', {'transaction': transaction})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = SavingsGoalForm()
    return render(request, 'tracker_app/add_goal.html', {'form': form})

@login_required
def edit_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id, user=request.user)
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SavingsGoalForm(instance=goal)
    return render(request, 'tracker_app/edit_goal.html', {'form': form})

@login_required
def delete_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('dashboard')
    return render(request, 'tracker_app/delete_goal.html', {'goal': goal})

def logout_view(request):
    logout(request)
    return redirect('login')
