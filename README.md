# husky_scripts

- In the `sim_tools_husky` repository
To launch the simulation, use:
```roslaunch mtu_husky_gazebo mtu_20_robot.launch```
where the final argument is the launchfile defined in `sim_tools_husky/src/mtu_husky_gazebo/launch`

To edit the environment, use:
```gazebo src/my_husky_sim/worlds/20_robot.world```

- In the `husky_devel` repository
To run the logic for an individual robot, use:
```rosrun microgrid_demo ssrr_agent.py r20n3```

- In this repository
I scripted this to run multiple robots at once with:
```bash multi-run.sh```

For the plots generated from the points in the bagfile, use:
```python simulation_plot.py 4```
Where the argument is the number of robots. (Note, this uses absolute paths and will not work out of the box)