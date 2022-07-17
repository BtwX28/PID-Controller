
import os
import sys

class myPID :

  def __init__(self, dt, max, min, kp, kd, ki) :
    self.dt  = dt
    self.max = max
    self.min = min
    self.kp  = kp
    self.kd  = kd
    self.ki  = ki
    self.integra = 0
    self.last_error = 0
    
  def running_gag(self,set,act) :
    error = set - act;
    #self.kp * (set -act) = P
    #I = (self.integra += (set-act)*self.dt) * self.ki
    #self.kd * ((set -act) - self.last_error)/self.dt = D
 
    P = self.kp * error;
 
    self.integra += error * self.dt;
    I = self.ki * self.integra;
 
    D = self.kd * (error - self.last_error) / self.dt;
 
    output = P + I + D;
 
    if output > self.max :
        output = self.max
    elif output < self.min :
        output = self.min
 
    self.last_error = error;
    return(output);

def main() :
  pid = myPID(0.1, 100, -100, 0.1, 0.01, 0.5)
 
  val = 20;
  for i in range(100) :
    inc = pid.running_gag(0, val)
    print(f'val: {round(val,2)} inc: {round(inc,2)}')
    val += inc
main()
#Graphik

#def graf() :