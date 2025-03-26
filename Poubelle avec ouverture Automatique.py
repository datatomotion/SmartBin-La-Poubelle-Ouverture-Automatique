
"""


Auteur: Georg WIll

Interface: microbit

Nom du projet: Poubelle Intelligente

Description: No-description

Toolbox: vittascience

Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="N!m#N0R[1WbQk6;M7xth">Distance</variable></variables><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="-287" y="-112"></block><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="-38" y="-38"><statement name="DO"><block type="variables_set" id="X]]0Eb5mzW~q?YxDi]l-"><field name="VAR" id="N!m#N0R[1WbQk6;M7xth">Distance</field><value name="VALUE"><shadow type="math_number" id="s|kf8n,~obe`o6|SQuxn"><field name="NUM">0</field></shadow><block type="sensors_getGroveUltrasonicRanger" id="T)c+$PYmkb1q9*_GIs3w" inline="false"><mutation pin="false"></mutation><field name="SENSOR">HC-SR04</field><field name="DATA">DIST</field><field name="TRIG">pin2</field><field name="ECHO">pin1</field></block></value><next><block type="controls_if" id="xtnhT{MI8yM1UytV:/1N"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id=")[(1ZXKn!0pLaOtI)1mX"><field name="OP">LT</field><value name="A"><block type="variables_get" id="KKZCvNL^:)43.CJT88Gu"><field name="VAR" id="N!m#N0R[1WbQk6;M7xth">Distance</field></block></value><value name="B"><shadow type="math_number" id="e8sN:Lq1E`;K_C%yp3qv"><field name="NUM">10</field></shadow></value></block></value><statement name="DO0"><block type="actuators_setServoAngle" id="TOmC~3`4KK$/U7MS4%c#"><field name="PIN">pin15</field><value name="ANGLE"><shadow type="math_number" id=")-Uk9NyQ#GajH?[A6aKM"><field name="NUM">0</field></shadow></value><next><block type="show_icon" id="u;54TAFM)4ssU{I)sPKs"><field name="ICON">YES</field><next><block type="io_pause" id=")ywepYr}(P3`6)sacf$E"><field name="UNIT">SECOND</field><value name="TIME"><shadow type="math_number" id="GUo*Q*CW}uSD2F,{@5[N"><field name="NUM">1</field></shadow></value></block></next></block></next></block></statement><statement name="ELSE"><block type="actuators_setServoAngle" id="]sGJjUl9auk7GKzPVOws"><field name="PIN">pin15</field><value name="ANGLE"><shadow type="math_number" id="Cep0{qh2U)Ssl)=DsDA-"><field name="NUM">180</field></shadow></value><next><block type="show_icon" id="T?lDF)~OUq5PT]lQF}$n"><field name="ICON">NO</field><next><block type="io_pause" id="7E2F,5)[pOMR}!23nLq0"><field name="UNIT">SECOND</field><value name="TIME"><shadow type="math_number" id="?c[AuhBH=[e#{COQ.-?["><field name="NUM">1</field></shadow></value></block></next></block></next></block></statement></block></next></block></statement></block></xml>

Projet généré par Vittascience.

Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau

sur l'interface http://vittascience.com/microbit


"""

from microbit import *
from machine import time_pulse_us
import utime

# Ultrasonic TRIG on pin2
# Ultrasonic ECHO on pin1
# Servo on pin15

def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
  trig.write_digital(0)
  utime.sleep_us(2)
  trig.write_digital(1)
  utime.sleep_us(10)
  trig.write_digital(0)
  echo.read_digital()
  duration = time_pulse_us(echo, 1, timeout_us)/1e6 # t_echo in seconds
  if duration > 0:
    if data == 'distance':
      #sound speed, round-trip/2, get in cm
      return 343 * duration/2 * 100
    elif data == 'duration':
      return duration
    else:
      raise ValueError("Data option '" + data + "' is not valid")
  else:
    return -1

def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.write_analog(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")

while True:
  Distance = getUltrasonicData(pin2, pin1, 'distance')
  if Distance < 10:
    setServoAngle(pin15, 0)
    display.show(Image.YES)
    utime.sleep(1)
  else:
    setServoAngle(pin15, 180)
    display.show(Image.NO)
    utime.sleep(1)
