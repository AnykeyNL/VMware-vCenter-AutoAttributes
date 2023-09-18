# VMware-vCenter-AutoAttributes
Creates based on vCenter alarms, automatic custom attributes on newly created VMs

## IMPORTANT NOTICE!
Make sure you use the **--no-deps** option when installing additional modules on your vCenter. 
This will prevent any existing libraries to be overwritten by newer version and might else break
any other vcenter dependencies.

**MAKE A BACKUP OF YOUR VCENTER FIRST!!!**

## How to install
1. SSH to your vCenter as root
2. go to the shell
3. Install python pip, run: tdnf install python3-pip
![Alt text](screenshots/installpip.png?raw=true "Install PIP")
4. Install pyVmomi library, run: pip3 install -U --no-deps pyVmomi
![Alt text](screenshots/installpyvmomi.png?raw=true "Install pyVmomi")
5. create a directory: mkdir /root/scripts
6. Modify the createVM.py script to have your vCenter credentials correctly in it
7. copy the createVM.py script in the scripts directory
8. In vCenter, browse to "Tags & Custom Attributes" and add the following Custom Attributes:
    1. Attribute: CreatedBy - Type: Virtual Machine
    2. Attribute: CreatedDate - Type: Virtual Machine
    ![Alt text](screenshots/customattribute.png?raw=true "vCenter Custom Attributes")
9. Create a vCenter Alarm
   1. Click on your vcenter,  and go to the "configure" menu
   2. Click on the Alarm Definitions
   3. Click ADD and give the alarm a name, for example "VM Creation"
   4. Select target type to "Virtual Machines", click next
   ![Alt text](screenshots/vcenter_alarm_1.png?raw=true "vCenter Alarm - Step 1")
   5. Set trigger type to "VM Created" (in the Deployment section)
   6. Set trigger the alarm an [Keep the target's current state]
   7. Enable "run script"
   8. set script to: /usr/bin/python /root/scripts/createVM.py
   ![Alt text](screenshots/vcenter_alarm_2.png?raw=true "vCenter Alarm - Step 2")
   9. Click Next and Click Create

If you have completed all these steps, any new VM that is created will have automatically 2 custom attribute values. Who created the VM and when.
![Alt text](screenshots/example.png?raw=true "Example Custom Attribute values")




 
