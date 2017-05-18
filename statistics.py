import sys
import json
import operator

overall_dict = {
    'country': {},
    'age': {
        'under 20': 0,
        '20-30': 0,
        '30-40': 0,
        '40-50': 0,
        '50-60': 0,
        '60-70': 0,
        '70-80': 0,
        '80-90': 0,
        '90-100': 0,
        'over 100': 0
    },
    'gender': {},
    'industry': {}
}

year = sys.argv[1]

with open('./static/data/raw_data/' + year + '.json') as f:
    raw_data = f.read()
    billionaires = json.loads(raw_data)
    print('billionaires count: ' + str(len(billionaires)))
    for billionaire in billionaires:
        for key in overall_dict:
            try:
                if key == 'age':
                    if billionaire[key] < 20:
                        overall_dict['age']['under 20'] += 1
                    elif billionaire[key] >= 20 and billionaire[key] < 30:
                        overall_dict['age']['20-30'] += 1
                    elif billionaire[key] >= 30 and billionaire[key] < 40:
                        overall_dict['age']['30-40'] += 1
                    elif billionaire[key] >= 40 and billionaire[key] < 50:
                        overall_dict['age']['40-50'] += 1                        
                    elif billionaire[key] >= 50 and billionaire[key] < 60:
                        overall_dict['age']['50-60'] += 1
                    elif billionaire[key] >= 60 and billionaire[key] < 70:
                        overall_dict['age']['60-70'] += 1
                    elif billionaire[key] >= 70 and billionaire[key] < 80:
                        overall_dict['age']['70-80'] += 1
                    elif billionaire[key] >= 80 and billionaire[key] < 90:
                        overall_dict['age']['80-90'] += 1                        
                    elif billionaire[key] >= 90 and billionaire[key] < 100:
                        overall_dict['age']['90-100'] += 1
                    elif billionaire[key] > 100:
                        overall_dict['age']['over 100'] += 1
                else:
                    if billionaire[key] not in overall_dict[key]:
                        overall_dict[key][billionaire[key]] = 1
                    else:
                        overall_dict[key][billionaire[key]] += 1     
            except:
                pass

for key in overall_dict:
    overall_dict[key] = sorted(overall_dict[key].items(), key=operator.itemgetter(1), reverse=True)
print(overall_dict)