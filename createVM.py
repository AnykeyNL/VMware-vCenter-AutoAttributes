import os
from pyVim.connect import SmartConnect, Disconnect, SmartConnection
from pyVmomi import vim, vmodl
import ssl
from datetime import datetime

user = "administrator@vsphere.local"
pwd = "setyourpasswordhere"
vc = "127.0.0.1"
vc_port = 443

def get_obj_by_moid(content, vimtype, moid):
    obj = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True)
    for c in container.view:
        if moid:
            if c._GetMoId() == moid:
                obj = c
                break
    return obj

VM_moref = os.getenv('VMWARE_ALARM_TARGET_ID', 'debug_VMWARE_ALARM_TARGET_ID')
alarm_user = os.getenv('VMWARE_ALARM_EVENT_USERNAME', 'debug_VMWARE_ALARM_EVENT_USERNAME')

context = None
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

si = SmartConnect(host=vc, user=user, pwd=pwd, port=vc_port, sslContext=context)
content = si.RetrieveContent()

vm = get_obj_by_moid(content, [vim.VirtualMachine], VM_moref)

key = 'CreatedBy'
value = alarm_user
vm.setCustomValue(key, value)

key = 'CreatedDate'
now = datetime.now()
value = now.strftime("%m/%d/%Y, %H:%M:%S")
vm.setCustomValue(key, value)

Disconnect(si)
