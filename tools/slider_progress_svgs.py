import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import m3_shapes as M
OUT=sys.argv[1]
FONT="Roboto,'Segoe UI',system-ui,sans-serif"
ONS='#1D1B20'; ONSV='#49454F'; SURF='#FEF7FF'
def wrap(w,h,body,extra=''):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="%s"><rect width="%d" height="%d" rx="28" fill="#F7F2FA"/>%s%s</svg>'%(w,h,w,h,FONT,w,h,body,extra)
# ---- slider sizes ----
sizes=[('XS',16,44,16),('S',24,44,8),('M',40,52,12),('L',56,68,16),('XL',96,108,28)]
y=28; body=''
for name,th,hh,c in sizes:
    rowh=max(th,hh)
    cy=y+rowh/2.0
    body+='<text x="40" y="%s" font-size="22" font-weight="500" fill="%s">%s</text><text x="40" y="%s" font-size="12" fill="%s">track %d · handle 4×%d · corner %d</text>'%(('%.0f'%(cy-2)),ONS,name,('%.0f'%(cy+16)),ONSV,th,hh,c)
    body+='<g transform="translate(300,%s)">%s</g>'%(('%.1f'%(cy-th/2.0)),M.slider_static(600,th,hh,c,260))
    y+=rowh+18
H=int(y+18)
open(OUT+'/slider-sizes.svg','w').write(wrap(960,H,'<rect x="0" y="0" width="960" height="%d" rx="28" fill="%s"/>'%(H,SURF)+body))
# ---- progress variants (animated) ----
def panel(x,yy,title,sub,stage):
    return '<g transform="translate(%d,%d)"><rect width="290" height="200" rx="24" fill="%s" stroke="#E7E0EC"/>%s<text x="145" y="172" text-anchor="middle" font-size="14" font-weight="500" fill="%s">%s</text><text x="145" y="190" text-anchor="middle" font-size="11" fill="%s">%s</text></g>'%(x,yy,SURF,stage,ONS,title,ONSV,sub)
X=[30,335,640]; Y=[30,245]
p=lambda t:.6
body=''
body+=panel(X[0],Y[0],'Linear · flat','4dp track · gap 4 · stop 4 · round caps','<g transform="translate(35,75)">%s</g>'%M.linear_stage(220,0,4,0,40,p,2,1))
body+=panel(X[1],Y[0],'Linear · wavy','amp 3 · wavelength 40 · container 10 high','<g transform="translate(35,75)">%s</g>'%M.linear_stage(220,0,4,3,40,p,12,1))
body+=panel(X[2],Y[0],'Linear · thick wavy','8dp track · corner 4','<g transform="translate(35,75)">%s</g>'%M.linear_stage(220,0,8,3,40,p,12,1,gap=4))
body+=panel(X[0],Y[1],'Circular · flat','40dp · stroke 4 · inset 4 · gap 4','<g transform="translate(145,75) scale(2)">%s</g>'%M.circular_stage(0,0,18,4,0,15,.7,2,1))
body+=panel(X[1],Y[1],'Circular · wavy','48dp · stroke 4 · amp 1.6 · wavelength 15','<g transform="translate(145,75) scale(2)">%s</g>'%M.circular_stage(0,0,22,4,1.6,15,.7,12,1))
body+=panel(X[2],Y[1],'Circular · thick wavy','52dp · stroke 8 · corner 4','<g transform="translate(145,75) scale(1.9)">%s</g>'%M.circular_stage(0,0,22,8,1.6,15,.7,12,1,gap=4))
body+='<text x="480" y="479" text-anchor="middle" font-size="12" fill="%s">Waves travel at 1 wavelength per second. Amplitude is 0 below 10%% and above 95%% progress.</text>'%ONSV
open(OUT+'/progress-variants.svg','w').write(wrap(960,495,body))
