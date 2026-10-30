import math
PRI='#6750A4'; SECC='#E8DEF8'; TRACK='#E8DEF8'
def f(v): return ('%.1f'%v).rstrip('0').rstrip('.')
# ---------------- slider ----------------
def slider_active(w,h,c):
    c=min(c,h/2.0)
    return "M%s,0 H%s A2,2 0 0 1 %s,2 V%s A2,2 0 0 1 %s,%s H%s A%s,%s 0 0 1 0,%s V%s A%s,%s 0 0 1 %s,0 Z"%(f(c),f(w-2),f(w),f(h-2),f(w-2),f(h),f(c),f(c),f(c),f(h-c),f(c),f(c),f(c),f(c))
def slider_inactive(a,L,h,c):
    c=min(c,h/2.0)
    return "M%s,0 H%s A%s,%s 0 0 1 %s,%s V%s A%s,%s 0 0 1 %s,%s H%s A2,2 0 0 1 %s,%s V2 A2,2 0 0 1 %s,0 Z"%(f(a+2),f(L-c),f(c),f(c),f(L),f(c),f(h-c),f(c),f(c),f(L-c),f(h),f(a+2),f(a),f(h-2),f(a+2))
def slider_static(L,h,hh,c,hpos,hw=4,gap=6):
    """static slider drawn with track top at y=0, handle centered on track. returns svg group content"""
    s=slider_active(hpos-gap,h,c)
    i=slider_inactive(hpos+hw+gap,L,h,c)
    return '<path d="%s" fill="%s"/><path d="%s" fill="%s"/><circle cx="%s" cy="%s" r="2" fill="%s"/><rect x="%s" y="%s" width="%s" height="%s" rx="2" fill="%s"/>'%(s,PRI,i,SECC,f(L-8),f(h/2.0),PRI,f(hpos),f(h/2.0-hh/2.0),hw,hh,PRI)
def slider_animated_xs(dur=4):
    L=200;h=16;c=8
    kt=[0,.1,.15,.45,.5,.7,.75,.95,1]
    H=[40,40,40,130,130,130,130,40,40]
    W=[4,4,2,2,4,4,2,2,4]
    act=[slider_active(x-6,h,c) for x in H]
    ina=[slider_inactive(x+W_+6,L,h,c) for x,W_ in zip(H,W)]
    X=[x+(4-w)/2.0 for x,w in zip(H,W)]
    ks=";".join(str(k) for k in kt); sp=";".join([".2 0 0 1"]*(len(kt)-1))
    def an(attr,vals): return '<animate attributeName="%s" values="%s" keyTimes="%s" calcMode="spline" keySplines="%s" dur="%ss" repeatCount="indefinite"/>'%(attr,";".join(vals),ks,sp,dur)
    return ('<path d="%s" fill="%s">%s</path><path d="%s" fill="%s">%s</path><circle cx="%d" cy="8" r="2" fill="%s"/><rect y="-14" height="44" rx="2" fill="%s" x="40" width="4">%s%s</rect>'
        %(act[0],PRI,an('d',act),ina[0],SECC,an('d',ina),L-8,PRI,PRI,an('x',[f(v) for v in X]),an('width',[str(w) for w in W])))
# ---------------- progress ----------------
def poly(pts): return 'M'+' L'.join('%s,%s'%(f(x),f(y)) for x,y in pts)
def wave_line(x0,x1,y,A,lam,phase,N=60):
    out=[]
    for i in range(N+1):
        x=x0+(x1-x0)*i/float(N)
        out.append((x,y+A*math.sin(2*math.pi*(x-x0)/lam+phase)))
    return out
def smooth(t): t=max(0,min(1,t)); return t*t*(3-2*t)
def linear_frames(L,y,thick,A,lam,pfun,nfr,dur,speed_wl_per_s=1.0,gap=4):
    """returns lists of active d, track d for nfr frames across dur"""
    ad=[];td=[]
    for k in range(nfr+1):
        t=dur*k/float(nfr); p=pfun(t); phase=2*math.pi*speed_wl_per_s*t
        amp=A*smooth((p-.1)/.05)*(1-smooth((p-.95)/.05)) if A else 0
        x1=max(thick/2.0+1,p*L)
        ad.append(poly(wave_line(thick/2.0,x1,y,amp,lam,phase)))
        s=min(x1+gap+thick,L-thick/2.0-1); e=L-thick/2.0
        td.append('M%s,%s L%s,%s'%(f(s),f(y),f(e),f(y)))
    return ad,td
def animate_d(vals,dur,linear=True):
    n=len(vals)
    return '<animate attributeName="d" values="%s" dur="%ss" repeatCount="indefinite" calcMode="linear"/>'%(";".join(vals),dur)
def linear_stage(L,y,thick,A,lam,pfun,nfr,dur,tilt=None,gap=4,dot=True):
    ad,td=linear_frames(L,y,thick,A,lam,pfun,nfr,dur,gap=gap)
    s='<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</path>'%(td[0],TRACK,thick,animate_d(td,dur))
    s+='<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</path>'%(ad[0],PRI,thick,animate_d(ad,dur))
    if dot: s+='<circle cx="%s" cy="%s" r="2" fill="%s"/>'%(f(L-thick/2.0),f(y),PRI)
    return s
def circ_pts(cx,cy,R,a0,sweep,A,lam,phase,N=80):
    out=[]
    for i in range(N+1):
        th=a0+sweep*i/float(N)
        arc=R*(th-a0)
        r=R+A*math.sin(2*math.pi*arc/lam+phase)
        out.append((cx+r*math.cos(th),cy+r*math.sin(th)))
    return out
def circular_frames(cx,cy,R,thick,A,lam,p,nfr,dur,gap=4):
    a0=-math.pi/2; gp=(gap+thick)/R
    ad=[];td=[]
    for k in range(nfr+1):
        t=dur*k/float(nfr); phase=2*math.pi*t
        ad.append(poly(circ_pts(cx,cy,R,a0,max(.05,p*2*math.pi-gp/2),A,lam,phase)))
        st=a0+p*2*math.pi+gp/2
        sw=(a0+2*math.pi-gp/2)-st
        td.append(poly(circ_pts(cx,cy,R,st,max(.02,sw),0,lam,0,N=60)))
    return ad,td
def circular_stage(cx,cy,R,thick,A,lam,p,nfr,dur,gap=4):
    ad,td=circular_frames(cx,cy,R,thick,A,lam,p,nfr,dur,gap)
    s='<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"/>'%(td[0],TRACK,thick)
    s+='<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</path>'%(ad[0],PRI,thick,animate_d(ad,dur) if A else '')
    return s
