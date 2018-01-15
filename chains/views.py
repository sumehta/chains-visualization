from django.shortcuts import render
import glob
import os
import json
from collections import defaultdict

from chains.models import Story, Chain, Clause, Question, Sentence


def index(request):
    if request.method == 'GET':
        publishers = dict()
        for ch in Chain.objects.all():
            if ch.story.publisher not in publishers:
                publishers[ch.story.publisher] = []
            publishers[ch.story.publisher].append(ch.story.id)
        return render(request, 'chains/index.html', {'publishers': publishers})


def view_chain(request, story_id):
    if request.method == 'GET':
        chains = eval(Chain.objects.get(story_id=story_id).chains)

        flattened_chains = []
        story = Story.objects.get(id=story_id)
        raw_text = story.text
        publisher = story.publisher
        country = story.country
        for chain in chains:
            flattened_chains.append([(q_a[1], q_a[2]) for q_a in chain])
        return render(request, 'chains/chain.html', {'chains': flattened_chains, 'text': raw_text,
                                                     'publisher': publisher, 'country': country, 'story_id': story_id})


def get_details(request, story_id):
    if request.method == 'GET':
        sentences = eval(Sentence.objects.get(story=story_id).sentences)
        questions = eval(Question.objects.get(story=story_id).questions)

        clauses = defaultdict(list)
        cl = Clause.objects.get(story=story_id)
        clauses_raw = eval(cl.clauses)
        for line in clauses_raw:
            tokens = line.strip('\n').split('\t')
            sent_no, clause = int(tokens[0]), ' '.join([tok[1:-1] for tok in tokens])
            clauses[sent_no].append(clause)

        sent_clause_questions = defaultdict(list)

        for k, v in questions.items():
            sent_clause_questions[int(k)].append((sentences[int(k)], clauses[int(k)], questions[k]))

        return render(request, 'chains/chain_details.html', {'story_id': story_id, 'sent_clause_questions': dict(sent_clause_questions)})
