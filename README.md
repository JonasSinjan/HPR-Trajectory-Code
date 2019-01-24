# HPR-Trajectory-Code

    functions.py

  Calculations.one_stage calculates the motor delay (coast time), max velocity and peak altitude of a one stage rocket.
  This uses equations from: http://www.rocketmime.com/rockets/qref.html
  The validity of these equations are not confirmed.

  Calculations.two_stage calculates the motor delay (coast time), max velocity and peak altitude of a two stage rocket.
  This uses equations from: http://www.rocketmime.com/rockets/multistg.html
  The validity of these equations are not confirmed.
  
  Calculations.ODEints not completed atm.
  Will complete a numerical intregation using forward Euler like that described in http://web.mit.edu/16.unified/www/FALL/systems/Lab_Notes/traj.pdf

    data_run.py
    
   Fill in the Area and empty mass parameters of the stages.
   Also fill in the engine data if using different engines.
   
   Engine data currently in file:
   
   1st stage motor: CESARONI - P38-4G WHITE THUNDER (I470).
   Link: https://www.apogeerockets.com/Rocket_Motors/Cesaroni_Propellant_Kits/Cesaroni_Certification_Special/38mm_Certification_Propellants/Cesaroni_P38-4G_White_Thunder_I470#faqs
   
   2nd stage motor: CESARONI - P38-5G BLUE STREAK (J357).
   Link: https://www.apogeerockets.com/Rocket_Motors/Cesaroni_Propellant_Kits/38mm_Motors/5-Grain_Motors/Cesaroni_P38-5G_Blue_Streak_J357
   
   Once all data filled in, just run: data_run.py.
  
   
   
