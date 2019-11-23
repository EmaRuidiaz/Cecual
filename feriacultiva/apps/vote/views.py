from django.shortcuts import render
from apps.vote.models import Vote
from apps.comentario.models import Comentario
from apps.tema.models import Tema
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Votar(request, pk):

	context = {}
	tema = Comentario.objects.get(pk = pk)
	p = Tema.objects.get(pk = tema.foro.pk)
	x = Comentario.objects.filter(foro = p)
	context['comentario'] = x

	try:
		check = Vote.objects.get(user = request.user, comentario = pk)
	except Exception as e:
		check = None

	if check:
		if check.vote == "1":
			Vote.objects.update(vote = "-1")
		else:
			Vote.objects.update(vote = "1")
		
	else:
		Vote.objects.create(user = request.user, comentario = Comentario.objects.get(pk = pk), vote = "1")


	votes = Vote.objects.filter(user = request.user, vote = "1")
	VotesListPositives = []
	for p in votes:
		VotesListPositives.append(p.pk)
	context['votes'] = VotesListPositives

	context['positives'] = len(VotesListPositives)

	neg = Vote.objects.filter(user = request.user, vote = "-1")
	context['negatives'] = len(neg)

	return render(request,'Foro/comentario.html',context)