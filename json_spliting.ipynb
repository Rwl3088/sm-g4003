import json
import csv
origin_txt = 'text.out.txt'
th = open(origin_txt)
tx = th.read()
js = json.loads(tx)
title_counts = 0
mapped_title = 0
non_mapped = 0
non_snomed = 0
mapped_concept = 0
total_concepts = 0
pre_mapped_title_snomed = 0
Post_coord=0
corpus_list = js['AllDocuments']
output_list = []
mapped_list = []
unmapped_list=[]
non_snomed_list=[]
snomed_list=[]
pre_snomed=[]
for corpus in corpus_list:
    title_counts += 1
    c_non_mapping = 0
    c_mapping_count = 0
    c_non_snomedct = 0
    c_total_concepts = 0
    corpus_terms = corpus['Document']['Utterances']
    
    for term in corpus_terms: 
        corpus_id = term['PMID']
        outcome_title = term['UttText']
        term_phrases = term['Phrases']
        
        for phrase in term_phrases:
            c_mapping_count += 1
            if phrase['Mappings'] == []:
                c_non_mapping += 1
                continue
            phrases_mappings = phrase['Mappings']
            
            for mapping in phrases_mappings:
                mapping_scores = mapping['MappingScore']
                mapping_candidates_list = mapping['MappingCandidates']
                
                if len(mapping_candidates_list) = 1
                    for candidate_concept in mapping_candidates_list:
                        score = candidate_concept['CandidateScore']
                        CUI = candidate_concept['CandidateCUI']
                        concept_name = candidate_concept['CandidatePreferred']
                        source = candidate_concept['Sources']

                        
                        for candidate_concept in mapping_candidates_list:
                        score = candidate_concept['CandidateScore']
                        CUI = candidate_concept['CandidateCUI']
                        concept_name = candidate_concept['CandidatePreferred']
                        source = candidate_concept['Sources']
                        total_concepts += 1
                        c_total_concepts += 1
                
                        if 'SNOMEDCT_US' not in source:
                           c_non_snomedct += 1
                            continue
                            mapped_concept += 1
                            concept_row = [corpus_id, outcome_title, score, CUI, concept_name, source]
                            output_list.append(concept_row)
                    
    if c_mapping_count == c_non_mapping: 
        non_mapped += 1
        concept_row = [corpus_id, outcome_title,'','' ,'' ]
        output_list.append(concept_row)
        unmapped_list.append(concept_row)
    if c_mapping_count - c_non_mapping >0: 
        mapped_title += 1
        concept_row = [corpus_id, outcome_title, score, CUI, concept_name, source]
        mapped_list.append(concept_row)
    if c_total_concepts == c_non_snomedct and c_non_snomedct != 0 and c_total_concepts != 0:
        non_snomed += 1
        concept_row = [corpus_id, outcome_title,'','' ,'' ]
        output_list.append(concept_row)
        non_snomed_row = [corpus_id, outcome_title, score, CUI, concept_name, source]
        non_snomed_list.append(non_snomed_row)
    if c_total_concepts - c_non_snomedct == 1:
        pre_mapped_title_snomed +=1
        concept_row = [corpus_id, outcome_title, score, CUI, concept_name, source]
        snomed_list.append(concept_row)
    if c_total_concepts - c_non_snomedct > 1:
        Post_coord += 1
print('Total count of titles: ', title_counts)
print('Unmapped title: ', non_mapped)
print('Mapped title: ', mapped_title)
print('Titles pre_mapped to SNOMED_CT', pre_mapped_title_snomed)
print('Titles mapped but not mapped to SNOMED_CT: ', non_snomed)
print('Total concepts',total_concepts)
print('Concepts mapped to snomed: ', mapped_concept)
print('Under threshold 700, the match rate = ', pre_mapped_title_snomed / title_counts)
print('Average mapped concepts per title = ', mapped_concept/mapped_title_snomed )
new_csv = 'Threshold1000_outcome.csv'

csvFile = open(new_csv, 'w', newline='')
outputWriter = csv.writer(csvFile)

for row in output_list:
    outputWriter.writerow(row)
csvFile.close()
