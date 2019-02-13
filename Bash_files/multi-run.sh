#!/bin/bash

cd ~/husky_devel
source devel/setup.bash

trap "kill $PID_LIST & exit" SIGINT SIGTERM
rosrun microgrid_demo ssrr_agent.py r20n1 & PID_LIST+=" $!" 
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n3 & PID_LIST+=" $!"
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n11 & PID_LIST+=" $!"
sleep 20
rosrun microgrid_demo ssrr_agent.py r20n4 & PID_LIST+=" $!"
sleep 10
rosrun microgrid_demo ssrr_agent.py r20n6 & PID_LIST+=" $!"
sleep 7
rosrun microgrid_demo ssrr_agent.py r20n16 & PID_LIST+=" $!"
sleep 210
rosrun microgrid_demo ssrr_agent.py r20n2 & PID_LIST+=" $!"
sleep 22
rosrun microgrid_demo ssrr_agent.py r20n5 & PID_LIST+=" $!"
sleep 10
rosrun microgrid_demo ssrr_agent.py r20n12 & PID_LIST+=" $!"
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n7 & PID_LIST+=" $!"
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n9 & PID_LIST+=" $!"
sleep 15
rosrun microgrid_demo ssrr_agent.py r20n17 & PID_LIST+=" $!"
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n8 & PID_LIST+=" $!"
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n10 & PID_LIST+=" $!"
sleep 18
rosrun microgrid_demo ssrr_agent.py r20n18 & PID_LIST+=" $!"
sleep 2
rosrun microgrid_demo ssrr_agent.py r20n13 & PID_LIST+=" $!"
sleep 25
rosrun microgrid_demo ssrr_agent.py r20n14 & PID_LIST+=" $!"
sleep 200
rosrun microgrid_demo ssrr_agent.py r20n15 & PID_LIST+=" $!"
sleep 5
rosrun microgrid_demo ssrr_agent.py r20n19 & PID_LIST+=" $!"
sleep 30
rosrun microgrid_demo ssrr_agent.py r20n20 & PID_LIST+=" $!"


sleep 999999

kill $PID_LIST



