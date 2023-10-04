import sys
import os
import pathlib



#file = sys.argv[1]
file = '/home/nisha/Desktop/Dinucleotide_project/a_manuscript_genomic_regions/various_genomic_regions/list'
current_path = str(pathlib.Path().absolute())
print (current_path)
with open(file,'r') as fh:
    for file_list in fh:
        file_list = file_list.strip()
        print("Running for ",end='\t')
        print(file_list)
        file_path = current_path+'/'+file_list
        print(file_path)
       
        input1 = file_list
        print(input1)
        
        input2 = file_list +'_median_stat.txt'
        print(input2)
        #output_stat = file_path+'/'+file_list+'_exon_stat.txt'

       
        # input1 = file_path+'/'+file_list+'_exon.txt'
        
        # input2 = file_path+'/'+file_list +'_exon_violin_arranged.txt'
        # #output_stat = file_path+'/'+file_list+'_exon_stat.txt'



        
        command3 = 'python3 stat-median.py '+input1+ '  > ' + input2

      
       
        os.system(command3)
        
        # #os.system(command9)
        # print(' stats done')

     
        print("Run completed for ",end='\t')
        print(file_list)


