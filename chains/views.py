from django.shortcuts import render
import glob
import os
import json

CHAIN_PATH = '/Users/sneha/Documents/dev/narrate.ai/narratives/output/chains_dj_wapo/'
files = glob.glob(os.path.join(CHAIN_PATH, '*.json'))
# Create your views here.


def index(request):
    if request.method == 'GET':
        story_ids = []
        for c_file in files:
           story_ids.append(c_file.split('/')[-1].split('.')[0])

        return render(request, 'chains/index.html', {'story_ids': story_ids})


def view_chain(request, story_id):
    if request.method == 'GET':
        with open(os.path.join(CHAIN_PATH, '{}.json'.format(story_id)), 'r') as f:
            chains = json.load(f)
        if not chains:
            return render(request, 'No chains found!')
        flattened_chains = []
        for chain in chains:
            flattened_chains.append('\n'.join(['Q: {}, A:{}'.format(q_a[1], q_a[2]) for q_a in chain]))
        return render(request, 'chains/chain.html', {'chains': flattened_chains})
