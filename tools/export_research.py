"""Read only reviewed aggregate CSVs;no research imports or private node inputs. Review public diff before publishing."""
from pathlib import Path
import csv,json,hashlib,statistics,html,re
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--source-root',type=Path,required=True);args=parser.parse_args()
S=args.source_root.resolve();P=Path(__file__).resolve().parents[1];R=P/'research'
def rows(name):return list(csv.DictReader((S/name).read_text(encoding='utf-8-sig').splitlines()))
base='reports/three_agent_cross_dataset_experiment/'
sources=[base+n for n in ['evaluation_comparison.csv','evaluation_seeds.csv','evaluation_classwise.csv','evaluation_confusion.csv','evaluation_independent_readback.json']]+['reports/sara_core_final_comparison.csv','reports/sara_core_final_seeds.csv']
data={'schema':'sara.public.aggregate.v1','date':'2026-11-18','freeze':'1d25c944a6d74a8a15643fa28218e5f0259b844365e33c455e3bbeced4bb62c1','sources':[{'path':n,'sha256':hashlib.sha256((S/n).read_bytes()).hexdigest()} for n in sources],'studies':[]}
names={'A':'B1','B':'Narrative','C':'No-Agent Fusion','D':'Three-Agent R0 + P1','E':'Matched-mask Narrative'}
for dataset,size in [('PubMed60',60),('CiteSeer120',120),('Cora R1',140)]:
 arms=[]
 for r in rows(base+'evaluation_comparison.csv') if dataset!='Cora R1' else rows('reports/sara_core_final_comparison.csv'):
  if dataset!='Cora R1' and r['dataset']!=dataset:continue
  aid=r.get('arm',r.get('Arm'));seedrows=[s for s in rows(base+'evaluation_seeds.csv' if dataset!='Cora R1' else 'reports/sara_core_final_seeds.csv') if s.get('arm',s.get('Arm'))==aid and (dataset=='Cora R1' or s['dataset']==dataset)]
  ss=[{'seed':int(s.get('seed',s.get('Seed'))),'accuracy':float(s['Accuracy']),'f1':float(s.get('Macro_F1',s.get('Macro-F1')))} for s in seedrows];ss.sort(key=lambda s:s['seed']);assert [s['seed'] for s in ss]==list(range(10))
  accuracy=float(r['Accuracy']);sd=float(r.get('Accuracy_population_SD',r.get('Accuracy_SD')));assert abs(statistics.mean(s['accuracy'] for s in ss)-accuracy)<1e-9;assert abs(statistics.pstdev(s['accuracy'] for s in ss)-sd)<1e-9
  arms.append({'id':aid,'name':names[aid] if dataset!='Cora R1' else r['Method'],'train':int(r.get('train_count',r.get('Train'))),'accuracy':accuracy,'sd':sd,'f1':float(r.get('Macro_F1',r.get('Macro-F1'))),'f1SD':float(r.get('Macro_F1_population_SD',r.get('Macro-F1_SD'))),'seeds':ss})
 classes=[]
 if dataset!='Cora R1':
  cr=rows(base+'evaluation_classwise.csv');classes=list(dict.fromkeys(r['class_name'] for r in cr if r['dataset']==dataset))
  for a in arms:
   a['classwise']=[{'name':c,'recall':statistics.mean(float(r['recall']) for r in cr if r['dataset']==dataset and r['arm']==a['id'] and r['class_name']==c)} for c in classes]
   cm=rows(base+'evaluation_confusion.csv');a['confusion']=[[sum(int(r['count']) for r in cm if r['dataset']==dataset and r['arm']==a['id'] and int(r['true_class'])==i and int(r['predicted_class'])==j)/10 for j in range(len(classes))] for i in range(len(classes))]
 data['studies'].append({'id':dataset,'size':size,'contract':'Historical R1; CE/noPS; LR0.005; test2568' if dataset=='Cora R1' else 'Final R0 referral + P1 fusion; fixed full-cohort test complement; ten matched GCN seeds','classes':classes,'arms':arms})
(R/'results.json').write_bytes((json.dumps(data,indent=2)+'\n').encode('utf-8'))
