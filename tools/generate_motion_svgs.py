import sys
OUT=sys.argv[1]
STD='cubic-bezier(.2,0,0,1)'; DEC='cubic-bezier(.05,.7,.1,1)'; ACC='cubic-bezier(.3,0,.8,.15)'; LIN='linear'
FONT="Roboto,'Segoe UI',system-ui,sans-serif"
PRI='#6750A4'; PC='#EADDFF'; SC='#E8DEF8'; SURF='#FEF7FF'; OUTL='#79747E'; ONS='#1D1B20'; ONSV='#49454F'

def kf(name,frames):
    return "@keyframes %s{%s}"%(name,"".join("%s%%{%s}"%(p,c) for p,c in frames))
class Doc:
    def __init__(s,h): s.css=[];s.body=[];s.h=h;s.n=0
    def anim(s,frames,dur=4,timing=STD,delay=0,extra=''):
        s.n+=1;nm='k%d'%s.n
        s.css.append(kf(nm,frames))
        return 'style="animation:%s %ss %s %ss infinite;%s"'%(nm,dur,timing,delay,extra)
    def panel(s,x,y,title,sub,stage):
        s.body.append('<g transform="translate(%d,%d)"><rect width="290" height="200" rx="24" fill="%s" stroke="#E7E0EC"/>%s<text x="145" y="172" text-anchor="middle" font-size="14" font-weight="500" fill="%s">%s</text><text x="145" y="190" text-anchor="middle" font-size="11" fill="%s">%s</text></g>'%(x,y,SURF,stage,ONS,title,ONSV,sub))
    def write(s,fn,footer):
        svg='<svg xmlns="http://www.w3.org/2000/svg" width="960" height="%d" viewBox="0 0 960 %d" font-family="%s">'%(s.h,s.h,FONT)
        svg+='<style>.t{transform-box:fill-box;transform-origin:center}.tl{transform-box:fill-box;transform-origin:0 50%%}.tt{transform-box:fill-box;transform-origin:0 0}%s</style>'%"".join(s.css)
        svg+='<defs><filter id="bl" x="-20%%" y="-20%%" width="140%%" height="150%%"><feGaussianBlur stdDeviation="3"/></filter></defs>'
        svg+='<rect width="960" height="%d" rx="28" fill="#F7F2FA"/>'%s.h
        svg+="".join(s.body)
        svg+='<text x="480" y="%d" text-anchor="middle" font-size="12" fill="%s">%s</text></svg>'%(s.h-16,ONSV,footer)
        open(OUT+'/'+fn,'w').write(svg)
def phone(inner,w=150,h=130,lines=True):
    l=''
    if lines:
        l='<rect x="12" y="14" width="70" height="8" rx="4" fill="#E7E0EC"/><rect x="12" y="30" width="126" height="6" rx="3" fill="#EFE9F3"/><rect x="12" y="42" width="110" height="6" rx="3" fill="#EFE9F3"/><rect x="12" y="54" width="118" height="6" rx="3" fill="#EFE9F3"/>'
    return '<g transform="translate(70,12)"><rect width="%d" height="%d" rx="14" fill="#fff" stroke="#CAC4D0"/>%s%s</g>'%(w,h,l,inner)
X=[30,335,640]; Y=[30,245]
def onoff(on,off,d=6):
    # frames helper: list of (pct,state) -> transitions
    pass

# ---------- FILE 1: controls ----------
d=Doc(495)
# A button
ov=d.anim([(0,'opacity:0'),(10,'opacity:0'),(17,'opacity:.08'),(36,'opacity:.08'),(37,'opacity:.1'),(58,'opacity:.1'),(65,'opacity:.08'),(82,'opacity:.08'),(90,'opacity:0'),(100,'opacity:0')],timing=LIN)
rp=d.anim([(0,'transform:scale(0);opacity:0'),(36,'transform:scale(0);opacity:0'),(37,'transform:scale(0);opacity:.2'),(58,'transform:scale(1);opacity:.14'),(70,'transform:scale(1);opacity:0'),(100,'transform:scale(1);opacity:0')],timing=STD)
st='<clipPath id="bc"><rect width="140" height="44" rx="22"/></clipPath><g transform="translate(75,52)"><rect width="140" height="44" rx="22" fill="%s"/><rect class="t" width="140" height="44" rx="22" fill="#fff" %s/><g clip-path="url(#bc)"><circle class="t" cx="70" cy="22" r="100" fill="#fff" %s/></g><text x="70" y="27" text-anchor="middle" font-size="14" font-weight="500" fill="#fff">Button</text></g>'%(PRI,ov,rp)
d.panel(X[0],Y[0],'Button','hover .08 → pressed .10 + ripple · short2–medium2',st)
# B switch
tr=d.anim([(0,'fill:#E6E0E9;stroke:#79747E'),(22,'fill:#E6E0E9;stroke:#79747E'),(36,'fill:#6750A4;stroke:#6750A4'),(62,'fill:#6750A4;stroke:#6750A4'),(78,'fill:#E6E0E9;stroke:#79747E'),(100,'fill:#E6E0E9;stroke:#79747E')],timing=STD)
hd=d.anim([(0,'transform:translateX(0) scale(1);fill:#79747E'),(12,'transform:translateX(0) scale(1);fill:#79747E;animation-timing-function:%s'%STD),(19,'transform:translateX(0) scale(1.75);fill:#79747E;animation-timing-function:cubic-bezier(.34,1.4,.64,1)'),(40,'transform:translateX(20px) scale(1.5);fill:#fff'),(62,'transform:translateX(20px) scale(1.5);fill:#fff;animation-timing-function:%s'%STD),(68,'transform:translateX(20px) scale(1.75);fill:#fff;animation-timing-function:cubic-bezier(.34,1.4,.64,1)'),(88,'transform:translateX(0) scale(1);fill:#79747E'),(100,'transform:translateX(0) scale(1);fill:#79747E')],timing=STD)
st='<g transform="translate(101,47) scale(1.7)"><rect x="1" y="1" width="50" height="30" rx="15" stroke-width="2" %s/><circle class="t" cx="16" cy="16" r="8" %s/></g>'%(tr,hd)
d.panel(X[1],Y[0],'Switch','handle 16 → 28 pressed → 24 · spatial spring',st)
# C checkbox
box=d.anim([(0,'fill:transparent;stroke:#49454F'),(20,'fill:transparent;stroke:#49454F'),(32,'fill:#6750A4;stroke:#6750A4'),(62,'fill:#6750A4;stroke:#6750A4'),(76,'fill:transparent;stroke:#49454F'),(100,'fill:transparent;stroke:#49454F')])
chk=d.anim([(0,'stroke-dashoffset:14'),(26,'stroke-dashoffset:14'),(38,'stroke-dashoffset:0'),(62,'stroke-dashoffset:0'),(72,'stroke-dashoffset:14'),(100,'stroke-dashoffset:14')])
lay=d.anim([(0,'opacity:0'),(8,'opacity:0'),(14,'opacity:.1'),(34,'opacity:.1'),(40,'opacity:0'),(56,'opacity:0'),(60,'opacity:.1'),(76,'opacity:.1'),(82,'opacity:0'),(100,'opacity:0')],timing=LIN)
st='<g transform="translate(125,48) scale(2.2)"><circle cx="9" cy="9" r="20" fill="%s" %s/><rect x="1" y="1" width="16" height="16" rx="2" stroke-width="2" %s/><path d="M4.5 9.5 L7.5 12.5 L13.5 5.5" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="14" %s/></g>'%(PRI,lay,box,chk)
d.panel(X[2],Y[0],'Checkbox','18dp box · 40dp state layer · check draws in · short4',st)
# D chip
bg=d.anim([(0,'opacity:0'),(25,'opacity:0'),(44,'opacity:1'),(66,'opacity:1'),(82,'opacity:0'),(100,'opacity:0')])
ck=d.anim([(0,'opacity:0'),(30,'opacity:0'),(44,'opacity:1'),(66,'opacity:1'),(78,'opacity:0'),(100,'opacity:0')])
lb=d.anim([(0,'transform:translateX(0)'),(25,'transform:translateX(0)'),(44,'transform:translateX(18px)'),(66,'transform:translateX(18px)'),(82,'transform:translateX(0)'),(100,'transform:translateX(0)')])
bo=d.anim([(0,'stroke-opacity:1'),(25,'stroke-opacity:1'),(44,'stroke-opacity:0'),(66,'stroke-opacity:0'),(82,'stroke-opacity:1'),(100,'stroke-opacity:1')])
st='<g transform="translate(85,56)"><rect x=".5" y=".5" width="119" height="31" rx="8" fill="none" stroke="%s" %s/><rect width="120" height="32" rx="8" fill="%s" %s/><path d="M11 16 L15 20 L22 11" fill="none" stroke="#4A4458" stroke-width="2" %s/><text x="16" y="21" font-size="14" font-weight="500" fill="#1D192B" %s>Filter</text></g>'%(OUTL,bo,SC,bg,ck,lb)
d.panel(X[0],Y[1],'Filter chip','32dp · radius 8 · label shifts, check fades in · medium1',st)
# E slider
act=d.anim([(0,'transform:scaleX(.2)'),(15,'transform:scaleX(.2)'),(45,'transform:scaleX(.65)'),(70,'transform:scaleX(.65)'),(95,'transform:scaleX(.2)'),(100,'transform:scaleX(.2)')])
hdl=d.anim([(0,'transform:translateX(40px)'),(15,'transform:translateX(40px)'),(45,'transform:translateX(130px)'),(70,'transform:translateX(130px)'),(95,'transform:translateX(40px)'),(100,'transform:translateX(40px)')])
hal=d.anim([(0,'opacity:0'),(12,'opacity:0'),(18,'opacity:.14'),(48,'opacity:.14'),(54,'opacity:0'),(100,'opacity:0')],timing=LIN)
st='<g transform="translate(45,75)"><rect y="-2" width="200" height="4" rx="2" fill="#E7E0EC"/><rect class="tl" y="-2" width="200" height="4" rx="2" fill="%s" %s/><g %s><circle r="20" fill="%s" %s/><circle r="10" fill="%s"/></g></g>'%(PRI,act,hdl,PRI,hal,PRI)
d.panel(X[1],Y[1],'Slider','track 4dp · handle 20dp · state layer 40dp',st)
# F text field
bd=d.anim([(0,'stroke:#79747E;stroke-width:1'),(10,'stroke:#79747E;stroke-width:1'),(26,'stroke:#6750A4;stroke-width:2'),(70,'stroke:#6750A4;stroke-width:2'),(84,'stroke:#79747E;stroke-width:1'),(100,'stroke:#79747E;stroke-width:1')])
lab=d.anim([(0,'transform:translateY(0) scale(1);fill:#49454F'),(10,'transform:translateY(0) scale(1);fill:#49454F'),(26,'transform:translateY(-30px) scale(.75);fill:#6750A4'),(70,'transform:translateY(-30px) scale(.75);fill:#6750A4'),(84,'transform:translateY(0) scale(1);fill:#49454F'),(100,'transform:translateY(0) scale(1);fill:#49454F')])
gap=d.anim([(0,'opacity:0'),(10,'opacity:0'),(26,'opacity:1'),(70,'opacity:1'),(84,'opacity:0'),(100,'opacity:0')])
inp=d.anim([(0,'opacity:0'),(30,'opacity:0'),(40,'opacity:1'),(66,'opacity:1'),(74,'opacity:0'),(100,'opacity:0')],timing=LIN)
st='<g transform="translate(45,40)"><rect x="1" y="1" width="198" height="54" rx="4" fill="none" %s/><rect x="8" y="-3" width="46" height="8" fill="%s" %s/><text class="tl" x="16" y="34" font-size="16" %s>Label</text><text x="16" y="36" font-size="16" fill="%s" %s>Hello</text></g>'%(bd,SURF,gap,lab,ONS,inp)
d.panel(X[2],Y[1],'Outlined text field','label 16→12sp · outline 1→2dp · medium1',st)
d.write('motion-controls.svg','Shown in ~3× slow motion so the easing is visible. Real durations are in the reference table.')

# ---------- FILE 2: surfaces ----------
d=Doc(495)
# A dialog
scr=d.anim([(0,'opacity:0'),(8,'opacity:0'),(34,'opacity:.32'),(66,'opacity:.32'),(81,'opacity:0'),(100,'opacity:0')],timing=LIN)
dlg=d.anim([(0,'opacity:0;transform:scale(.8)'),(8,'opacity:0;transform:scale(.8);animation-timing-function:%s'%DEC),(34,'opacity:1;transform:scale(1)'),(66,'opacity:1;transform:scale(1);animation-timing-function:%s'%ACC),(81,'opacity:0;transform:scale(.9)'),(100,'opacity:0;transform:scale(.8)')])
inner='<rect width="150" height="130" rx="14" fill="#000" %s/><g class="t" %s><rect x="15" y="22" width="120" height="86" rx="28" fill="#ECE6F0"/><rect x="34" y="40" width="58" height="7" rx="3.5" fill="%s"/><rect x="34" y="56" width="82" height="5" rx="2.5" fill="#CAC4D0"/><rect x="34" y="66" width="70" height="5" rx="2.5" fill="#CAC4D0"/><text x="56" y="96" font-size="11" font-weight="500" fill="%s">Cancel</text><text x="104" y="96" font-size="11" font-weight="500" fill="%s">OK</text></g>'%(scr,dlg,ONS,PRI,PRI)
d.panel(X[0],Y[0],'Dialog','radius 28 · scrim .32 · enter 350ms decelerate, exit 200ms',phone(inner))
# B menu
mn=d.anim([(0,'opacity:0;transform:scaleY(.3)'),(10,'opacity:0;transform:scaleY(.3);animation-timing-function:%s'%DEC),(26,'opacity:1;transform:scaleY(1)'),(66,'opacity:1;transform:scaleY(1)'),(74,'opacity:0;transform:scaleY(1)'),(100,'opacity:0;transform:scaleY(.3)')])
items=''
for i,t in enumerate(['Edit','Duplicate','Delete']):
    a=14+4*i
    it=d.anim([(0,'opacity:0'),(a,'opacity:0'),(a+10,'opacity:1'),(66,'opacity:1'),(74,'opacity:0'),(100,'opacity:0')],timing=LIN)
    items+='<text x="16" y="%d" font-size="13" fill="%s" %s>%s</text>'%(36+i*30-2,ONS,it,t)
# simpler clean build (avoid hacks above)
mn2=mn.replace('style="','style="transform-box:fill-box;transform-origin:0 0;')
st='<g transform="translate(70,10)"><rect width="100" height="32" rx="16" fill="none" stroke="%s"/><text x="50" y="21" text-anchor="middle" font-size="13" font-weight="500" fill="%s">Open</text></g><g transform="translate(70,50)"><rect width="150" height="90" rx="4" fill="#000" opacity=".15" filter="url(#bl)" transform="translate(0,2)" %s/><rect width="150" height="90" rx="4" fill="#F3EDF7" %s/>%s</g>'%(OUTL,ONS,mn2,mn2,items)
st=st.replace('width="150" height="90"','width="130" height="100"')
d.panel(X[1],Y[0],'Menu','radius 4 · item 48dp · grows from anchor · medium1',st)
# C bottom sheet
sc2=d.anim([(0,'opacity:0'),(8,'opacity:0'),(40,'opacity:.32'),(66,'opacity:.32'),(85,'opacity:0'),(100,'opacity:0')],timing=LIN)
sh=d.anim([(0,'transform:translateY(90px)'),(8,'transform:translateY(90px);animation-timing-function:%s'%DEC),(45,'transform:translateY(0)'),(66,'transform:translateY(0);animation-timing-function:%s'%ACC),(85,'transform:translateY(90px)'),(100,'transform:translateY(90px)')])
inner='<clipPath id="pc"><rect width="150" height="130" rx="14"/></clipPath><g clip-path="url(#pc)"><rect width="150" height="130" fill="#000" %s/><g %s><path d="M0 130 V78 Q0 48 28 48 H122 Q150 48 150 78 V130 Z" fill="#F3EDF7"/><rect x="59" y="56" width="32" height="4" rx="2" fill="%s" opacity=".4"/><rect x="20" y="74" width="80" height="7" rx="3.5" fill="#CAC4D0"/><rect x="20" y="90" width="110" height="5" rx="2.5" fill="#E0DAE6"/><rect x="20" y="102" width="96" height="5" rx="2.5" fill="#E0DAE6"/></g></g>'%(sc2,sh,ONSV)
d.panel(X[2],Y[0],'Bottom sheet','top radius 28 · handle 32×4 · enter 500ms decelerate',phone(inner))
# D snackbar
sn=d.anim([(0,'opacity:0;transform:translateY(24px)'),(10,'opacity:0;transform:translateY(24px);animation-timing-function:%s'%DEC),(28,'opacity:1;transform:translateY(0)'),(70,'opacity:1;transform:translateY(0)'),(78,'opacity:0;transform:translateY(0)'),(100,'opacity:0;transform:translateY(0)')])
inner='<g %s><rect x="8" y="66" width="134" height="48" rx="4" fill="#322F35"/><text x="20" y="94" font-size="12" fill="#F5EFF7">Saved</text><text x="108" y="94" font-size="12" font-weight="500" fill="#D0BCFF">Undo</text></g>'%sn
d.panel(X[0],Y[1],'Snackbar','radius 4 · 48dp (1 line) · fade out 100ms',phone(inner))
# E card elevation
sd=d.anim([(0,'opacity:.12;transform:translateY(1px)'),(15,'opacity:.12;transform:translateY(1px)'),(27,'opacity:.26;transform:translateY(4px)'),(66,'opacity:.26;transform:translateY(4px)'),(78,'opacity:.12;transform:translateY(1px)'),(100,'opacity:.12;transform:translateY(1px)')])
sl=d.anim([(0,'opacity:0'),(15,'opacity:0'),(27,'opacity:.08'),(66,'opacity:.08'),(78,'opacity:0'),(100,'opacity:0')],timing=LIN)
st='<g transform="translate(75,36)"><rect class="t" width="140" height="84" rx="12" fill="#000" filter="url(#bl)" %s/><rect width="140" height="84" rx="12" fill="#F3EDF7"/><rect width="140" height="84" rx="12" fill="%s" %s/><text x="14" y="30" font-size="13" font-weight="500" fill="%s">Elevated card</text><text x="14" y="48" font-size="11" fill="%s">level 1 → 2 on hover</text></g>'%(sd,PRI,sl,ONS,ONSV)
d.panel(X[1],Y[1],'Card','radius 12 · elevation 1dp → 3dp · state layer .08',st)
# F extended FAB (SMIL)
ks='0;.1;.35;.7;.95;1'; sp='0 0 1 1;.05 .7 .1 1;0 0 1 1;.3 0 .8 .15;0 0 1 1'
lbl=d.anim([(0,'opacity:0'),(26,'opacity:0'),(36,'opacity:1'),(66,'opacity:1'),(72,'opacity:0'),(100,'opacity:0')],timing=LIN)
st='<g transform="translate(55,46)"><rect height="56" rx="16" fill="%s"><animate attributeName="width" values="56;56;150;150;56;56" keyTimes="%s" calcMode="spline" keySplines="%s" dur="4s" repeatCount="indefinite"/></rect><path d="M28 18 V38 M18 28 H38" stroke="#21005D" stroke-width="2.5" stroke-linecap="round"/><text x="54" y="33" font-size="14" font-weight="500" fill="#21005D" %s>Create</text></g>'%(PC,ks,sp,lbl)
d.panel(X[2],Y[1],'Extended FAB','56dp · radius 16 · width morphs, label fades in',st)
d.write('motion-surfaces.svg','Shown in ~3× slow motion so the easing is visible. Real durations are in the reference table.')

# ---------- FILE 3: navigation, transitions, progress ----------
d=Doc(495)
def oncolor(intervals,on,off,w=6):
    fr=[(0,'fill:%s'%off)]
    for a,b in intervals:
        fr+= [(max(a-w,0),'fill:%s'%off),(a,'fill:%s'%on),(b,'fill:%s'%on),(min(b+w,100),'fill:%s'%off)]
    fr.append((100,'fill:%s'%off))
    # dedupe/sort
    seen={};
    for p,c in fr: seen[p]=c
    return sorted(seen.items())
# A navigation bar
cx=[65,145,225]
i1=d.anim([(0,'transform:scaleX(1)'),(30,'transform:scaleX(1)'),(37,'transform:scaleX(0)'),(86,'transform:scaleX(0)'),(93,'transform:scaleX(1)'),(100,'transform:scaleX(1)')])
i2=d.anim([(0,'transform:scaleX(0)'),(36,'transform:scaleX(0)'),(52,'transform:scaleX(1)'),(80,'transform:scaleX(1)'),(87,'transform:scaleX(0)'),(100,'transform:scaleX(0)')])
c1=d.anim(oncolor([(0,34),(90,100)],'#1D192B','#49454F'),timing=LIN)
c2=d.anim(oncolor([(40,82)],'#1D192B','#49454F'),timing=LIN)
st='<g transform="translate(0,20)"><rect x="25" y="20" width="240" height="84" rx="14" fill="#F3EDF7"/><rect class="t" x="33" y="28" width="64" height="32" rx="16" fill="%s" %s/><rect class="t" x="113" y="28" width="64" height="32" rx="16" fill="%s" %s/><circle cx="65" cy="44" r="8" %s/><rect x="137" y="36" width="16" height="16" rx="4" %s/><path d="M225 35 L233 44 L225 53 L217 44 Z" fill="#49454F"/><text x="65" y="82" text-anchor="middle" font-size="12" fill="%s">Home</text><text x="145" y="82" text-anchor="middle" font-size="12" fill="%s">Search</text><text x="225" y="82" text-anchor="middle" font-size="12" fill="%s">Library</text></g>'%(SC,i1,SC,i2,c1,c2,ONS,ONSV,ONSV)
d.panel(X[0],Y[0],'Navigation bar','80dp · indicator 64×32 · expands from center',st)
# B tabs
tx=d.anim([(0,'transform:translateX(0)'),(20,'transform:translateX(0)'),(32,'transform:translateX(80px)'),(48,'transform:translateX(80px)'),(60,'transform:translateX(160px)'),(76,'transform:translateX(160px)'),(88,'transform:translateX(0)'),(100,'transform:translateX(0)')])
t1=d.anim(oncolor([(0,26),(88,100)],PRI,'#49454F',5),timing=LIN)
t2=d.anim(oncolor([(32,54)],PRI,'#49454F',5),timing=LIN)
t3=d.anim(oncolor([(60,82)],PRI,'#49454F',5),timing=LIN)
st='<g transform="translate(0,34)"><rect x="25" y="0" width="240" height="56" fill="#FEF7FF"/><text x="65" y="32" text-anchor="middle" font-size="14" font-weight="500" %s>Photos</text><text x="145" y="32" text-anchor="middle" font-size="14" font-weight="500" %s>Albums</text><text x="225" y="32" text-anchor="middle" font-size="14" font-weight="500" %s>Shared</text><rect x="25" y="55" width="240" height="1" fill="#CAC4D0"/><rect x="45" y="52" width="40" height="3" rx="1.5" fill="%s" %s/></g>'%(t1,t2,t3,PRI,tx)
d.panel(X[1],Y[0],'Primary tabs','48dp · indicator 3dp · slides with standard easing',st)
# C shared axis
a=d.anim([(0,'transform:translateX(0);opacity:1'),(20,'transform:translateX(0);opacity:1;animation-timing-function:%s'%ACC),(27,'transform:translateX(-30px);opacity:0'),(77,'transform:translateX(-30px);opacity:0;animation-timing-function:%s'%DEC),(99,'transform:translateX(0);opacity:1'),(100,'transform:translateX(0);opacity:1')])
b=d.anim([(0,'transform:translateX(30px);opacity:0'),(27,'transform:translateX(30px);opacity:0;animation-timing-function:%s'%DEC),(49,'transform:translateX(0);opacity:1'),(70,'transform:translateX(0);opacity:1;animation-timing-function:%s'%ACC),(77,'transform:translateX(30px);opacity:0'),(100,'transform:translateX(30px);opacity:0')])
st='<g transform="translate(70,20)"><g %s><rect width="150" height="120" rx="12" fill="%s"/><text x="75" y="64" text-anchor="middle" font-size="16" font-weight="500" fill="#21005D">Step 1</text></g><g %s><rect width="150" height="120" rx="12" fill="#FFD8E4"/><text x="75" y="64" text-anchor="middle" font-size="16" font-weight="500" fill="#31111D">Step 2</text></g></g>'%(a,PC,b)
d.panel(X[2],Y[0],'Shared axis (X)','slide 30dp + fade · out 90ms accelerate, in 210ms decelerate',st)
# D container transform (SMIL)
ks='0;.15;.5;.7;.9;1'; sp='0 0 1 1;.05 .7 .1 1;0 0 1 1;.3 0 .8 .15;0 0 1 1'
def an(attr,vals):
    return '<animate attributeName="%s" values="%s" keyTimes="%s" calcMode="spline" keySplines="%s" dur="4s" repeatCount="indefinite"/>'%(attr,vals,ks,sp)
sm=d.anim([(0,'opacity:1'),(15,'opacity:1'),(24,'opacity:0'),(68,'opacity:0'),(90,'opacity:1'),(100,'opacity:1')],timing=LIN)
bigc=d.anim([(0,'opacity:0'),(34,'opacity:0'),(46,'opacity:1'),(66,'opacity:1'),(72,'opacity:0'),(100,'opacity:0')],timing=LIN)
st='<rect x="30" y="14" width="230" height="128" rx="12" fill="#fff" stroke="#E7E0EC"/><rect x="42" y="24" width="100" height="6" rx="3" fill="#E7E0EC"/><rect x="42" y="38" width="130" height="5" rx="2.5" fill="#EFE9F3"/><rect fill="%s" x="60" y="80" width="90" height="56" rx="12">%s%s%s%s</rect><rect x="72" y="94" width="46" height="6" rx="3" fill="#21005D" %s/><rect x="72" y="108" width="64" height="5" rx="2.5" fill="#7F67BE" %s/><g %s><rect x="46" y="28" width="90" height="8" rx="4" fill="#21005D"/><rect x="46" y="48" width="196" height="6" rx="3" fill="#7F67BE"/><rect x="46" y="62" width="170" height="6" rx="3" fill="#7F67BE"/><rect x="46" y="76" width="184" height="6" rx="3" fill="#7F67BE"/></g>'%(PC,an('x','60;60;30;30;60;60'),an('y','80;80;14;14;80;80'),an('width','90;90;230;230;90;90'),an('height','56;56;128;128;56;56')+an('rx','12;12;12;12;12;12'),sm,sm,bigc)
d.panel(X[0],Y[1],'Container transform','card grows into the page · 500ms emphasized',st)
# E linear indeterminate
b1=d.anim([(0,'transform:translateX(-80px) scaleX(.5)'),(60,'transform:translateX(150px) scaleX(1.4)'),(100,'transform:translateX(330px) scaleX(.5)')],dur=2,timing=STD)
b2=d.anim([(0,'transform:translateX(-80px) scaleX(.5)'),(50,'transform:translateX(-80px) scaleX(.5)'),(100,'transform:translateX(330px) scaleX(.4)')],dur=2,timing=STD,delay=.4)
st='<clipPath id="lc"><rect x="45" y="73" width="200" height="4" rx="2"/></clipPath><rect x="45" y="73" width="200" height="4" rx="2" fill="#E7E0EC"/><g clip-path="url(#lc)"><rect class="tl" x="45" y="73" width="80" height="4" fill="%s" %s/><rect class="tl" x="45" y="73" width="80" height="4" fill="%s" %s/></g>'%(PRI,b1,PRI,b2)
d.panel(X[1],Y[1],'Linear progress','4dp track · indeterminate (real speed)',st)
# F circular
rot=d.anim([(0,'transform:rotate(0)'),(100,'transform:rotate(360deg)')],dur=1.6,timing=LIN)
dsh=d.anim([(0,'stroke-dasharray:6 107;stroke-dashoffset:0'),(50,'stroke-dasharray:72 41;stroke-dashoffset:-22'),(100,'stroke-dasharray:6 107;stroke-dashoffset:-113')],dur=1.6,timing=STD)
st='<g transform="translate(145,75)"><g class="t" %s><circle class="t" r="18" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round" %s/></g></g>'%(rot,PRI,dsh)
d.panel(X[2],Y[1],'Circular progress','48dp · stroke 4dp · indeterminate (real speed)',st)
d.write('motion-navigation.svg','Transitions shown in ~3× slow motion · progress indicators at real speed.')
