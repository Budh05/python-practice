
#!Printing Saturn
from math import sin

#? Aspect ratio total 42 rows and 150 columns
for y in range (-21,21):
    for x in range (-75,75):
        a,b=x/34,y/20
        d=1-a*a - b*b                   #Saturns sphere
        v=(0.99*b -0.14*a) / 0.22       #Saturns ring
        r=((0.99*a +0.14*b)**2 +v*v)**0.5
        ring= 1.3<r<2.2 and abs (r-1.8)>0.05    #abs curves out gap b/w radius
        light=0
        if ring and (d<0 or v>0):               #3D depth effect for ring
            light=0.7 + 0.25*sin(r*11)          #ring lighting
        elif d>=0:
            light=0.3 +0.7*d*0.5 -a/4 +sin(v*5)/20  #planet lighting
        q=int(min(max(light,0),0.99)*256)            #adding colours
        i=q*10//256
        c = f"\033[38;2;{q};{q*85//100};{q*60//100}m"
        print(c + " .:-=+*#%@"[i], end="")
    print("\033[0m")