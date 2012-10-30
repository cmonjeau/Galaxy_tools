#!/bin/bash

# ./LogolMultiExec.sh -h for usage
#
#

. /local/env/envjava-1.6.0_05.sh
#. /local/env/envlogol.sh
#. /local/env/envvmatch.sh

# Installation directory
export LOGOL_HOME=/local/logol/LogolMatch
export VMATCH_HOME=/local/vmatch/vmatch.distribution
export PATH=/local/logol/LogolMatch:$PATH:$VMATCH_HOME

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/sge/lib/lx24-amd64


echo "calling logol with parameters "$*

java -Xms512m -Xmx4096m -Dlogol.install=$LOGOL_HOME -Dlog4j.configuration=file://$LOGOL_HOME/log4j.properties -classpath  $LOGOL_HOME/lib/xalan.jar:$LOGOL_HOME/lib/xercesImpl.jar:$LOGOL_HOME/lib/xml-apis.jar:$LOGOL_HOME/lib/mail.jar:$LOGOL_HOME/lib/activation.jar:$LOGOL_HOME/lib/biojava.jar:$LOGOL_HOME/lib/bytecode:$LOGOL_HOME/lib/drmaa.jar:$LOGOL_HOME/lib/commons-configuration-1.5.jar:$LOGOL_HOME/lib/LogolExec.jar:$LOGOL_HOME/lib/commons-cli-1.1.jar:$LOGOL_HOME/lib/commons-collections-3.2.1.jar:$LOGOL_HOME/lib/commons-lang-2.4.jar:$LOGOL_HOME/lib/commons-logging-1.1.1.jar:$LOGOL_HOME/lib/log4j-1.2.15.jar:$LOGOL_HOME/lib/antlrworks-1.4.2.jar  org.irisa.genouest.logol.dispatcher.Dispatch  $* -conf /home/genouest/admin/galaxy/dependencies/logol/logol.dev.properties

