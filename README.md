# Wormy

## What is a worm and how does it work?

A computer worm is a piece of software ( can be both malicious or helpful ) that is designed to replicate itself on the machine and spread to other devices. While some computer worms may have payloads sometime there are worms that are just designed to spread themseleves as far as possible with no payload on them and its only function is to spread to other machines.

There are several stages a worm must complete in order to be effective. 
  - Must first be able to see the other networks ( this can be the internet or a LAN )
  - Must have some way to get into the system ( this can be done with ssh passwords or other exploits )
  - Must have some way to replicate itself on the target machine
  - Must be able to spread to other networks using the same steps above
  
As state before the worm replication itself may not be harmful and there are often some benefitial use cases to use a worm to patch out security flaws ( such as changing default ssh passwords ). However the worm can also be used for malicious purposes such as when you use the worm to install backdoors on a number of machines or use them to crash a target computer. This can be done by adding a 'payload' in addition to the replication.


## Wormy

For this specific worm we will be testing out how to create a basic worm that is able to 
 
1) Scan the network using n-map : then storing that output 
2) Using that output to attempt to ssh into the ipaddresses using a default username and password ( in this case newly installed kali linus machines 
  2a) default user for kali machines: root
  2b) default passowrd for kali machines : toor
3) If the device is able to connect, will run a py script that will download the worm from github
4) Repeat steps 1-3 with infected machine


|Problems that I faced| | 
|--------|-----|
|No way to stop replication | Because of the way this worm works if each machine were to try to find other machines and run the script it would be problematic if say machine 1, infected machine 2 then if machine 2 scaned the network it would also see machine 1 and infect machine 1 again running the script one more time. Over time this could take down the entire network |
|Getting a readable n-map output| n-map has many different outputs, the one I used is the grepable output using the flag -oG since the other outputs gave too much information and for the purposes of this worm I only want information about the ipaddress. I can see in the future using the other outputs to perform more elborate scanning|
|Bash file| Had to learn how to use bash files to itereate through the n-map output and exectue python script|


## Tools

1) paramiko libaray: A library written in python to allow a script to run commands in the terminal.
2) python: worm is written in python and simply creates copies of itself on the machine. A payload can be added to this script
3) github: We import the worm onto other machines using git clone and cloning this repository. In the future we can host the worm on a seperate server instead.

## Limitations:

|limitation | description|
|---------|--------------|
|Python| Since the worm is written in python, This makes it so that only machines that can interpret python will be able to run it. While this is not an issue for linux machines ( As many linux machines come installed/ written in python ) for windows the interpreter must be downloaded beforehand |
|Shell Script| The sh file is written for linux/mac and the windows terminal is different|
|Network| Since we only try to ssh into machines where we know that user and password, it would be impossible to spread the worm to machines that do not use default user and passwords.|
