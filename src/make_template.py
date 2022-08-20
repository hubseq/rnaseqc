import json
MODULE = 'rnaseqc'

mi_template_json = {'module_version': '00.00.00', 'program_name': 'rnaseqc', 'program_subname': '', 'program_version': '3.4', 'compute': {'environment': 'aws', 'language': 'Python', 'language_version': '3.7', 'vcpus': 2, 'memory': 8000}, 'program_arguments': '', 'program_input': [{'input_type': 'file', 'input_file_type': 'BAM', 'input_position': 1, 'input_prefix': ''}], 'program_output': [{'output_type': 'folder', 'output_file_type': '', 'output_position': -1, 'output_prefix': ''}], 'alternate_inputs': [{'input_type': 'file', 'input_file_type': 'GTF', 'input_position': 0, 'input_prefix': ''}], 'alternate_outputs': [], 'defaults': {}}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_dryrun_json = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny1.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/rnaseqc/'], 'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.collapsed.GENCODE.gtf'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''}
io_json = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny1.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/rnaseqc/'], 'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.collapsed.GENCODE.gtf'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'}

with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)

# job info test JSONs                                                                                                        
job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/test/modules/"+MODULE+"/job/"+MODULE+".test.io.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test.job.json','w') as fout:
    json.dump(job_json, fout)
