from django.shortcuts import render
import glob
import os
import json
from collections import defaultdict

from chains.models import Story, Chain


# Create your views here.


def index(request):
    # if request.method == 'GET':
    publishers = dict()
    for ch in Chain.objects.all():
        if ch.story_id.publisher not in publishers:
            publishers[ch.story_id.publisher] = []
        publishers[ch.story_id.publisher].append(ch.story_id.id)
    return render(request, 'chains/index.html', {'publishers': publishers})


def view_chain(request, story_id):
    # if request.method == 'GET':
    chains = eval(Chain.objects.get(story_id=story_id).chains)
    flattened_chains = []
    story = Story.objects.get(id=story_id)
    raw_text = story.text
    publisher = story.publisher
    country = story.country
    for chain in chains:
        flattened_chains.append([(q_a[1], q_a[2]) for q_a in chain])
    return render(request, 'chains/chain.html', {'chains': flattened_chains, 'text': raw_text,
                                                 'publisher': publisher, 'country': country})
