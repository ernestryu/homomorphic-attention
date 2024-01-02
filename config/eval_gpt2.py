# evaluate the base gpt2
# n_layer=12, n_head=12, n_embd=768
# 124M parameters
batch_size = 8
eval_iters = 300 # use more iterations to get good estimate
eval_only = True
wandb_log = True





dataset = 'openwebtext' 
# dataset = 'lambada' 
# dataset = 'wiki' 
# dataset = 'ptb' 
# dataset = 'TinyStories' 


init_from = 'finetune'  #'gpt-2' #'manipulate'




wandb_run_name= 'small-prbl-weighted' + dataset  #'gpt2-proj-block-12hd-weighted'#'only_qk_gpt2_MSE_combined' #'CRAMMED-GK-exp-12lyr-12-40-ddp'
wandb_project = 'finetune_score' #'FineTune Investigation' #'AttentionTransfer3'
out_dir = 'attn_transfer/second-12hd-2nd'