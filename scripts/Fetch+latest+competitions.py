
# coding: utf-8

# In[29]:

import requests
import yaml


# In[30]:

base_url = 'https://www.kaggle.com/competitions.json?sortBy=latestDeadline&group=general&page=1&pageSize=20&category=featured'

r = requests.get(base_url)
competitions = r.json()['pagedCompetitionGroup']['competitions']


# In[31]:

keys = ['competitionId', 'competitionName', 'competitionTitle', 'competitionDescription', 'competitionUrl', 'coverImageUrl', 'thumbnailImageUrl', 'deadline', 
        'rewardQuantity', 'rewardTypeName', 'organizationName', 'organizationUrl', 'organizationAvatarUrl', 'hostSegment',  'evaluationMetric','categories',]

to_print = []
for competition in competitions:
    to_print.append({k:competition[k] for k in keys})
print(yaml.safe_dump(to_print, default_flow_style=False))


# In[ ]:



