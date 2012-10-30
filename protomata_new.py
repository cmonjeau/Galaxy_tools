#!/usr/bin/env python
import sys
import os
from os.path import basename


def __main__():
	# arguments recuperation
    	input_seq = sys.argv[1]
	input2_seq = sys.argv[2]
	redundant = sys.argv[3]
	significativity = sys.argv[4]
	max_fragment_size = sys.argv[5]
	afc_output = sys.argv[6]
	consensus = sys.argv[7]
	plma_output = sys.argv[8]
	dot_output = sys.argv[9]
	proto_output = sys.argv[10]
	plma_dot_output = sys.argv[11]
	proto_dot_output = sys.argv[12]
	weight_sequences = sys.argv[13]
	quorum_value = sys.argv[14]
	indices = sys.argv[15]
	dot_output_png = sys.argv[16]
	dot_output = sys.argv[17]
	plma_dot_output_png = sys.argv[18]
	proto_dot_output_png = sys.argv[19]
	dot_output_svg = sys.argv[20]
	plma_dot_output_svg = sys.argv[21]
	proto_dot_output_svg = sys.argv[22]
	proto_logo_output = sys.argv[23]
	protobuild_plma_output = sys.argv[24]

	# redundant test

	if redundant != "none":
		os.system('cd-hit -i ' + input_seq + ' -o ' + input2_seq + ' -c ' + redundant)
		os.system('dialign -nta -thr ' + significativity + " -lmax " + max_fragment_size + " -afc -fn /opt/galaxy-dist/database/tmp/my_afc_file " + input2_seq)
		os.system('mv /opt/galaxy-dist/database/tmp/my_afc_file.afc > ' + afc_output)
		os.system('paloma --training-sequences-input ' + input2_seq + ' --threshold '  + significativity + ' --min-size 1 --max-size ' +  max_fragment_size + ' --'+consensus + ' --plma-output ' + plma_output + ' --use-afc ' + afc_output)
		os.system('plma2dot -i ' + plma_output + ' -o ' + dot_output)

		# remove cd-hit output (.clstr , .bak.clstr)
		os.system('rm ' + input2_seq + '.clstr')
		os.system('rm ' + input2_seq + '.bak.clstr')
	else:
		
		os.system('dialign -nta -thr ' + significativity + ' -lmax ' + max_fragment_size + ' -afc -fn /opt/galaxy-dist/database/tmp/my_afc_file ' + input_seq)
		os.system('mv /opt/galaxy-dist/database/tmp/my_afc_file.afc > ' + afc_output)
		os.system('paloma --training-sequences-input ' + input_seq + ' --threshold '  + significativity + ' --min-size 1 --max-size ' +  max_fragment_size + ' --'+ consensus + ' --plma-output ' + plma_output + ' --use-afc ' + afc_output)
		os.system('plma2dot -i ' + plma_output + ' -o ' + dot_output)

	# weight sequences test and probuild execution

	file_path=os.path.splitext(plma_output)[0]

	if weight_sequences == "weight-sequences":
		os.system('protobuild --plma-input ' + plma_output + ' --proto-output ' + proto_output + ' --plma-dot-output ' + plma_dot_output + ' --proto-dot-output ' + proto_dot_output + ' --weight-sequences --percentage-quorum ' + quorum_value + ' --pseudocounts Dirichlet --components ' + indices)
		os.system('mv '+ file_path +'_p' + quorum_value + 'w' + '.plma '+ protobuild_plma_output)
	else:
		os.system('protobuild --plma-input ' + plma_output + ' --proto-output ' + proto_output + ' --plma-dot-output ' + plma_dot_output + ' --proto-dot-output ' + proto_dot_output + ' --percentage-quorum ' + quorum_value + ' --pseudocounts Dirichlet --components ' + indices)
		os.system('mv '+ file_path +'_p' + quorum_value + '.plma '+ protobuild_plma_output)

	# images generations

	os.system('dot -o ' + dot_output_png + ' -Tpng ' + dot_output)
	os.system('dot -o ' + plma_dot_output_png + ' -Tpng ' + plma_dot_output)
	os.system('dot -o ' + proto_dot_output_png + ' -Tpng ' + proto_dot_output)
	
	os.system('dot -o ' + dot_output_svg + ' -Tsvg ' + dot_output)
	os.system('dot -o ' + plma_dot_output_svg + ' -Tsvg ' + plma_dot_output)
	os.system('dot -o ' + proto_dot_output_svg + ' -Tsvg ' + proto_dot_output)

	os.system('sh /home/genouest/admin/galaxy/dependencies/protomata/proto2logojpg.sh ' + proto_output + ' /opt/galaxy-dist/database/tmp/proto.jpg')
	os.system('mv /opt/galaxy-dist/database/tmp/proto.jpg ' + proto_logo_output)

	# remove tmp file

	os.system('rm /opt/galaxy-dist/database/tmp/my_afc_file.afc')



if __name__ == "__main__": __main__()
