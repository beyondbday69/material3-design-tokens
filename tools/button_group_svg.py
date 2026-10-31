import sys
OUT=sys.argv[1]
FONT="Roboto,'Segoe UI',system-ui,sans-serif"
PRI='#6750A4'; SURF='#FEF7FF'; ONS='#1D1B20'; ONSV='#49454F'
def f(v): return ('%.2f'%v).rstrip('0').rstrip('.')
def rr(x,y,w,h,tl,tr,br,bl):
    return "M%s,%s H%s A%s,%s 0 0 1 %s,%s V%s A%s,%s 0 0 1 %s,%s H%s A%s,%s 0 0 1 %s,%s V%s A%s,%s 0 0 1 %s,%s Z"%(
        f(x+tl),f(y),f(x+w-tr),f(tr),f(tr),f(x+w),f(y+tr),f(y+h-br),f(br),f(br),f(x+w-br),f(y+h),f(x+bl),f(bl),f(bl),f(x),f(y+h-bl),f(y+tl),f(tl),f(tl),f(x+tl),f(y))
KT=[0,.12,.2,.55,.63,1]
KS=";".join([".2 0 0 1"]*5)
def anim(attr,vals,dur=4):
    return '<animate attributeName="%s" values="%s" keyTimes="%s" calcMode="spline" keySplines="%s" dur="%ss" repeatCount="indefinite"/>'%(attr,";".join(vals),";".join(str(k) for k in KT),KS,dur)
def layouts(W,gap,p,ratio=.15,limit=16):
    """returns (base widths, pressed widths)"""
    n=len(W); P=list(W)
    if n>1:
        if 0<p<n-1:
            g=min(ratio*W[p]/2.0,limit,limit); gl=min(g,W[p-1]); gr=min(g,W[p+1])
            P[p-1]-=gl; P[p+1]-=gr; P[p]+=gl+gr
        elif p==0:
            g=min(ratio*W[p],limit); g=min(g,W[p+1]); P[1]-=g; P[0]+=g
        else:
            g=min(ratio*W[p],limit); g=min(g,W[p-1]); P[p-1]-=g; P[p]+=g
    return list(W),P
def xs(W,gap):
    out=[];x=0
    for w in W: out.append(x); x+=w+gap
    return out
def row(labels,W,gap,p,connected,H=40,full=20,inner=8,pinner=4,pressed_round=8):
    base,pr=layouts(W,gap,p)
    xb=xs(base,gap); xp=xs(pr,gap)
    s=''
    n=len(W)
    for i in range(n):
        if connected:
            ol=full if i==0 else inner; orr=full if i==n-1 else inner
            def d(x,w,pressed):
                il=ol; ir=orr
                if pressed:
                    il=ol if i==0 else pinner; ir=orr if i==n-1 else pinner
                return rr(x,0,w,H,il,ir,ir,il)
            dv=[d(xb[i],base[i],0)]*2+[d(xp[i],pr[i],i==p)]*2+[d(xb[i],base[i],0)]*2
            dv=[d(xb[i],base[i],0),d(xb[i],base[i],0),d(xp[i],pr[i],i==p),d(xp[i],pr[i],i==p),d(xb[i],base[i],0),d(xb[i],base[i],0)]
            s+='<path d="%s" fill="%s">%s</path>'%(dv[0],PRI,anim('d',dv))
        else:
            xv=[xb[i],xb[i],xp[i],xp[i],xb[i],xb[i]]
            wv=[base[i],base[i],pr[i],pr[i],base[i],base[i]]
            rv=[full,full,pressed_round if i==p else full,pressed_round if i==p else full,full,full]
            s+='<rect y="0" height="%d" x="%s" width="%s" rx="%d" fill="%s">%s%s%s</rect>'%(H,f(xb[i]),f(base[i]),full,PRI,anim('x',[f(v) for v in xv]),anim('width',[f(v) for v in wv]),anim('rx',[str(v) for v in rv]))
        cx=[xb[i]+base[i]/2.0]*2+[xp[i]+pr[i]/2.0]*2+[xb[i]+base[i]/2.0]*2
        s+='<text y="25" text-anchor="middle" font-size="14" font-weight="500" fill="#fff" x="%s">%s%s</text>'%(f(cx[0]),labels[i],anim('x',[f(v) for v in cx]))
    return s,base,pr
rows=[]
body=''
labels=['Day','Week','Month','Year']; W=[80,76,96,80]
specs=[('Standard group · press a middle button','spacing 12 · pressed grows 15% of its width · each neighbor gives up 7.5%',W,12,1,False),
       ('Standard group · press an end button','the single neighbor gives up the full 15%',W,12,0,False),
       ('Connected group','spacing 2 · inner corners 8 → 4 when pressed · outer corners full',W,2,2,True)]
y=24
for title,sub,Ws,gap,p,conn in specs:
    g,base,pr=row(labels,Ws,gap,p,conn)
    total=sum(Ws)+gap*(len(Ws)-1)
    ox=(960-total*2)/2.0
    body+='<text x="40" y="%d" font-size="15" font-weight="500" fill="%s">%s</text><text x="40" y="%d" font-size="12" fill="%s">%s</text>'%(y+14,ONS,title,y+32,ONSV,sub)
    body+='<g transform="translate(%s,%d) scale(2)">%s</g>'%(f(ox),y+46,g)
    sw='pressed %s → %s · neighbor(s) %s'%(f(base[p]),f(pr[p]),' / '.join(f(base[i])+' → '+f(pr[i]) for i in range(len(Ws)) if i!=p and pr[i]!=base[i]))
    body+='<text x="480" y="%d" text-anchor="middle" font-size="12" fill="%s">%s (dp, size S)</text>'%(y+46+80+24,ONSV,sw)
    y+=160
H=y+30
svg='<svg xmlns="http://www.w3.org/2000/svg" width="960" height="%d" viewBox="0 0 960 %d" font-family="%s"><rect width="960" height="%d" rx="28" fill="%s"/>%s<text x="480" y="%d" text-anchor="middle" font-size="12" fill="%s">Shown in slow motion. Real motion: fast spatial spring (Standard 1400 / 0.9, Expressive 800 / 0.6).</text></svg>'%(H,H,FONT,H,SURF,body,H-12,ONSV)
open(OUT+'/button-group.svg','w').write(svg)
print(H)
