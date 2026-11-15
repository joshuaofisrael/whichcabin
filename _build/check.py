#!/usr/bin/env python3
"""Site QA: JSON-LD parses, legal line on legal pages, no owner/LLC name outside legal pages, broken internal links, duplicate titles, one h1,
canonical on whichcabin.com, beacon present (launch) / noindex present (preview). Usage: check.py [--launch]"""
import glob,re,json,os,sys,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); LAUNCH="--launch" in sys.argv; PREFIX="" if LAUNCH else "/whichcabin"
LEGAL={'terms','privacy','disclaimer','copyright','ad-disclosure'}
bad=0;titles={}
files=[f for f in glob.glob(ROOT+'/**/*.html',recursive=True) if '/_build/' not in f]
for f in files:
    h=open(f).read(); rel=os.path.relpath(f,ROOT); top=rel.split('/')[0]
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',h):
        try: json.loads(m)
        except Exception as e: print('JSONLD',rel,e); bad+=1
    vis=re.sub(r'<script.*?</script>','',h,flags=re.S)
    if top not in LEGAL and re.search(r'Joshua|Israel Ventures|©',vis): print('LLC/©',rel); bad+=1
    if top in LEGAL and 'is a trade name of Joshua Israel Ventures LLC' not in h: print('nolegalline',rel); bad+=1
    if not re.search(r'<link rel="canonical" href="https://whichcabin.com/',h): print('canonical',rel); bad+=1
    if h.count('<h1')!=1: print('h1count',rel,h.count('<h1')); bad+=1
    if LAUNCH:
        if 'static.cloudflareinsights.com/beacon.min.js' not in h: print('nobeacon',rel); bad+=1
        if 'noindex' in h and rel!='404.html': print('noindex',rel); bad+=1
    elif 'noindex' not in h: print('preview-missing-noindex',rel); bad+=1
    if '—' in h or '–' in h: print('dash',rel)
    t=re.search(r'<title>(.*?)</title>',h).group(1); titles.setdefault(t,[]).append(rel)
    for l in re.findall(r'(?:href|src)="(/[^"#?]*)',h):
        if not l.startswith(PREFIX+'/') and l!=PREFIX+'/': print('prefix',rel,l); bad+=1; continue
        p=os.path.join(ROOT,l[len(PREFIX):].lstrip('/'))
        if not (os.path.isfile(p) or os.path.isfile(os.path.join(p,'index.html'))): print('broken',rel,l); bad+=1
for t,fs in titles.items():
    if len(fs)>1: print('duptitle',t,fs); bad+=1
    if len(html.unescape(t))>70: print('longtitle',len(html.unescape(t)),t)
print('files',len(files),'issues',bad); sys.exit(1 if bad else 0)
