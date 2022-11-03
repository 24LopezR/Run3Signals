import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--model', action='store', type=str, dest='model', default='', help='Model')
args = parser.parse_args()

if args.model == 'SquarkToNeutralinoTo2LNu':
	# SquarkToNeutralinoTo2LNu Model

	squark_masses = [1500]
	chi_masses = [494]
	ctau_values = [1000]
	
	f_in = open(args.model+"/SquarkToNeutralinoTo2LNu-fragment-template.py", "rt")


	for m_s in squark_masses:
        	for m_c in chi_masses:
                	for ctau in ctau_values:
                        	f_out_name = args.model+"/fragments/SquarkToNeutralinoTo2LNu_MSquark_{0}_MChi_{1}_ctau_{2}mm-fragment.py".format(m_s,m_c,ctau)
                        	f_out = open(f_out_name, "wt")
                        	filedata_temp = f_in.read()
                        	filedata_temp = filedata_temp.replace('msquark_template',str(m_s))
                        	filedata_temp = filedata_temp.replace('mchi_template',str(m_c))
                        	filedata_temp = filedata_temp.replace('ctau_template',str(ctau))
                        	f_out.write(filedata_temp)
                        	f_out.close()
	f_in.close()

elif args.model == 'StopToBottomL':
	# StopToBottomL Model

	masses = [1000]
	xsections = [0.00615134]
	ctau_values = [1000]

	f_in = open(args.model+"/StopToBottomL-fragment-template.py", "rt")


	for m in masses:
        	for xs in xsections:
                	for ctau in ctau_values:
                        	f_out_name = args.model+"/fragments/StopToBottomL_MStop_{0}_ctau_{1}mm-fragment.py".format(m,ctau)
                        	f_out = open(f_out_name, "wt")
                        	filedata_temp = f_in.read()
                        	filedata_temp = filedata_temp.replace('mass_template',str(m))
                        	filedata_temp = filedata_temp.replace('cross_section_template',str(xs))
                        	filedata_temp = filedata_temp.replace('ctau_template',str(ctau))
                        	f_out.write(filedata_temp)
                        	f_out.close()
	f_in.close()

