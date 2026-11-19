import json,glob,os
d=os.path.dirname(os.path.abspath(__file__))
units=[]
for f in sorted(glob.glob(d+'/content/unit*.json')):
    units.append(json.load(open(f,encoding='utf-8')))
open(d+'/android/app/src/main/assets/www/data.js','w',encoding='utf-8').write('window.UNITS='+json.dumps(units,ensure_ascii=False)+';')
print(len(units),'units',sum(len(u['terms']) for u in units),'terms',sum(len(u['mcqs']) for u in units),'mcqs')
