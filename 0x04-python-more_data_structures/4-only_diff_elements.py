# only_diff_elements -  returns a set of all elements present in only one set
#return: elements present in only one set

#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

	s3 = set_1.symmetric_difference(set_2);
	return s3;

