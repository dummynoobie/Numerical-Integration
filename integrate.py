#from sympy import *
from sympy import sympify,plot,Float,N,Interval,EmptySet
from sympy.abc import x
import matplotlib
from sympy.calculus.singularities import singularities





class numericalIntegration:
    def __init__(self,infunction :str,interval :str,n :int):
        self.infunction=infunction
        self.interval=interval
        self.n=n
        self.f=sympify(self.infunction)
        self.check=self.check_singularity()

    def plot_graphic(self,file_name):
        file = '{}.png'.format(file_name)

        graph = plot(self.f,(x,Float(self.interval.split()[0]),Float(self.interval.split()[1])), show=False, line_color='r')
       # graph.append(List2DSeries(x1, y1))

        graph.save(file)
        #graph.save()


    def evaluation(self,num):

        a = self.f.subs(x, num)
        res = N(a)
        return Float(res)

    def check_singularity(self):
        function=self.f
       # continous=continuous_domain(function, x, S.Reals)
        holeset=singularities(function,x)
        intervalset=Interval(Float(self.interval.split()[0]),Float(self.interval.split()[1]))
        intersection=holeset.intersect(intervalset)
        return intersection

    def rectangle(self):

        if self.check != EmptySet:
            return( 'Your interval contain singularity or undefined point')

        deltax=(Float(self.interval.split()[1])-Float(self.interval.split()[0]))/self.n
        addup = Float(self.interval.split()[0])
        area=0
        for i in range(1,self.n+1):
            area+=deltax*self.evaluation(addup)
            addup=addup+deltax
        return area
    def trapezoidal(self):
        if self.check != EmptySet:
            return ('Your interval contain singularity or undefined point')


        deltax=(Float(self.interval.split()[1])-Float(self.interval.split()[0]))/self.n
        addup = Float(self.interval.split()[0])
        area=0
        for i in range(1,self.n+1):
          if i==1 or i==self.n:
              area += deltax/2 * (self.evaluation(addup))
          else:
              area += deltax  * (self.evaluation(addup))
          addup=addup+deltax
        return area

    def simpson(self):
        if self.check != EmptySet:
            return ('Your interval contain singularity or undefined point')

        deltax=(Float(self.interval.split()[1])-Float(self.interval.split()[0]))/self.n
        addup = Float(self.interval.split()[0])
        area=0
        for i in range(self.n+1):
          if i==0 or i==self.n:
              area += deltax/3 * (self.evaluation(addup))
          else:
            if i%2==0 :
              area += 2/3*deltax*(self.evaluation(addup))
            elif i%2==1:
              area += 4 / 3 * deltax * (self.evaluation(addup))
          addup=addup+deltax
        return area


