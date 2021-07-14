#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys, string, time
import com.xhaus.jyson.JysonCodec as json
from servicenow.ServiceNowClient import ServiceNowClient

if servicenowServer is None:
    print "No server provided."
    sys.exit(1)


snClient = ServiceNowClient.create_client(servicenowServer, username, password)

content = """
{"used_for":"%s","name":"%s","company":"%s","u_config_admin_group":"%s","version":"%s","u_vm":"%s","u_tomcat":"%s","u_mysql":"%s","u_space":"%s"}
""" % (environment, applicationName, company, configAdminGroup, version, virtualMachine, tomcat, mysql, cfSpace)
print "Sending content %s" % content

try:
    data = snClient.update_record( 'cmdb_ci_appl', content )
    print "Returned DATA = %s" % (data)
    print json.dumps(data, indent=4, sort_keys=True)
    sysId = data["sys_id"]
    print "Created %s in Service Now." % (sysId)
except Exception, e:
    exc_info = sys.exc_info()
    traceback.print_exception( *exc_info )
    print e
    print "Failed to create record in Service Now"
    sys.exit(1)
