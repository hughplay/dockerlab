DEFAULT_TEMPLATE = "workspace_base"
TEMPLATE_SETTING = {
    "workspace_base": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_cuda_11_1": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_cuda_11_7": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "runtime_node_lts": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
    },
    "workspace_pytorch_1_13": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_pytorch_2_0": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_protein": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
}
