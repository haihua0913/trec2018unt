"""
This Program performs the preprocessing of the Clinical Trials Document collection released by TREC PM 2017 for Task 2

In the pre-processing, the program extracts Brief_title, Official_title, Breif_summary, Purpose, Criteria, Gender, min_age, max_age, keywords and MeSH Termsfrom the Clinical Trials.

Following steps are performed by this program in order to perform preprocessing:
1. Imports and reads each Medline file inside the subfolders of source directory
2. Extracts Brief_title, Official_title, Breif_summary, Purpose, Criteria, Gender, min_age, max_age, keywords from each Clinical Trial using Regular expressions.
3. Converts the article structure into TREC Indexing format
4. Writes the processed articles into desired destination directory

To Run the Script:
$ python3 [source directory of collection] [destination directory]
     Example:
     $ python3 /home/lokesh/TREC_PM_2017_Document_Collection/ClinicalTrails/clinicaltrials_xml/ /home/lokesh/TREC_PM_2017_Document_Collection/ClinicalTrails/clinicaltrials_trecNew/
"""
import os
import re
import sys

if len(sys.argv)<2:
     print('[ERROR] Incomplete number of arguements')
elif len(sys.argv)==2:
     # Getting source collection directory from the arguements to python script
     source_path=sys.argv[0]
     # Getting destination directory from the arguements to python script
     dest_path=sys.argv[1]

source_dir='/home/lokesh/TREC_PM_2017_Document_Collection/ClinicalTrails/clinicaltrials_xml/'
dest_dir='/home/lokesh/TREC_PM_2017_Document_Collection/ClinicalTrails/clinicaltrials_trecNew/'

# Importing the file list from source directory
# The below code goes through the sub folders of clinical trials collection and imports the file list of raw data
sub_dirs=os.listdir(source_dir)
err_file=open('/home/lokesh/TREC_PM_2017_Document_Collection/ClinicalTrails/error_log_new.txt','a')
for folder in sub_dirs:
    sub_folders=os.listdir(source_dir+folder+'/')
    trec_dir=dest_dir+folder+'/'
    if not os.path.exists(trec_dir):
        os.makedirs(trec_dir)
    for sub_folder in sub_folders:
        # The below statement imports the file list into workspace
        xml_files=os.listdir(source_dir+folder+'/'+sub_folder+'/')
        # The below condition checks if the file is already processed or not
        if not os.path.exists(trec_dir+sub_folder+'.txt'):
            trec_trail=open(trec_dir+sub_folder+'.txt','a')
            # The below code performs preprocessing on each clinical trial
            for file in xml_files:
                trail_file=open(source_dir+folder+'/'+sub_folder+'/'+file)
                trail=trail_file.read()
                trec_trail.write('<DOC>\n')
                file_parts=file.split('.')

                # Extracting Document ID using Regular Expressions
                docid=file_parts[0]
                print(docid)
                # Writing Document ID into Output file
                trec_trail.write('<DOCNO>'+docid+'</DOCNO>\n')
                trec_trail.write('<TEXT>\n')
                
                # Extracting Brief title using Regular Expressions
                brief_title=re.search(r'<brief_title>(.*?)</brief_title>', trail, re.M|re.I|re.DOTALL)
                # Writing brief title into Output file
                if brief_title:
                    trec_trail.write('<brief_title>{0}</brief_title>\n'.format(brief_title.group(1)))
                else:
                    trec_trail.write('<brief_title></brief_title>\n')
                    err_file.write(docid+': brief_title does not exists \n')

                # Extracting Official title using Regular Expressions
                official_title=re.search(r'<official_title>(.*?)</offical_title>', trail, re.M|re.I|re.DOTALL)
                # Writing Official title into Output file
                if official_title:
                    trec_trail.write('<official_title>{0}</official_title>\n'.format(official_title.group(1)))
                else:
                    trec_trail.write('<official_title></official_title>\n')
                    err_file.write(docid+': official_title does not exists \n')

                # Extracting Brief Summary using Regular Expressions
                breif_summary=re.search(r'<brief_summary>(.*?)</brief_summary>', trail, re.M|re.I|re.DOTALL)
                # Writing brief summary into Output file
                if breif_summary:
                    breif_summary=re.sub('<textblock>','',breif_summary.group(1))
                    breif_summary=re.sub('</textblock>','',breif_summary)
                    trec_trail.write('<breif_summary>{0}</breif_summary>\n'.format(breif_summary))
                else:
                    trec_trail.write('<breif_summary></breif_summary>\n')
                    err_file.write(docid+': breif_summary does not exists \n')

                # Extracting Primary purpose using Regular Expressions
                purpose=re.search(r'<primary_purpose>(.*?)</primary_purpose>', trail, re.M|re.I|re.DOTALL)
                # Writing Primary purpose into Output file
                if purpose:
                    trec_trail.write('<purpose>{0}</purpose>\n'.format(purpose.group(1)))
                else:
                    trec_trail.write('<purpose></purpose>\n')
                    err_file.write(docid+': purpose does not exists \n')
                # Extracting Eligibility tag using Regular Expressions
                eligible=re.search(r'<eligibility>(.*?)</eligibility>', trail, re.M|re.I|re.DOTALL)
                if eligible:
                    # Extracting criteria using Regular Expressions
                    criteria=re.search(r'<criteria>(.*?)</criteria>', eligible.group(1), re.M|re.I|re.DOTALL)
                    # Writing criteria into Output file
                    if criteria:
                        criteria=re.sub('<textblock>','',criteria.group(1))
                        criteria=re.sub('</textblock>','',criteria)
                        trec_trail.write('<criteria>{0}</criteria>\n'.format(criteria))
                    else:
                        trec_trail.write('<criteria></criteria>\n')
                        err_file.write(docid+': criteria does not exists \n')

                    # Extracting Gender using Regular Expressions
                    gender=re.search(r'<gender>(.*?)</gender>', eligible.group(1), re.M|re.I|re.DOTALL)
                    # Writing gender information into Output file
                    if gender:
                        trec_trail.write('<gender>{0}</gender>\n'.format(gender.group(1)))
                    else:
                        trec_trail.write('<gender></gender>\n')
                        err_file.write(docid+': gender does not exists \n')

                    # Extracting Minimum Age using Regular Expressions
                    min_age=re.search(r'<minimum_age>(.*?)</minimum_age>', eligible.group(1), re.M|re.I|re.DOTALL)
                    # Writing Minimum age information into Output file
                    if min_age:
                        trec_trail.write('<min_age>{0}</min_age>\n'.format(min_age.group(1)))
                    else:
                        trec_trail.write('<min_age></min_age>\n')
                        err_file.write(docid+': min_age does not exists \n')

                    # Extracting Maximum age using Regular Expressions
                    max_age=re.search(r'<maximum_age>(.*?)</maximum_age>', eligible.group(1), re.M|re.I|re.DOTALL)
                    # Writing Maximum age information into Output file
                    if max_age:
                        trec_trail.write('<max_age>{0}</max_age>\n'.format(max_age.group(1)))
                    else:
                        trec_trail.write('<max_age></max_age>\n')
                        err_file.write(docid+': max_age does not exists \n')
                else:
                    trec_trail.write('<criteria></criteria>\n')
                    trec_trail.write('<gender></gender>\n')
                    trec_trail.write('<min_age></min_age>\n')
                    trec_trail.write('<max_age></max_age>\n')
                    err_file.write(docid+': eligible does not exists \n')

                # Extracting Keywords using Regular Expressions
                keywords=re.findall(r'<keyword>(.*?)</keyword>', trail, re.M|re.I|re.DOTALL)
                # Writing Keywords into Output file
                if keywords:
                    keywords=';'.join(keywords)
                    trec_trail.write('<keywords>{0}</keywords>\n'.format(keywords))
                else:
                    trec_trail.write('<keywords></keywords>\n')
                    err_file.write(docid+': keywords does not exists \n')

                # Extracting MeSH terms using Regular Expressions
                mesh_terms=re.findall(r'<mesh_term>(.*?)</mesh_term>', trail, re.M|re.I|re.DOTALL)
                # Writing MeSH terms into Output file
                if mesh_terms:
                    mesh_terms=';'.join(mesh_terms)
                    trec_trail.write('<mesh_terms>{0}</mesh_terms>\n'.format(mesh_terms))
                else:
                    trec_trail.write('<mesh_terms></mesh_terms>\n')
                    err_file.write(docid+': mesh_terms does not exists \n')
                trec_trail.write('</TEXT>\n')
                trec_trail.write('</DOC>\n')
                trail_file.close()
            trec_trail.close()
                
err_file.close()
