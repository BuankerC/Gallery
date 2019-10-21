from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardForm, CommentForm
from .models import Board, Comment
# Create your views here.


def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/index.html', context)


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('board:index')
    else:
        form = BoardForm()

    context = {
        'form': form
    }
    return render(request, 'board/form.html', context)


def detail(request, id):
    board = get_object_or_404(Board, id=id)
    comment_form = CommentForm()
    context = {
        'board': board,
        'comment_form': comment_form
    }
    return render(request, 'board/detail.html', context)


def delete(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == "POST":
        board.delete()
        return redirect('board:index')


def update(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('board:detail', id)
    else:
        form = BoardForm(instance=board)
    context = {
        'form': form
    }
    return render(request, 'board/form.html', context)


def comment_create(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.board = board
            comment.user = request.user
            comment.save()
            return redirect('board:detail', board_id)


def comment_delete(request, board_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('board:detail', board_id)
