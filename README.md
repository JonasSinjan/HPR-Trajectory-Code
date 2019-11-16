# HPR-Trajectory-Code
    
    odersolver.py

  The system: a two-stage rocket, using the motors described at the bottom, for only vertical flight.
  The governing set of ordinary differential equations, taking into account a v^2 drag and gravity, are solved numerically
  using scipy.integrate.solve_ivp (initial value problem), using the RK45 method.  Run odesolver.py and the graphs
  will be generated including the velocity, height, mass and acceleration against time.  A parachute opening on descent is not included in the simulation.


    functions.py

  Calculations.one_stage calculates the motor delay (coast time), max velocity and peak altitude of a one stage rocket.
  This uses equations from: http://www.rocketmime.com/rockets/qref.html
  These equations make an estimate for the average mass during the burn.  For a thorough analysis a dynamic (changing) mass must be considered, this requires Numerical methods since it cannot be solved analytically.

  Calculations.two_stage calculates the motor delay (coast time), max velocity and peak altitude of a two stage rocket.
  This uses equations from: http://www.rocketmime.com/rockets/multistg.html
  These equations make an estimate for the average mass during the burn.  For a thorough analysis a dynamic (changing) mass must be considered, this requires Numerical methods since it cannot be solved analytically.

    data_run.py
    
   Fill in the Area and empty mass parameters of the stages.
   Also fill in the engine data if using different engines.
   
   Engine data currently in file:
   
   1st stage motor: CESARONI - P38-4G WHITE THUNDER (I470).
   Link: https://www.apogeerockets.com/Rocket_Motors/Cesaroni_Propellant_Kits/Cesaroni_Certification_Special/38mm_Certification_Propellants/Cesaroni_P38-4G_White_Thunder_I470#faqs
   
   2nd stage motor: CESARONI - P38-5G BLUE STREAK (J357).
   Link: https://www.apogeerockets.com/Rocket_Motors/Cesaroni_Propellant_Kits/38mm_Motors/5-Grain_Motors/Cesaroni_P38-5G_Blue_Streak_J357
   
   Once all data filled in, run: data_run.py.
   
  
   
   
