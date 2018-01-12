from django.core.management import BaseCommand, CommandError
from chains.models import Story, Chain
import json
import glob
import os

PROTEST_PATH = '/Users/sneha/Documents/dev/narrate.ai/narratives/output/protest_events/'
protest_files = glob.glob(os.path.join(PROTEST_PATH, '*.json'))
CHAIN_PATH = '/Users/sneha/Documents/dev/narrate.ai/narratives/output/chains_dj_wapo/'
files = glob.glob(os.path.join(CHAIN_PATH, '*.json'))

class Command(BaseCommand):
    help = 'Run this command to populate db'

    def handle(self, *args, **options):
        # for p_file in protest_files:
        #     with open(p_file, 'r') as f:
        #         for line in f:
        #             data = json.loads(line)
        #             s = Story(id=data['StoryID'], text=data['RawText'],
        #                       publisher=data['Publisher'], event_code=int(data['event_details']['CAMEO Code']),
        #                       country=data['event_details']['Country'])
        #             s.save()
        #             print(data['StoryID'])

        for c_file in files:
            story_id = int(c_file.split('/')[-1].split('.')[0])
            with open(c_file, 'r') as f:
                chains = json.load(f)

            c = Chain(story_id=Story.objects.get(id=story_id), chains=str(chains))
            c.save()

            print(story_id)
