from modelestimator._bw_estimator.bw_estimator import bw_estimator
from modelestimator._handle_input.handle_input_file import handle_input_file
from modelestimator._bootstraper.bootstraper import bootstraper

def controller(file_format, bootstrap, resamplings, threshold, file_name_list):
    multialignment_list = []
    
    for file in file_name_list:
        multialignment = handle_input_file(file, file_format)
        multialignment_list.append(multialignment) 
        
    if threshold == None:
        threshold = 0.001
    
    if bootstrap:
        multialignment = multialignment_list[0]
        bootstrap_norm,_ = bootstraper(resamplings, threshold, multialignment)
        output_string = "Bootstrap norm = " + str(bootstrap_norm)
    else:
        q_matrix, eq = bw_estimator(threshold, multialignment_list)
        output_string = "Q =\n" + str(q_matrix) + "\nEQ =\n" + str(eq)   

    return output_string
